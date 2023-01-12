import csv, itertools


def get_ddis(ls_medocs):

    with open('db_ml_interaction_model_mie23.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        ddireader = list(reader)
        ls_ddi = []
        ls_combis = itertools.combinations(ls_medocs, 2)
        for c in ls_combis:
            for row in ddireader:
                if((c[0]==row[0] and c[1]==row[1]) or (c[1]==row[0] and c[0]==row[1])):
                    if(row[3]== "2/1"):
                        #drug1, drug2, mechanism, action, property, description
                        row_r = [None] * 6
                        row_r[0] = row[1]
                        row_r[1] = row[0]
                        row_r[2] = row[2]
                        row_r[3] = "1/2"
                        row_r[4] = row[4]
                        row_r[5] = row[5]
                        ls_ddi.append(row_r)
                    else:
                        ls_ddi.append(row)
    return ls_ddi

def check_inter(inter):
    if(inter[3]=="1+2"):
        print(inter[4], "of ", inter[0], "and", inter[1], "are ", inter[2],"d", "  :   ", inter[5])
    elif(inter[3]=="1/2"):
        print(inter[0], " " , inter[2], " ", inter[4], "of", inter[1], "  :   ", inter[5])
    elif (inter[3] == "2/1"):
        print(inter[1], " ", inter[2], " ", inter[4], "of", inter[0], "  :   ", inter[5])
ls_medocs = ['Abemaciclib', 'Diltiazem', 'Doxorubicin', 'Doxycycline', 'Dronedarone','Dihydroergotamine']
drug_test = ["Abiraterone", "Digoxin", "Cyproteroneacetate", "Cyclophosphamide", "Captopril", "Bisoprolol", "Bupropion"]

inters = get_ddis(drug_test)
for i in inters:
    check_inter(i)


def Sort(sub_li, pos):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.sort(key=lambda x: x[pos])
    return sub_li


def get_ddi_by_effects(ddis_full):
    # select PD inters
    pd_ddis = []
    for ddi in ddis_full:
        if(ddi[4] not in ["A", "D", "M", "E", "Bio_A"]):
            pd_ddis.append(ddi)

    # sort by effect (property = 4th)
    ddis = Sort(pd_ddis, 4)

    ls_directions = []
    ls_d1 = []
    ls_d2 = []
    ls_mechanism = []
    ls_effects = []
    #Distinct Effects !
    for ddi in ddis:
        if (ddi[3] == "1+2"):
            ls_directions.append("--+--")
            ls_d1.append(ddi[0])
            ls_d2.append(ddi[1])
            ls_mechanism.append(ddi[2])
            ls_effects.append(ddi[4])
        else:
            ls_directions.append("----->")
            ls_d1.append(ddi[0])
            ls_d2.append(ddi[1])
            ls_mechanism.append(ddi[2])
            ls_effects.append(ddi[4])


    return [ls_d1, ls_directions, ls_d2, ls_mechanism, ls_effects]


def get_ddi_by_victim_pk(ddis_full):
    # select PK inters
    pk_ddis = []
    for ddi in ddis_full:
        if(ddi[4] in ["A", "D", "M", "E", "Bio_A"]):
            pk_ddis.append(ddi)
            print(ddi)


    # sort by victime drug
    ddis = Sort(pk_ddis, 1)

    ls_directions = []
    ls_d1 = []
    ls_d2 = []
    ls_mechanism = []
    ls_phases = []

    for ddi in ddis:
        if (ddi[3] == "1+2"):
            ls_directions.append("--+--")
            ls_d1.append(ddi[0])
            ls_d2.append(ddi[1])
            ls_mechanism.append(ddi[2])
            action_phase = "%s %s"%(ddi[2], ddi[4])
            ls_phases.append(action_phase)
        else:
            ls_directions.append("----->")
            ls_d1.append(ddi[0])
            ls_d2.append(ddi[1])
            ba_cons = ddi[2]
            if(ddi[4] in ["M", "E"]):
                if(ddi[2]=="decrease"):
                    ba_cons = "increase"
                elif(ddi[2] == "increase"):
                    ba_cons = "decrease"
            ls_mechanism.append(ba_cons)
            action_phase = "%s %s" % (ddi[2], ddi[4])
            ls_phases.append(action_phase)

    return [ls_d1, ls_directions, ls_d2, ls_phases, ls_mechanism]


ddi_by_effects = get_ddi_by_effects(inters)
ddi_by_pk = get_ddi_by_victim_pk(inters)


# Generate multiple interations

# PKs inters
# ### by victim drug  & Action on Bio A

# PDs inters
# ### by effect & Action on effect # Later, it will be distributed according
#                                    to the drugs involved in inters PK Having
#                                    the same action

#PK & PD
# ### by effect & Action on effect & Action on Bio A of involved drugs with Pk interactions



import plotly.graph_objects as go



fig1 = go.Figure(data=[go.Table(header=dict(values=['Perpetrator Drug', 'Direction' ,'Victim Drug', "Action", "Effect"]),
                 cells=dict(values=[
                                    ddi_by_effects[0],
                                    ddi_by_effects[1],
                                    ddi_by_effects[2],
                                    ddi_by_effects[3],
                                    ddi_by_effects[4]
                                    ]))])
fig1.show()


fig2 = go.Figure(data=[go.Table(header=dict(values=['Perpetrator Drug', 'Direction' ,'Victim Drug', "Action on Bio availability phase", "Bio availability conseqence"]),
                 cells=dict(values=[
                                    ddi_by_pk[0],
                                    ddi_by_pk[1],
                                    ddi_by_pk[2],
                                    ddi_by_pk[3],
                                    ddi_by_pk[4]
                                    ]))])
fig2.show()

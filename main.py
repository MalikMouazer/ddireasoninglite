import csv, itertools


def get_ddis(ls_medocs):

    with open('interactions_modele_4.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        ddireader = list(reader)
        ls_ddi = []
        ls_combis = itertools.combinations(ls_medocs, 2)
        for c in ls_combis:
            for row in ddireader:
                if((c[0]==row[0] and c[1]==row[1]) or (c[1]==row[0] and c[0]==row[1])):
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


def get_ddi_by_effects(ddis_full):

    ddis = []
    for ddi in ddis_full:
        if(ddi[4] not in ["A", "D", "M", "E"]):
            ddis.append(ddi)

    # select PD inters
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
        elif (ddi[3] == "1/2"):
            ls_directions.append("----->")
            ls_d1.append(ddi[0])
            ls_d2.append(ddi[1])
            ls_mechanism.append(ddi[2])
            ls_effects.append(ddi[4])
        elif (ddi[3] == "2/1"):
            ls_directions.append("----->")
            ls_d1.append(ddi[1])
            ls_d2.append(ddi[0])
            ls_mechanism.append(ddi[2])
            ls_effects.append(ddi[4])

    return [ls_d1, ls_directions, ls_d2, ls_mechanism, ls_effects]


ddi_by_effects = get_ddi_by_effects(inters)

import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(header=dict(values=['Drug1', 'Direction' ,'Drug2', "Mechanism", "Effect"]),
                 cells=dict(values=[
                                    ddi_by_effects[0],
                                    ddi_by_effects[1],
                                    ddi_by_effects[2],
                                    ddi_by_effects[3],
                                    ddi_by_effects[4]
                                    ]))])
fig.show()
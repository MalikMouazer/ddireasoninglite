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

ls_medocs = ['Abemaciclib', 'Diltiazem', 'Doxorubicin', 'Doxycycline', 'Dronedarone','Dihydroergotamine']

inters = get_ddis(ls_medocs)
for i in inters:
    print(i)
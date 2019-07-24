data_list = [ 'itn_0040',  'itn_0046',  'itn_0042',  'int_0060',  'bht_0072',  'itn_0047',  'bht_0079',  'itn_0059',  'itn_0099',
  'bht_0080',  'itn_0109',  'itn_0093',  'itn_0133',  'itn_0050',  'itn_0041',  'itn_0100',  'bht_0071',  'itn_0083',
  'itn_0094',  'itn_0058',  'itn_0113',  'itn_0048',  'itn_0075',  'itn_0062',  'itn_0073',  'itn_0089',  'bht_0060',
  'itn_0104',  'itn_0107',  'itn_0118',  'itn_0037',  'itn_0098',  'bht_0069',  'itn_0135',  'itn_0065',  'itn_0034',
  'itn_0049',  'itn_0067',  'itn_0087',  'itn_0053',  'itn_0090',  'itn_0063',  'itn_0054',  'itn_0051',  'bht_0078',
  'itn_0097',  'itn_0068',  'itn_0101',  'itn_0108',  'itn_0106',  'itn_0064',  'itn_0110',  'itn_0069',  'itn_0121',
  'itn_0124',  'itn_0132',  'bht_0074',  'itn_0061',  'itn_0120',  'itn_0123',  'itn_0134',  'itn_0045',  'itn_0072',
  'itn_0070',  'bht_0073',  'itn_0112',  'itn_0129',  'itn_0111',  'itn_0044',  'itn_0079',  'bht_0064',  'itn_0055',
  'itn_0066',  'itn_0117' ]
data_dict = {}
'''DATA COMPILATION'''
for id in data_list:
    data_dict[id] = []
MDE = [4, 4, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 3, 1, 3, 1, 4, 1, 1, 1, 1, 1, 1, 3, 1, 1, 4, 3, 2, 2, 1, 2, 4, 3, 4, 3, 2, 3, 2, 1, 1, 3, 4, 1, 2, 3, 1, 1, 3, 1, 1, 1, 2, 1, 1, 1, 4, 2, 1, 1, 1, 4, 1, 1, 2, 1, 1, 1, 3, 1, 1, 2, 4, 2]
for id in data_dict:
    data_dict[id].append(MDE.pop(0))
PDD = [4, 4, 2, 2, 4, 4, 3, 1, 1, 4, 3, 4, 4, 1, 3, 1, 4, 1, 4, 4, 4, 1, 4, 4, 4, 2, 4, 3, 1, 4, 4, 2, 4, 4, 1, 4, 2, 3, 1, 1, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 1, 4, 4, 4, 1, 3, 4, 2, 3, 1, 2, 3, 2, 4, 4, 1, 4, 4, 4, 1, 4, 1, 4, 4]
for id in data_dict:
    data_dict[id].append(PDD.pop(0))
MDD = [3, 3, 1, 1, 1, 1, 3, 1, 1, 4, 3, 1, 3, 3, 3, 1, 4, 1, 3, 1, 4, 1, 1, 3, 4, 2, 3, 3, 1, 2, 1, 1, 4, 4, 3, 3, 1, 3, 1, 1, 1, 3, 3, 4, 1, 3, 1, 3, 3, 1, 1, 4, 2, 1, 2, 3, 4, 1, 1, 1, 1, 3, 1, 1, 4, 1, 1, 3, 4, 1, 1, 1, 4, 2]
for id in data_dict:
    data_dict[id].append(MDD.pop(0))
OSDD = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 2, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 3]
for id in data_dict:
    data_dict[id].append(OSDD.pop(0))
# severity = [3.53, 4.12, -1.0, 5.64, 5.15, 6.62, 5.96, 6.29, 5.68, 6.29, 6.61, 4.6, 8.64, 6.4, 7.01, 6.21, 1.25, 5.5, 6.62, -1.0, 4.74, 5.04, 5.37, 4.44, 6.5, 7.07, 2.92, 6.54, 5.79, 6.54, 5.18, 2.5, 4.38, 5.26, 2.92, 1.67, 4.96, 4.52, 5.71, 6.32, 6.0, 6.04, 5.41, 7.72, 7.06, -1.0, 6.03, 6.36, 5.4, 6.68, 5.04, 5.99, 6.03, 6.69, 5.86, -1.0, -1.0, 2.5, 7.89, -1.0, 7.0, 5.57, 5.89, 8.01, 4.14, 6.79, 5.86, 6.03, 4.77, 4.79, 7.61, 6.79, 5.29, 5.59]
# for id in data_dict:
#     data_dict[id].append(severity.pop(0))
# for id in data_dict:
#     data_dict[id].append('y')
# data_dict["bht_0080"][5] = "n"
# data_dict["bht_0071"][5] = "n"
# data_dict["bht_0069"][5] = "n"
# data_dict["bht_0074"][5] = "n"
# data_dict["itn_0066"][5] = "n"
# num = "00111111111101010111111011001111001010111001101101111111011110111111011101"
# for id in data_dict:
#     data_dict[id].append(num[0])
#     num = num[1:]
def sensitivity_finder(a,c):
    try:
        return round(a/(a+c), 4)
    except:
        return 0
#Finds Specificity
def specificity_finder(b,d):
    try:
        return round(d/(b+d), 4)
    except:
        return 0
def accuracy_finder(a,b,c,d):
    return round((a+d)/(a+b+c+d),4)
# '''
# The bound for severity scores is 4. If there is a severity score of less
# than 4, do not consider SAGE data for that patient. If there is a severity
# score of greater than 4 and there is no SAGE diagnosis, it should have one.
# '''
# ids_to_remove = set()
# ids_to_add = []
# for id in data_dict:
#     if data_dict[id][4] < 4:
#         ids_to_remove.add(id)
#     else:
#         if data_dict[id][6] == '0':
#             ids_to_add.append(id)
# for id in ids_to_remove:
#     if data_dict[id][0] == 2:
#         data_dict[id][0] = 4
#     if data_dict[id][0] == 1:
#         data_dict[id][0] = 3
#     if data_dict[id][2] == 2:
#         data_dict[id][2] = 4
#     if data_dict[id][2] == 1:
#         data_dict[id][2] = 3
# # print(ids_to_add)
# # print(data_dict)
# for id in ids_to_add:
#     if data_dict[id][0] == 3:
#         data_dict[id][0] = 1
#     if data_dict[id][0] == 4:
#         data_dict[id][0] = 2
#     if data_dict[id][2] == 3:
#         data_dict[id][2] = 1
#     if data_dict[id][2] == 4:
#         data_dict[id][2] = 2

def kappa_finder(a,b,c,d):
    try:
        total = a+b+c+d
        p_0 = (a + d)/total
        p_e = ((a+b)/total)*((a+c)/total) + ((c+d)/total)*((b+d)/total)
        return round((p_0-p_e)/(1-p_e), 3)
    except:
        return -100
print(len(data_dict))
final = []
result = []
for i in range(4):
    a = 0
    b = 0
    c = 0
    d = 0
    for id in data_dict:
        num = data_dict[id][i]
        if num == 1:
            a += 1
        if num == 2:
            b += 1
        if num == 3:
            c += 1
        if num == 4:
            d += 1
    kappa = kappa_finder(a,b,c,d)
    result.append((sensitivity_finder(a,c), specificity_finder(b,d), accuracy_finder(a,b,c,d)))
    final.append(kappa)
    print(a,b,c,d)
print(result)
print(final)

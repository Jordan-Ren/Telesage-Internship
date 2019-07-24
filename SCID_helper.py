num = "33111111121131314111111311331111431313111331131131111111411113111111311141"
a =0
b=0
def sensitivity_finder(a,c):
    try:
        return round(a/(a+c), 3)
    except:
        return 0
#Finds Specificity
def specificity_finder(b,d):
    try:
        return round(d/(b+d), 3)
    except:
        return 0
def kappa_finder(a,b,c,d):
    total = a+b+c+d
    print(total)
    p_0 = (a + d)/total
    p_e = ((a+b)/total)*((a+c)/total) + ((c+d)/total)*((b+d)/total)
    return round((p_0-p_e)/(1-p_e), 3)
c=0
d=0
for val in num:
    if val == '1':
        a += 1
    if val == '2':
        b += 1
    if val == '3':
        c += 1
    if val == '4':
        d += 1
print(a,b,c,d)
print(kappa_finder(a,b,c,d))
print(specificity_finder(b,d))
print(sensitivity_finder(a,c))

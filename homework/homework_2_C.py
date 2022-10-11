def kekw(value, base):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r=""
    while(value>0):
        k=value%base   
        r=digits[k]+r
        value=value//base
    return r

print(kekw(2,2))
print(kekw(10,16))
print(kekw(35,36))
def decrypt(Security):
    
    codeList = []
    codeLength = len(Security)
    codeRange = codeLength / 3

    for i in range(0, codeRange):

        x = i * 3
        y = x + 3

        codeRead = Security[x:y]

        if codeRead == 'XXX' or codeRead == 'XYX':
            codes = 'Intruder '
        elif codeRead == 'XXY' or codeRead == 'XYY':
            codes = 'Identified '
        else:
            codes = 'False Alarm '

        codeList.append(codes)
        codeJoin = "".join(codeList)
    return codeJoin

securityCode = raw_input("Enter your security code:")
decryptedCode = decrypt(securityCode)
print(decryptedCode)
        
        
ofile = open("codeDecrypted.txt", "w")
f = open("Securitycode.txt", "r+")
for list in f:
    fileDecrypted = decrypt(list)
    ofile.write(fileDecrypted)
ofile.close()
f.close()   

            

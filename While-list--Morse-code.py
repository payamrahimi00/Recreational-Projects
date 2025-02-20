j=True
while j:
        
 req=input("insert your chr:")
 if req=="":
    j=False
 else:
     pass

 Mourse__code={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":".."
              ,"J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-"
              ,"R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-",
              "Y":"-.--","Z":"--.."}
 val=list(Mourse__code.values())
 for Key,valuse in Mourse__code.items():
 
    if req in Key=="A":
        print(val[0])
    elif req in Key=="B":
        print(val[1])
    elif req in Key=="C":
        print(val[2])
    elif req in Key=="D":
        print(val[3])
    elif req in Key=="E":
        print(val[4])
    elif req in Key=="F":
        print(val[5])
    elif req in Key=="G":
        print(val[6])
    elif req in Key=="H":
        print(val[7])
    elif req in Key=="I":
        print(val[8])
    elif req in Key=="J":
        print(val[9])
    elif req in Key=="K":
        print(val[10])
    elif req in Key=="L":
        print(val[11])
    elif req in Key=="M":
        print(val[12])
    elif req in Key=="N":
        print(val[13])
    elif req in Key=="O":
        print(val[14])
    elif req in Key=="P":
        print(val[15])
    elif req in Key=="Q":
        print(val[16])
    elif req in Key=="R":
        print(val[17]) 
    elif req in Key=="S":
        print(val[18]) 
    elif req in Key=="T":
        print(val[19])      
    elif req in Key=="U":
        print(val[20])  
    elif req in Key=="V":
        print(val[21]) 
    elif req in Key=="W":
        print(val[22]) 
    elif req in Key=="X":
        print(val[23])
    elif req in Key=="Y":
        print(val[24])  
    elif req in Key=="Z":
        print(val[25]) 
    # elif req in Key=="U":
    #     print(val[26]) 
    else:
        pass
        

        
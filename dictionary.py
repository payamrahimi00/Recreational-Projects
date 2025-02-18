matty=int(input("Insert code org:"))
John={("Pid",):"12345678911","Relationship":"Sis","Family":"XXFamily"}
Mikel={("Pid",):"12345678911","Relationship":"Sis","Family":"XXXFamily"}
Leo={("Pid",):"12345678911","Relationship":"Sis","Family":"XXXFamily"}
windows={("Pid",):"12345678911","Relationship":"Sis","Family":"XXXFamily"}
Goat={("Pid",):"12345678911","Relationship":"Sis","Family":"XXXFamily"}
if matty==1:
    print(John)
elif matty==10:
    print(John[("Pid",)])
elif matty==101:
    print(John["Relationship"])
elif matty==1012:
    print(John["Family"])
elif matty==2:
    print(Mikel)
elif matty==20:
    print(Mikel[("Pid",)])
elif matty==201:
    print(Mikel["Relationship"])
elif matty==2012:
    print(Mikel["Family"])
elif matty==3:
    print(Leo)
elif matty==30:
    print(Leo[("Pid",)])
elif matty==301:
    print(Leo["Relationship"])
elif matty==3012:
    print(Leo["Family"])
elif matty==4:
    print(windows)
elif matty==40:
    print(windows[("Pid",)])
elif matty==401:
    print(windows["Relationship"])
elif matty==4012:
    print(windows["Family"])
elif matty==5:
    print(Goat)
elif matty==50:
    print(Goat[("Pid",)])
elif matty==501:
    print(Goat["Relationship"])
elif matty==5012:
    print(Goat["Family"])
else:
    pass




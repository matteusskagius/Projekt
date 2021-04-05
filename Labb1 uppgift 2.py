p=6

def recept(antal):
    print("Personer",antal)
    print()
    print("1)")             #1
    print("Ägg", int((3/4)*antal),"st")         
    print("Strösocker",(3/4)*antal,"dl")              
    print("Vaniljsocker",(2/4)*antal,"tsk")              
    print("Bakpulver",(2/4)*antal,"tsk")              
    print("Vetemjöl",(3/4)*antal,"dl")              
    print("Smör",(75/4)*antal,"g")             
    print("Vatten",(1/4)*antal,"dl")



recept(p)


print()
print()
print()
print("2)")                 #2
def tidBlanda(antal):
    print("Omrörningstid",(10+1*antal))

tidBlanda(p)


def tidGradda(antal):
    print("tid grädda",(30+3*antal))

tidGradda(p)


print()
print()
print()
print("3)")                 #3
def sockerkaka(antal):
        print("Ingredienser")
        print("Ägg", int((3/4)*antal),"st")         
        print("Strösocker",(3/4)*antal,"dl")              
        print("Vaniljsocker",(2/4)*antal,"tsk")              
        print("Bakpulver",(2/4)*antal,"tsk")              
        print("Vetemjöl",(3/4)*antal,"dl")              
        print("Smör",(75/4)*antal,"g")             
        print("Vatten",(1/4)*antal,"dl")
        print()
        print("Tid")
        print("Omrörningstid",(10+1*antal))  
        print("tid grädda",(30+3*antal))

sockerkaka(p)

print()
print()
print()

print("4)")                 #4



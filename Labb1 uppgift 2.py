def recept(antal):  #definierar recept som funktion
    print("Personer",antal)
    #print()
    #print("1)")             #1
    #print()
    print("Ägg", int((3/4)*antal),"st")         
    print("Strösocker",(3/4)*antal,"dl")              
    print("Vaniljsocker",(2/4)*antal,"tsk")              
    print("Bakpulver",(2/4)*antal,"tsk")              
    print("Vetemjöl",(3/4)*antal,"dl")              
    print("Smör",(75/4)*antal,"g")             
    print("Vatten",(1/4)*antal,"dl")

#print("2)")                 #2
def tidBlanda(antal):
    print("Omrörningstid",(10+1*antal))

def tidGradda(antal):
    print("tid grädda",(30+3*antal))




#print("3)")                 #3

def sockerkaka(antal):
        recept(antal)
        tidBlanda(antal)
        tidGradda(antal)
            
        
    
        

#sockerkaka(p)





print("4)")                 #4



        

sockerkaka(4)
print()
print()
sockerkaka(7)

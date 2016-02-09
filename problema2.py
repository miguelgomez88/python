import random

N = 1000
p1 = 0
p2 = 0
p3 = 0

for i in range(N):
    exp = ["cabra", "cabra", "cabra"]
    coche = random.randrange(3)
    exp[coche] = "coche"
    
    player = random.randrange(3)
    
    selec = [x for x in range(3) if exp[x] is not "coche" and x is not player][0]
    
    laOtra = [x for x in range(3) if x is not player and x is not selec][0]
    print exp, coche, player, selec, laOtra        
                
    if player==coche:
        p1+=1    
        
    if laOtra==coche:
        p3+=1            
            
    if random.randint(0, 1) == 0:   
        if player==coche:
            p2+=1
    else:                   
        if laOtra== coche:
            p2+=1
    print "-----------------------------"
    
print float(p1)/N*100,"%"
print float(p2)/N*100,"%"
print float(p3)/N*100,"%"                

        
    
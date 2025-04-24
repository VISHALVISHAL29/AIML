Jug1=3
Jug2=5
Target = 4

X=0
Y=0

def state(X,Y):
  
  a=[]

  a.append((Jug1,Y))
  a.append((X,Jug2))
  a.append((X,0))
  a.append((0,Y))

  set(a)

  pour = min(X,Jug1-Y)
  



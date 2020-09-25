
from gurobipy import *

m = Model("Proyecto")


##Variables
w = m.addVar(vtype=GRB.BINARY, name="w")
x = m.addVar(vtype=GRB.BINARY, name="x")
y = m.addVar(vtype=GRB.BINARY, name="y")
z = m.addVar(vtype=GRB.BINARY, name="z")

m.update()


##Función objetivo
m.setObjective( , GRB.MINIMIZE)

##Restricciones

m.addConstr( , "C1")
m.addConstr( , "C2")
m.addConstr( , "C3")
m.addConstr( , "C4")
m.addConstr( , "C5")
m.addConstr( , "C6")
m.addConstr( , "C7")

m.optimize()



##
for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
print(f'Obj: {m.objVal}')
m.write('example.lp')

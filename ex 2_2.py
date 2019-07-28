from pulp import *
prop = LpProblem("The Agriculture Institute", LpMinimize)
x = LpVariable("No. of bags Of Mixture A", 0, None, LpInteger)
y = LpVariable("No. of Bags of Mixture B", 0, None, LpInteger)
prop += 40*x + 24*y
prop += 20*x + 50*y >= 4800, "Phosphate requirement"
prop += 80*x + 50*y >= 7200, "Nitrogen Requirement"
prop.writeLP("ex 2_2.Lp")
prop.solve()
print("Status:", LpStatus[prop.status])
for v in prop.variables():
    print(v.name, "+", v.varValue)
print("The required fertilizer at minimum cost",value(prop.objective))
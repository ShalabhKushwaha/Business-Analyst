from pulp import *

prop = LpProblem("The Raw Material", LpMaximize)
x1 = LpVariable("Product A Units ", 0, None, LpInteger)
x2 = LpVariable("Product B Units", 0, None, LpInteger)
prop += 40 * x1 + 35 * x2
prop += 2 * x1 + 3 * x2 <= 60, "The Raw Material Constraint(in Kg)"
prop += 4 * x1 + 3 * x2 <= 96, "The Labour Hrs Constraint(In HRs)"
prop.writeLP("Example 2_1.Lp")
prop.solve()
print("Satus:",LpStatus[prop.status])
for v in prop.variables():
    print(v.name, "=", v.varValue)
print("The maximum profit a firm can earn:", value(prop.objective))

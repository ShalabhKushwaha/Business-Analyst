
# import PuLP
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Miracle Worker", LpMaximize)

# Create problem variables
x=LpVariable("Medicine_1_units",0,None,LpInteger)
y=LpVariable("Medicine_2_units",0, None, LpInteger)

# The objective function is added to 'prob' first
prob += 10*x + 20*y, "Health restored; to be maximized"
# The two constraints are entered
prob += 3*x + 4*y <= 25, "Herb A constraint"
prob += 2*x + y <= 10, "Herb B constraint"

# The problem data is written to an .lp file
prob.writeLP("MiracleWorker.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])
# Output=
# Status: Optimal

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)
# Output=
# Medicine_1_units = 3.0
# Medicine_2_units = 4.0

# The optimised objective function value is printed to the screen
print("Total Health that can be restored = ", value(prob.objective))
# Output=
# Total Health that can be restored =  155.0
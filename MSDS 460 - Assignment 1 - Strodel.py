# Import packages
import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# Create function that takes cost and servings per container and calculates cost per serving (cps)
def cost_per_serving(cost, servings):
    return round(cost / servings, 2)

# Calculate unit costs for each food item: eggs, milk, vitamins, vegetables, cheerios
# Eggs
cps_eggs = cost_per_serving(1.49, 12)

# milk
cps_milk = cost_per_serving(1.89, 8)

# vitamins (using cost divided by two because these are always buy-one-get-one)
cps_yog = cost_per_serving(5.99, 5)

# vegetables
cps_veg = cost_per_serving(2.59, 10)

# cheerios
cps_cheerios = cost_per_serving(3.69, 6)

# print all cost per servings
print(f'Eggs: {cps_eggs} per serving\nMilk: {cps_milk} per serving\nYogurt: {cps_vit} per serving\nVegetables: {cps_veg} per serving\nCheerios: {cps_cheerios} per serving')

# define variables
eggs = LpVariable('Eggs', 0, None) # eggs >= 0
milk = LpVariable('Milk', 0, None) # milk >= 0
yogt = LpVariable('Yogurt', 0, None) # vitamins >=0
vegs = LpVariable('Vegetables', 0, None) # vegetables >= 0
chrs = LpVariable('Cheerios', 0, None) # cheerios >= 0

# define problem
prob = LpProblem('problem', LpMinimize) # minimize cost

# define constraints
prob += eggs * 70 + milk * 115 + yogt *  60 + vegs *  10 + chrs * 190 <= 5000 # milligrams of sodium
prob += eggs * 70 + milk * 120 + yogt * 130 + vegs *  60 + chrs * 140 >= 2000 # calories
prob += eggs *  6 + milk *   8 + yogt *  14 + vegs *   2 + chrs *   5 >=   50 # grams of protein
prob += eggs *  1 + milk *   3 + yogt *   0 + vegs *   0 + chrs *   4 >=   20 # micrograms of Vitamin D
prob += eggs * 30 + milk * 292 + yogt * 170 + vegs *   0 + chrs * 130 >= 1300 # milligrams of calcium
prob += eggs *  1 + milk *   0 + yogt *   0 + vegs *   1 + chrs *  13 >=   18 # milligrams of iron
prob += eggs * 70 + milk * 341 + yogt * 220 + vegs * 171 + chrs * 250 >= 4700 # milligrams of potassium

# define objective function
prob += cps_eggs * eggs + cps_milk * milk + cps_yog * yogt + cps_veg * vegs + cps_cheerios * chrs

# solve the problem
status = prob.solve()
print(f'Diet Problem\nStatus: {LpStatus[status]}')

# print results
print(f'Servings of:')
for variable in prob.variables():
    print(f'  - {variable.name} = {round(variable.varValue, 2)}')
print(f'Minimized Cost: {round(value(prob.objective), 2)}')

# define the revised problem (with additional constraints)
# define variables
eggs = LpVariable('Eggs', 0, None) # eggs >= 0
milk = LpVariable('Milk', 0, None) # milk >= 0
yogs = LpVariable('Yogurt', 0, None) # vitamins >=0
vegs = LpVariable('Vegetables', 0, None) # vegetables >= 0
chrs = LpVariable('Cheerios', 0, None) # cheerios >= 0

# define problem
prob_rev = LpProblem('problem', LpMinimize) # minimize cost

# define constraints
prob_rev += eggs * 70 + milk * 115 + yogt *  60 + vegs *  10 + chrs * 190 <= 5000 # milligrams of sodium
prob_rev += eggs * 70 + milk * 120 + yogt * 130 + vegs *  60 + chrs * 140 >= 2000 # calories
prob_rev += eggs *  6 + milk *   8 + yogt *  14 + vegs *   2 + chrs *   5 >=   50 # grams of protein
prob_rev += eggs *  1 + milk *   3 + yogt *   0 + vegs *   0 + chrs *   4 >=   20 # micrograms of Vitamin D
prob_rev += eggs * 30 + milk * 292 + yogt * 170 + vegs *   0 + chrs * 130 >= 1300 # milligrams of calcium
prob_rev += eggs *  1 + milk *   0 + yogt *   0 + vegs *   1 + chrs *  13 >=   18 # milligrams of iron
prob_rev += eggs * 70 + milk * 341 + yogt * 220 + vegs * 171 + chrs * 250 >= 4700 # milligrams of potassium
prob_rev += eggs *  1 + milk *   0 + yogt *   0 + vegs *   0 + chrs *   2 >=   11 # milligrams of zinc
prob_rev += eggs *  0 + milk *   0 + yogt *  11 + vegs *   0 + chrs *   1 <=   50 # grams of added sugar

# define objective function
prob_rev += cps_eggs * eggs + cps_milk * milk + cps_yog * yogt + cps_veg * vegs + cps_cheerios * chrs

# solve the problem
status = prob_rev.solve()
print(f'Diet Problem\nStatus: {LpStatus[status]}')

# print results
print(f'Servings of:')
for variable in prob_rev.variables():
    print(f'  - {variable.name} = {round(variable.varValue, 2)}')
print(f'Minimized Cost: {round(value(prob_rev.objective), 2)}')

#test test test
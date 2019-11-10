import pydrake.all
import numpy as py
import matplotlib.pyplot as plt


program=pydrake.solvers.mathematicalprogram.MathematicalProgram()
x=program.NewContinuousVariables(2)
print("Variables in for optimization are as below : ")
print(x)
program.AddConstraint(x[0]+x[1]==1)
program.AddConstraint(x[0]<=x[1])
program.AddCost(x[0]**2+x[1]**2)
result=pydrake.solvers.mathematicalprogram.Solve(program)
print("Cost function :", x[0]**2+x[1]**2)
print("Constraint 1 :",x[0]+x[1]==1)
print("Constraint 2:",x[0]-x[1]<=0)
print("Was it a success",result.is_success())
print("Minimuim X Value :",result.GetSolution())
print("For Minimal Value Optimal Cost is : ",result.get_optimal_cost)
print("Solver Used : ", result.get_solver_id().name())

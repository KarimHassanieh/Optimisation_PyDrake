import pydrake.all
import numpy as py
import matplotlib.pyplot as plt


program=pydrake.solvers.mathematicalprogram.MathematicalProgram()
x=program.NewContinuousVariables(2)
print("Variables in for optimization are as below : ")
print(x)

program.AddConstraint(x[0]>=0)
program.AddConstraint(x[1]>=0)
program.AddConstraint(2*x[0]+x[1]==100)
program.AddConstraint(100-4*x[0]==0)
program.AddCost(x[0]*x[1])
result=pydrake.solvers.mathematicalprogram.Solve(program)
print("Was it a success",result.is_success())
print("Minimuim X Value :",result.GetSolution())
print("Optimal Cost is  : ",result.get_optimal_cost())
print("Solver Used : ", result.get_solver_id().name())

#Sample code to run a MineralDistribution Problem in Form of Ising 
#against the Azure Quantum solver using this repo
#  
#You don't need to use this repo to get your results. 
#The meaning of the existense is to demostrate how to implement and use the Azure Quantum python SDK
#
#

import workspaceHelper
from problems.mineralWeights import mineralWeightsProblem
from azure.quantum.optimization import ParallelTempering
import time

#Call of the workspaceObject constructor. For details see workspaceHelper.py
workspaceObject = workspaceHelper.WorkspaceHelperInit(
    "subscriptionId",
     "rg_name",
      "quantum_workspace_name",
       "East US")
workspace = workspaceObject.getWorkspace()
workspace.login()

mineralWeightsSample = [1, 5, 9, 21, 35, 5, 3, 5, 10, 11]
mineralWeigtsProblemObject = mineralWeightsProblem(mineralWeightsSample)
mineralWeigtsProblemObject.createProblem()
problem = mineralWeigtsProblemObject.getProblem()

solver = ParallelTempering(workspace, timeout=100)


print("submitting problem...")
start = time.time()

result = solver.optimize(problem)

timeElapsed = time.time() - start
print(f'Result in {timeElapsed} seconds: ', result)


from typing import List
from azure.quantum.optimization import Problem, ProblemType, Term


#This class realizes one special Problem
#Problem:
#   Distribute a set of weights equally to two different containers
#   For more details see: https://docs.microsoft.com/en-us/learn/modules/solve-quantum-inspired-optimization-problems/

class mineralWeightsProblem(object):
    
    #Constructor to initialize the mineralWeightProblem object
    def __init__(self, mineralWeights):
        self.problem= None
        self.mineralWeights = mineralWeights
    #Method to create a Problem with Terms based on the input mineralWeight List
    #You need to call this method to work with this problem
    def createProblem(self):
        terms: List[Term] = []

        for i in range(len(self.mineralWeights)):
            for j in range(len(self.mineralWeights)):
                if i == j:
                    # Skip the terms where i == j as they form constant terms in an Ising problem and can be disregarded.
                    continue

                terms.append(
                    Term(
                        c = self.mineralWeights[i] * self.mineralWeights[j],
                        indices = [i, j]
                    )
             )
        self.problem = Problem(name="Balancing Problem", problem_type=ProblemType.ising, terms=terms)

    #Get-method for the problem
    def getProblem(self) -> Problem:
        if self.problem != None:

            return self.problem
        else:
            print("Problem is not initialized yet")
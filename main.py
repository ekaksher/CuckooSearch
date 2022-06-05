from cuckoo_main import CuckooProblem
from functions import FUNCTIONS

problem = CuckooProblem(function=FUNCTIONS['michalewicz'], nests=20,upper_boundary=4,lower_boundary=0,alpha=1,max_generations=30,p_a=0.1)
best_nest = problem.solve()
problem.replay()

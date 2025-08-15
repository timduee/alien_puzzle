from alien_death_game import run_simulation
from itertools import permutations
import numpy as np

if __name__ == "__main__":


    max_age = 10
    nr_reproductive_years = 3

    print('\n \n max_age:' + str(max_age) +', reproductive years:' + str(nr_reproductive_years))

    #gen all_combinations

    #number of combinations = 
    age_list = np.arange(max_age+1)

    w = 0
    for i in permutations(age_list, max_age+1):
        age_sequence = i

        aliens_won = run_simulation(age_sequence,max_age, nr_reproductive_years)

        if aliens_won:
            print('Aliens Win with sequence: ' + str(age_sequence))
            w = 1
            
            

    if w == 0:
        print('Not possible to win for Aliens \n \n')

import numpy as np

max_age = 3
nr_reproductive_years = 2




population = np.ones(max_age+1)
selected_ages = []

def new_cycle(population,min_reproductive_age):
    #population = np.asarray(population).copy()  # copy so we don’t modify original
    #population[1:][population[:-1] == 1] = 1
    #population[1:][population[:-1] == 0] = 0
    
    if np.any(population[min_reproductive_age:]) == True:
        reproduction_happens = True
    else:
        reproduction_happens = False

    population[1:] = population[:-1]

    if reproduction_happens:
        population[0] = 1
    else:
        population[0] = 0

    return population


def remove_age(age, population):
    population[age] = 0
    return population

# Play game




def run_simulation(age_sequence,max_age, nr_reproductive_years):
    
    min_reproductive_age = max_age - nr_reproductive_years + 1

    population = np.ones(max_age+1)

    for n in range(len(age_sequence)):

        population = remove_age(age_sequence[n], population)

        population = new_cycle(population, min_reproductive_age)

    if np.any(population) == False:
        return 1 # Aliens won
    else:
        return 0 # Aliens did not win

    
if __name__ == "__main__":
    while True:
        print("remaining population:")
        for i in range(max_age+1):
            if population[i] == True:
                print(i, " ", end='')
        no_age_selected = True
        print()
        print("Available ages:")
        for i in range(max_age+1):
            if selected_ages.__contains__(i) == False:
                print(i, " ", end='')
        print()
        while no_age_selected:
            selected_age = int(input("What age should be removed?"))
            if selected_ages.__contains__(selected_age) == False:
                selected_ages.append(selected_age)
                no_age_selected = False
            else:
                print("Age already selected!")
        population = remove_age(selected_age, population)

        
        population = new_cycle(population, min_reproductive_age)
        print("--------------------")
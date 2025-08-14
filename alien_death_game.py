import numpy as np

max_age = 3

population = np.ones(max_age+1)
selected_ages = []

def new_cycle(population):
    #population = np.asarray(population).copy()  # copy so we don’t modify original
    #population[1:][population[:-1] == 1] = 1
    #population[1:][population[:-1] == 0] = 0
    population[1:] = population[:-1]
    population[0] = 1
    return population


def remove_age(age, population):
    population[age] = 0
    return population

# Play game

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
    population = new_cycle(population)
    print("--------------------")

    
#HOMELYSM (Home Lighting System Manager)

# Creator Contact: pieroruesta2010@hotmail.com - https://github.com/Piero27
# Principal Collabority and creator of GUI: espartanlook777@gmail.com - https://github.com/jephersond

#This part of the repository implements the genetic algorithm that is the heart of the program.
import numpy as np

#Minimize objetive function

def objetive(x,y,z, P_a, P_b, P_c):
    return P_a*x + P_b*y + P_c*z 

#Principal restriction
def restriction(x,y,z, Lm_a, Lm_b, Lm_c, E):
    return abs(Lm_a*x + Lm_b*y + Lm_c*z - E)

def binaryToInt(num_array):
    sum = 0
    for i in range(len(num_array)):
        sum += num_array[i]*2**(len(num_array)-1-i)
    return sum

def mutate(individuals, prob, pool):
    for i in range(len(individuals)):
        mutate_individual=individuals[i]
        if np.random.random() < prob:
            mutation = np.random.choice(pool)
            mutate_individual = [mutation] + mutate_individual[1:]
        
        for j in range(1,len(mutate_individual)):
            if np.random.random() < prob:
                mutation = np.random.choice(pool)
                mutate_individual = mutate_individual[0:j] + [mutation] + mutate_individual[j+1:]
        individuals[i] = mutate_individual

def GeneticAlgorithm(generations, size_people, P_a, P_b, P_c, Lm_a, Lm_b, Lm_c, E):
    people = []; n=4

    for i in range(size_people):
        person = []
        person += np.array(np.random.choice([0,1],12)).tolist()
        people.append(person)
    
    for _ in range(generations):
        fitness_obj = []; fitness_r = []

        for person in people:
            value = [person[i:i + n] for i in range(0, 12, n)]
            fitness_obj += [objetive(binaryToInt(value[0]),binaryToInt(value[1]),binaryToInt(value[2]), P_a, P_b, P_c)]
            fitness_r += [restriction(binaryToInt(value[0]),binaryToInt(value[1]),binaryToInt(value[2]), Lm_a, Lm_b, Lm_c, E)]

        fitness_obj = np.array(fitness_obj)
        fitness_obj = fitness_obj.max() - fitness_obj + 1
        
        fitness_r = np.array(fitness_r)
        fitness_r = fitness_r.max() - fitness_r + 1
        
        fitness = fitness_obj * fitness_r
        fitness = fitness/fitness.sum()
        
        offspring = []

        for i in range(size_people//2):
            parents = np.random.choice(size_people, 2, p=fitness)
            cross_point = np.random.randint(11)
            offspring += [people[parents[0]][:cross_point] + people[parents[1]][cross_point:]]
            offspring += [people[parents[1]][:cross_point] + people[parents[0]][cross_point:]]

        people = offspring

        mutate(people,0.005,[0,1])

    fitness = fitness.tolist()
    optimal_solution = people[fitness.index(max(fitness))]
    solution_values = [optimal_solution[i:i + n] for i in range(0, 12, n)]
    solution = [binaryToInt(solution_values[0]), binaryToInt(solution_values[1]), binaryToInt(solution_values[2])]
    if restriction(solution[0], solution[1], solution[2], Lm_a, Lm_b, Lm_c, E) > 0:
        solution[0] = solution[0] + (restriction(solution[0], solution[1], solution[2], Lm_a, Lm_b, Lm_c, E) + (Lm_a - 1)) // Lm_a
        return solution
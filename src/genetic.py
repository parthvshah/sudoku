# Python3 program to create target string, starting from 
# random string using Genetic Algorithm 
  
import random 
  
# Number of individuals in each generation 
POPULATION_SIZE = 2000
  
# Valid genes 
GENES = '''123456789'''
TARGET = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
  
def notInRow(arr, row):  
    st = set()  
    count = 0
    for i in range(0, 9):
        if arr[row][i] in st:  
            count += 1
  
        if arr[row][i] != '.':  
            st.add(arr[row][i])  
      
    return count
  
def notInCol(arr, col):  
    st = set()  
    count = 0
    for i in range(0, 9):
        if arr[i][col] in st: 
            count += 1            
  
        if arr[i][col] != '.':
            st.add(arr[i][col])  
      
    return count
  
def notInBox(arr, startRow, startCol):  
    st = set()  
    count = 0
    for row in range(0, 3):  
        for col in range(0, 3):  
            curr = arr[row + startRow][col + startCol]  
  
            if curr in st:  
                count += 2
  
            if curr != '.':  
                st.add(curr)  
          
    return True
  
def isValid(arr, row, col):  
    return(notInRow(arr, row) + notInCol(arr, col) + notInBox(arr, row - row % 3, col - col % 3))  
  
def isValidConfig(arr, n):
    count = 0  
    for i in range(0, n):  
        for j in range(0, n):
            count += isValid(arr, i, j) 

    return count
  
class Individual(object): 
    ''' 
    Class representing individual in population 
    '''
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness() 
  
    @classmethod
    def mutated_genes(cls, self): 
        ''' 
        create random genes for mutation 
        '''
        global GENES 
        gene = random.choice(GENES) 
        return gene 
  
    @classmethod
    def create_gnome(cls, self): 
        ''' 
        create chromosome or string of genes
        
        '''
        global TARGET
        # TODO: Anchor the given places in target
        gnome_len = 81
        genome = []
        for i in range(len(TARGET)):
            if(TARGET[i]=='.'):
                genome.append(self.mutated_genes())
            else:
                genome.append(TARGET[i])
        # return [self.mutated_genes() for _ in range(gnome_len)] 
        return genome
  
    def mate(self, par2): 
        ''' 
        Perform mating and produce new offspring 
        '''
  
        # chromosome for offspring 
        child_chromosome = [] 
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     
  
            # random probability   
            prob = random.random() 
  
            # if prob is less than 0.45, insert gene 
            # from parent 1  
            if prob < 0.45: 
                child_chromosome.append(gp1) 
  
            # if prob is between 0.45 and 0.90, insert 
            # gene from parent 2 
            elif prob < 0.90: 
                child_chromosome.append(gp2) 
  
            # otherwise insert random gene(mutate),  
            # for maintaining diversity 
            else: 
                child_chromosome.append(self.mutated_genes()) 
  
        # create new Individual(offspring) using  
        # generated chromosome for offspring 
        return Individual(child_chromosome) 
  
    def cal_fitness(self):
        # global TARGET 
        # fitness = 0
        # for gs, gt in zip(self.chromosome, TARGET): 
        #     if gs != gt: fitness+= 1
        # return fitness
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(self.chromosome[(9*i)+j])
            board.append(row)

        return isValidConfig(board, 9)
  
# Driver code 
def main(): 
    global POPULATION_SIZE 
  
    #current generation 
    generation = 1
  
    found = False
    population = [] 
  
    # create initial population 
    for _ in range(POPULATION_SIZE): 
                gnome = Individual.create_gnome() 
                population.append(Individual(gnome)) 
  
    while not found: 
  
        # sort the population in increasing order of fitness score 
        population = sorted(population, key = lambda x:x.fitness) 
  
        # if the individual having lowest fitness score ie.  
        # 0 then we know that we have reached to the target 
        # and break the loop 
        if population[0].fitness <= 0: 
            found = True
            break
  
        # Otherwise generate new offsprings for new generation 
        new_generation = [] 
  
        # Perform Elitism, that mean 10% of fittest population 
        # goes to the next generation 
        s = int((10*POPULATION_SIZE)/100) 
        new_generation.extend(population[:s]) 
  
        # From 50% of fittest population, Individuals  
        # will mate to produce offspring 
        s = int((90*POPULATION_SIZE)/100) 
        for _ in range(s): 
            parent1 = random.choice(population[:50]) 
            parent2 = random.choice(population[:50]) 
            child = parent1.mate(parent2) 
            new_generation.append(child) 
  
        population = new_generation 
  
        print("Generation: {}\tString: {}\tFitness: {}". 
              format(generation, 
              "".join(population[0].chromosome), 
              population[0].fitness))
  
        generation += 1
  
      
    print("Generation: {}\tString: {}\tFitness: {}".
          format(generation, 
          "".join(population[0].chromosome), 
          population[0].fitness)) 
  
if __name__ == '__main__': 
    main() 
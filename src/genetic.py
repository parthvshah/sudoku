import random 
  
# Number of individuals in each generation 
POPULATION_SIZE = 100
MAX_GENERATION_COUNT = 100
  
# Valid genes 
GENES = '''123456789'''
TARGET = "9.42....7.1..........7.65.....8...9..2.9.4.6..4...2.....16.7..........3.3....57.2"
MASK = []
for i in range(len(TARGET)):
    if(TARGET[i]!="."):
        MASK.append(i)

def parser(arr):
    string_rep = "".join([str(e) for e in arr])
    temp = string_rep.replace('.','0')
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(int(temp[(9*i)+j]))
        board.append(row)
    return board

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr

def sanity(num):
    if(num in MASK):
        return 0
    else:
        return 1

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
    def mutated_genes(self): 
        ''' 
        create random genes for mutation 
        '''
        global GENES 
        gene = random.choice(GENES) 
        return gene 
    
    def swap_genes(self): 
        ''' 
        swap genes for mutation 
        '''
        global GENES
        prob = random.random()

        a = random.randint(0, 8)
        b = random.randint(0, 8)

        if(prob <= 0.1):
            if(sanity(a) and sanity(b)):
                self.chromosome = swap(self.chromosome, a, b)
        if(prob > 0.1 and prob <= 0.2):
             if(sanity(a+9) and sanity(b+9)):
                self.chromosome = swap(self.chromosome, a+9, b+9)
        if(prob > 0.2 and prob <= 0.3):
            if(sanity(a+18) and sanity(b+18)):
                self.chromosome = swap(self.chromosome, a+18, b+18) 
        if(prob > 0.3 and prob <= 0.4):
            if(sanity(a+27) and sanity(b+27)):
                self.chromosome = swap(self.chromosome, a+27, b+27) 
        if(prob > 0.4 and prob <= 0.5):
            if(sanity(a+36) and sanity(b+36)):
                self.chromosome = swap(self.chromosome, a+36, b+36) 
        if(prob > 0.5 and prob <= 0.6):
            if(sanity(a+45) and sanity(b+45)):
                self.chromosome = swap(self.chromosome, a+45, b+45) 
        if(prob > 0.6 and prob <= 0.7):
            if(sanity(a+54) and sanity(b+54)):
                self.chromosome = swap(self.chromosome, a+54, b+54) 
        if(prob > 0.7 and prob <= 0.8):
            if(sanity(a+63) and sanity(b+63)):
                self.chromosome = swap(self.chromosome, a+63, b+63) 
        if(prob > 0.8 and prob <= 0.9):
            if(sanity(a+72) and sanity(b+72)):
                self.chromosome = swap(self.chromosome, a+72, b+72) 

        return self.chromosome
    
    @classmethod
    def create_gnome(self):
        # Must return an array of 81
        genome = []
        genes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for i in range(9):
            random.shuffle(genes)
            for j in genes:
                genome.append(j)
        
        # Now we mask it
        targetList = list(TARGET)
        for j in range(81):
            if(targetList[j] != "."):
                genome[j] = int(targetList[j])

        return genome

  
    def mate(self, par2): 
        ''' 
        Perform mating and produce new offspring 
        '''

        for i in range(1):
            self.swap_genes()
            par2.swap_genes()
        
        if(self.cal_fitness() > par2.cal_fitness()): 
            return Individual(self.chromosome)
        else:
            return Individual(par2.chromosome)
  
    def cal_fitness(self):
        return isValidConfig(parser(self.chromosome), 9)
  
# Driver code 
def main(): 
    global POPULATION_SIZE 
  
    #current generation 
    generation = 1
  
    found = False
    population = [] 
  
    # create initial population 
    for _ in range(POPULATION_SIZE): 
                # mask = Individual.create_mask()
                gnome = Individual.create_gnome()
                population.append(Individual(gnome)) 
  
    while not found: 
  
        # sort the population in increasing order of fitness score 
        population = sorted(population, key = lambda x:x.fitness) 
  
        # if the individual having lowest fitness score ie.  
        # 0 then we know that we have reached to the target 
        # and break the loop 
        if population[0].fitness == 81: 
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
  
        print("Gen: {}\tSol: {}\tMin Fit: {}\tMax Fit: {}". 
              format(generation, 
              "".join([str(e) for e in population[0].chromosome]), 
              population[0].fitness,
              population[POPULATION_SIZE-1].fitness))

        if(generation==MAX_GENERATION_COUNT):
            break
        generation += 1
  
      
    print("Gen: {}\tSol: {}\tMin Fit: {}".
          format(generation, 
          "".join([str(e) for e in population[0].chromosome]), 
          population[0].fitness)) 
  
if __name__ == '__main__': 
    main() 
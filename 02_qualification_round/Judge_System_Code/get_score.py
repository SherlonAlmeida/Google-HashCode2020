###################################
#Author: Sherlon Almeida da Silva #
#Email: sherlon@usp.br            #
#University of Sao Paulo - Brazil #
###################################

import sys

ADD_LIB_and_BOOKS = []
BOOKS_SCANNED = {}

"""Updates library registrations and book scans daily. That is, it decreases 1 every day"""
def update_scan_situation(queue, size_queue, last_lib_index, n_L):
    can_i_sign_up_a_new_library = False  #Flag to control the registration of new libraries (Pipeline)
    for p in range(size_queue):          #Cycles through all processes in the queue
        """Description of the data below
           queue[p][0] #Dias de cadastro restantes
           queue[p][1] #Numero de livros que faltam ser escaneados
           queue[p][2] #Numero de livros que podem ser escaneados por dia
           queue[p][3] #Indice da biblioteca"""
        
        if queue[p][0] != 0:              #Tests if the current library is still in the registration process, if yes
            queue[p][0] -= 1              #Decreases one day from current registration
        else:                             #Only allows the scanning of books after registering the library
            if queue[p][1] > 0:               #Tests whether the current library still has books to be scanned, if so
                if queue[p][1] >= queue[p][2]:    #Tests whether they can be removed from N in N books, if yes
                    for i in range(queue[p][1], queue[p][1] - queue[p][2], -1):  #Scrolls through the books being scanned
                        #print("SCAN BOOK " + str(ADD_LIB_and_BOOKS[p][-i]) + " from LIB " + str(queue[p][3]))
                        book_index = ADD_LIB_and_BOOKS[p][-i]    #Gets the index of the scanned book
                        BOOKS_SCANNED[book_index] = 1            #Place the book in the list of scanned books
                    queue[p][1] -= queue[p][2]    #Reduces N books per day, N being the number of books that can be sent per day by this library
                else:                             #otherwise
                    for i in range(queue[p][1], queue[p][1] - queue[p][1], -1):  #Scrolls through the books being scanned
                        #print("SCAN BOOK " + str(ADD_LIB_and_BOOKS[p][-i]) + " from LIB " + str(queue[p][3]))
                        book_index = ADD_LIB_and_BOOKS[p][-i]    #Gets the index of the scanned book
                        BOOKS_SCANNED[book_index] = 1            #Place the book in the list of scanned books
                    queue[p][1] -= queue[p][1]    #Reduces the rest of the books, resulting in 0 (Not to give a negative result)
    
    if (queue[last_lib_index][0] == 0) and (last_lib_index != n_L-1): #If the registration of the last library has ended and there are others to be inserted, then
        can_i_sign_up_a_new_library = True        #Allows the registration of the next library
        
    return queue, can_i_sign_up_a_new_library

def get_score(n_L, B_scores, Libraries, D, filename):
    queue = []      #Create a queue to add registered libraries and scanned books daily
    size_queue = 0  #The queue starts empty
    can_i_sign_up_a_new_library = False  #Flag to control the registration of new libraries (Pipeline)
    last_lib_index = 0 #Go through the libraries that will be registered over the days
    
    #Iterate the days until the last day arrives
    for day in range(D):
        if day == 0: #If it is the first day (That is, the queue is empty)
            curr_lib_index = ADD_LIB_and_BOOKS[last_lib_index][0]                #Get the current library index in the "Libraries" variable
            number_of_books = Libraries[ADD_LIB_and_BOOKS[last_lib_index][0]][0] #Gets the value [number_of_books] from the current library
            signup_days = Libraries[ADD_LIB_and_BOOKS[last_lib_index][0]][1]     #Gets the value [signup_days] from the current library
            ships_per_day = Libraries[ADD_LIB_and_BOOKS[last_lib_index][0]][2]   #Gets the value [ships_per_day] from the current library
            number_of_books_scanned = ADD_LIB_and_BOOKS[last_lib_index][1]       #Gets the number of books to be scanned
            
            """Adds [Registration Days, Books to be scanned, Total number of daily deliveries, index] from the current library"""
            queue.append([signup_days, number_of_books_scanned, ships_per_day, curr_lib_index])              #Adds the current library to the queue
            size_queue += 1                                                                                  #Adds one more to the queue size
            queue, can_i_sign_up_a_new_library = update_scan_situation(queue,size_queue,last_lib_index,n_L)  #Updates the queue for the first time
        else:
            if can_i_sign_up_a_new_library: #If I can add a new library, then
                last_lib_index += 1                                                  #Atualiza o indice para a nova biblioteca
                curr_lib_index = ADD_LIB_and_BOOKS[last_lib_index][0]                #Get the current library index in the "Libraries" variable
                number_of_books = Libraries[ADD_LIB_and_BOOKS[last_lib_index][0]][0] #Gets the value [number_of_books] from the current library
                signup_days = Libraries[ADD_LIB_and_BOOKS[last_lib_index][0]][1]     #Gets the value [signup_days] from the current library
                ships_per_day = Libraries[ADD_LIB_and_BOOKS[last_lib_index][0]][2]   #Gets the value [ships_per_day] from the current library
                number_of_books_scanned = ADD_LIB_and_BOOKS[last_lib_index][1]       #Gets the number of books to be scanned

                """Adds [Registration Days, Books to be scanned, Total number of daily deliveries, index] from the current library"""
                queue.append([signup_days, number_of_books_scanned, ships_per_day, curr_lib_index])              #Adds the current library to the queue
                size_queue += 1                                                                                  #Adds one more to the queue size
                queue, can_i_sign_up_a_new_library = update_scan_situation(queue,size_queue,last_lib_index,n_L)  #Updates the queue
            else: #Agora, se eu nao posso adicionar uma nova biblioteca, entao
                queue, can_i_sign_up_a_new_library = update_scan_situation(queue,size_queue,last_lib_index,n_L)  #Updates the queue
        #print(day, queue, can_i_sign_up_a_new_library)
    
    score = 0
    for book in BOOKS_SCANNED:
        score += B_scores[book]
    print("Score: ", score)
    """Create a file to save the partial results and after obtaining the total sum"""
    best_score = open(filename, "a")
    best_score.write(str(score) + "\n")
    best_score.close()

"""Load the dataset file"""
def load_dataset(filename):
    size_dataset = 0
    with open(filename, 'r') as arq:
        dataset = arq.readlines()
        size_dataset = len(dataset)
        for i in range(size_dataset):
            dataset[i] = list(map(int, dataset[i].rstrip("\n").split()))
    B,L,D = dataset[0]
    B_scores = dataset[1]
    Libraries = []
    for i in range(2, size_dataset-1, 2):
        curr_data = []
        for j in dataset[i]:
            curr_data.append(j)
        for j in dataset[i+1]:
            curr_data.append(j)
        Libraries.append(curr_data)
    return B,L,D,B_scores,Libraries

"""Load your results file"""
def load_your_result(filename):
    size_result = 0
    with open(filename, 'r') as arq:
        result = arq.readlines()
        size_result = len(result)
        for i in range(size_result):
            result[i] = list(map(int, result[i].rstrip("\n").split()))
    total_libraries_signup = result[0][0]
    for i in range(1, size_result-1, 2):
        curr_data = []
        for j in result[i]:
            curr_data.append(j)
        for j in result[i+1]:
            curr_data.append(j)
        ADD_LIB_and_BOOKS.append(curr_data)
    return total_libraries_signup

"""Main Function"""
def main():
    if len(sys.argv) < 4:
        print("Type it: python3 " + sys.argv[0] + " " + "<dataset.in> <your_result.out> <this_is_a_name_to_the_results_file_output.out>")
        sys.exit()
    
    B,L,D,B_scores,Libraries = load_dataset(sys.argv[1])
    total_libraries_signup = load_your_result(sys.argv[2])
    
    get_score(total_libraries_signup, B_scores, Libraries, D, sys.argv[3])

main() #Call the main function

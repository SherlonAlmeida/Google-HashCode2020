###################################
#Author: Sherlon Almeida da Silva #
#Email: sherlon@usp.br            #
#Author: Isadora Garcia Ferrao    #
#Email: isadoraferrao@usp.br      #
#University of Sao Paulo - Brazil #
###################################

ADD_LIB_and_BOOKS = []
BOOKS_REPEATED = []

"""Print the output in stdout"""
def print_results (total_libraries_signup):
    print(total_libraries_signup)
    for i in range(total_libraries_signup):
        ID_library = ADD_LIB_and_BOOKS[i][0]
        n_books = ADD_LIB_and_BOOKS[i][1]
        print( str(ID_library) + " " + str(n_books) )
        for j in range(2, n_books+2):
            print(ADD_LIB_and_BOOKS[i][j], end=" ")
        print("")

"""Scroll through the current List, checking if the books have already been scanned, if so, lower your priority by putting to the end of the list"""
def repetition_checker(v, L_signup, B):
    index_lib = v[0]  #Index of this library
    n_B = v[1]        #Number of books
    global BOOKS_REPEATED
    not_repeated_books = []
    repeated_books = []
    
    if L_signup == 0: #If there is a library in the queue (The first one), then add its values in the BOOKS_REPEATED
        BOOKS_REPEATED = [0 for i in range(B)]      #Initialize this variable to identify books repeated
        for i in range(2, n_B+2):
            index = v[i]                     #Get the current book index
            BOOKS_REPEATED[index] = 1        #Consider this book scanned
            not_repeated_books.append(index) #Add this book in the "Not Repeated Books" list
    else:
        for i in range(2, n_B+2):
            index = v[i]                          #Get the current book index
            if (BOOKS_REPEATED[index] != 1):      #Se esse livro nao foi escaneado, entao
                not_repeated_books.append(index)  #Add this book in the "Not Repeated Books" list
                BOOKS_REPEATED[index] = 1         #Consider this book scanned
            else:                                 #Otherwise
                repeated_books.append(index)      #Consider this book repeated
    
    not_repeated_books.extend(repeated_books)     #Add the repeated book in the final of the list
    
    #Armazena os valores atuais no formato do ADD_LIB_and_BOOKS
    not_repeated_books.insert(0, index_lib)         #O index da Library
    not_repeated_books.insert(1, n_B)           #A quantidade de livros atual
    return not_repeated_books

"""Scroll through the current list by ordering the best result first"""
def best_score_order(v, B_scores, Libraries, n_B, index_lib):
    score_order = []
    for i in range(3, n_B+3):
        index = v[i]
        score = B_scores[index]
        score_order.append([index, score])
    ordered = sorted(score_order, key = lambda x: x[1], reverse=True) #Sort by highest score first
    new_order = []
    for i in range(n_B):
        new_order.append(ordered[i][0])
    #Stores current values in ADD_LIB_and_BOOKS format
    new_order.insert(0, index_lib)         #The Library index
    new_order.insert(1, n_B)               #The current book quantity
    return new_order

def signup_libraries(indexes, Libraries, B_scores, B, L, D, L_signup):
    i = 0
    size_indexes = len(indexes)
    while (i < size_indexes): #Scroll through the libraries in the order I want to insert
        n_B = Libraries[indexes[i]][0]  #Total of Books in this Library
        x = Libraries[indexes[i]][1]    #Total days to signup
        d = Libraries[indexes[i]][2]    #Total ships per day
        
        #Get the list ordered by best score "Score Order"
        new_order = best_score_order(Libraries[indexes[i]], B_scores, Libraries, n_B, indexes[i])
        
        #Get the list reorganized, throwing the scanned books to the end (Lowering the priority)
        new_order = repetition_checker(new_order, L_signup, B)
        
        ADD_LIB_and_BOOKS.append(new_order)
        i += 1
        L_signup += 1
    return L_signup

"""Scroll through the dictionary backwards to increase the number of scanned books"""
def set_order(B, L, D, B_scores, Libraries, signup_order, order):
    L_signup = 0 #Stores the number of registered Libraries
    
    if order == "crescent": #From smallest to largest
        for key in sorted(signup_order.keys()):
            L_signup = signup_libraries(signup_order[key], Libraries, B_scores, B, L, D, L_signup)
    
    elif order == "decrescent": #From largest to smallest
        for key in reversed(sorted(signup_order.keys())):
            L_signup = signup_libraries(signup_order[key], Libraries, B_scores, B, L, D, L_signup)
        
    return L_signup

"""Main Function"""
def main():
    B,L,D = list(map(int, input().split()))     #Number of: Books, Libraries, Days in total
    B_scores = list(map(int, input().split()))  #Scores of each book
    Libraries = []                              #Save the data
    signup_order = {}                           #Inverse hash to keep indexes (Key is the sum to maximize the "chosen variable", and Value are the indexes)
    order = ""                                  #To define the order to organize the data
    
    #Load the dataset
    for i in range(L):
        number_of_books, signup_days, ships_per_day = list(map(int, input().split()))
        set_of_books = list(map(int, input().split()))
        Libraries.append([number_of_books, signup_days, ships_per_day])
        for j in range(number_of_books):
            Libraries[i].append(set_of_books[j])
        
        #Populate a inverse hash to identify the order to [number_of_books, signup_days, ships_per_day] the Libraries
        #index = number_of_books; order = "decrescent" #The order must be DECRESCENT, that is, from the largest to the smallest (Larger number of books is better)
        index = signup_days; order = "crescent"        #The order must be CRESCENT, that is, from the smallest to the largest (Smaller signup days is better)
        #index = ships_per_day; order = "decrescent"   #The order must be DECRESCENT, that is, from largest to smallest (Higher number of ships per day is better)
        if index in signup_order:
            signup_order[index].append(i)
        else:
            signup_order[index] = [i]
    
    total_libraries_signup = set_order(B,L,D,B_scores,Libraries, signup_order, order)
    print_results (total_libraries_signup)
            
main() #Call the main function

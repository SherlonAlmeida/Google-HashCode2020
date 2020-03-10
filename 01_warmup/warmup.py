###################################
#Author: Sherlon Almeida da Silva #
#Author: Isadora Garcia Ferrao    #
#University of Sao Paulo - Brazil #
###################################

"""The results found are shown"""
def print_result(size, order):
    print("%d"%(size))
    for i in range(size, 0, -1):
        print(order[i-1], end=" ")

"""The algorithm looks for types of pizza to order"""
def sum(pizzas, M, N):
    best_score = -1; best_size = 0; best_order = []
    for k in range(1, N+1):
        score = 0; size = 0; order = []
        for p in range(k, N+1):
            if ((score + pizzas[N-p]) <= M):
                order.append(N-p)
                score += pizzas[N-p]
                size += 1
        if score >= best_score:
            best_score = score
            best_size = size
            best_order = order
        if best_score == M: break
    #print("Score: ", best_score, "Total: ", M, "Result: ", M-best_score)
    print_result(best_size, best_order)

"""Main Function"""
def main():
    M,N = list(map(int, input().split()))
    pizzas = list(map(int, input().split()))
    sum(pizzas, M, N)
            
main() #Call the main function

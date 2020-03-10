###################################
#Author: Sherlon Almeida da Silva #
#Email: sherlon@usp.br            #
#University of Sao Paulo - Brazil #
###################################

import sys

"""Load your results file"""
def load_your_result(filename):
    best_score = 0
    with open(filename, 'r') as arq:
        result = arq.readlines()
        for i in range(len(result)):
            result[i] = list(map(int, result[i].rstrip("\n").split()))[0]
            best_score += result[i]
    return best_score

"""Main Function"""
def main():
    if len(sys.argv) < 2:
        print("Type it: python3 " + sys.argv[0] + " " + "<<this_is_a_name_to_the_results_file_output.out>")
        sys.exit()
    
    best_score = load_your_result(sys.argv[1])
    print("Total Score: " + str(best_score))

main() #Call the main function

###############################
##   GOOGLE HASH CODE 2020   ##
##        Auto Checker       ##
###############################
Dataset A ... Score:  21
Dataset B ... Score:  5822900
Dataset C ... Score:  5467966
Dataset D ... Score:  4109300
Dataset E ... Score:  4215235
Dataset F ... Score:  2430950
Total Score: 22046372

My solution:
    -I order the books in each library by highest score first.
    -I implemented a function to get the duplicate books and put the duplicates at the end of the list, that is, with lower priority.
    -Defined a variable called "order" to define the order of organizing the data, either CRESCENT, or DECRESCENT, since:
        number_of_books:
            The order must be DECRESCENT, that is, from the largest to the smallest (Larger number of books is better)
                Dataset A ... Score:  21
                Dataset B ... Score:  4126100
                Dataset C ... Score:  1178242
                Dataset D ... Score:  4815395
                Dataset E ... Score:  1121672
                Dataset F ... Score:  818292
                Total Score: 12059722
        signup_days: (BEST RESULT)
            The order must be CRESCENT, that is, from the smallest to the largest (Smaller signup days is better)
                Dataset A ... Score:  21
                Dataset B ... Score:  5822900
                Dataset C ... Score:  5467966
                Dataset D ... Score:  4109300
                Dataset E ... Score:  4215235
                Dataset F ... Score:  2430950
                Total Score: 22046372
        ships_per_day:
            The order must be DECRESCENT, that is, from largest to smallest (Higher number of ships per day is better)
                Dataset A ... Score:  21
                Dataset B ... Score:  4126100
                Dataset C ... Score:  949503
                Dataset D ... Score:  4109300
                Dataset E ... Score:  1268094
                Dataset F ... Score:  386634
                Total Score: 10839652

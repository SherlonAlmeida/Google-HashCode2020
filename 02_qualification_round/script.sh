###################################
#Author: Sherlon Almeida da Silva #
#University of Sao Paulo - Brazil #
#Email: sherlon@usp.br            #
###################################

PATH_DATASET="Datasets"
PATH_RESULTS="Output"
PATH_JUDGE="Judge_System_Code"
YOUR_CODE="solution.py"
FILENAME="best_score.out"

printf "###############################\n"
printf "##   GOOGLE HASH CODE 2020   ##\n"
printf "##        Auto Checker       ##\n"
printf "###############################\n"

if [ -e $FILENAME ]; then
    rm $FILENAME
fi

if [ -d $PATH_RESULTS ]; then
    rm -r $PATH_RESULTS
    mkdir $PATH_RESULTS
else
    mkdir $PATH_RESULTS
fi

printf "Dataset A ... "
python3 $YOUR_CODE < $PATH_DATASET/a_example.txt &> $PATH_RESULTS/a.out
python3 $PATH_JUDGE/get_score.py  $PATH_DATASET/a_example.txt $PATH_RESULTS/a.out $FILENAME

printf "Dataset B ... "
python3 $YOUR_CODE < $PATH_DATASET/b_read_on.txt &> $PATH_RESULTS/b.out
python3 $PATH_JUDGE/get_score.py  $PATH_DATASET/b_read_on.txt $PATH_RESULTS/b.out $FILENAME

printf "Dataset C ... "
python3 $YOUR_CODE < $PATH_DATASET/c_incunabula.txt &> $PATH_RESULTS/c.out
python3 $PATH_JUDGE/get_score.py  $PATH_DATASET/c_incunabula.txt $PATH_RESULTS/c.out $FILENAME

printf "Dataset D ... "
python3 $YOUR_CODE < $PATH_DATASET/d_tough_choices.txt &> $PATH_RESULTS/d.out
python3 $PATH_JUDGE/get_score.py  $PATH_DATASET/d_tough_choices.txt $PATH_RESULTS/d.out $FILENAME

printf "Dataset E ... "
python3 $YOUR_CODE < $PATH_DATASET/e_so_many_books.txt &> $PATH_RESULTS/e.out
python3 $PATH_JUDGE/get_score.py  $PATH_DATASET/e_so_many_books.txt $PATH_RESULTS/e.out $FILENAME

printf "Dataset F ... "
python3 $YOUR_CODE < $PATH_DATASET/f_libraries_of_the_world.txt &> $PATH_RESULTS/f.out
python3 $PATH_JUDGE/get_score.py  $PATH_DATASET/f_libraries_of_the_world.txt $PATH_RESULTS/f.out $FILENAME

python3 $PATH_JUDGE/get_sum.py $FILENAME
rm $FILENAME



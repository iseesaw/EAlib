#####################################
# @Date    : 2019-09-24 16:29:54
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# The script is used to run the top3 best algorithms on 10 tsps.
#####################################

# install the lib
python setup.py install

# define the functions
# bash run.sh basic basic basic
selection=$1
mutation=$2
crossover=$3

# parameters
unit_nums=(10 20 50 100)
#max_gens=(5000 10000 20000)

# filenames
filenames=(eil51 eil76 eil101 st70 kroA100 kroC100 kroD100 lin105 pcb442 pr2392)

for filename in ${filenames[@]};
do
    for unit_num in ${unit_nums[@]};
    do
        python test/EAlibTest.py \
              -filename=tsp/${filename}.tsp \
               --selection=$selection \
               --mutation=$mutation \
               --crossover=$crossover \
               --unit_num=$unit_num \
               --max_gen=20000
    done
done


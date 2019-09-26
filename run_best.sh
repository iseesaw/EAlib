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
selection=tournament
mutation=inversion
crossover=pmx

# parameters
unit_num=50
max_gen=10000

# filenames
filenames=(eil51 eil76 eil101 st70 kroA100 kroC100 kroD100 lin105 pcb442 pr2392)

for ((i=1; i<=2; i ++));
do
    for filename in ${filenames[@]};
    do
        python test/EAlibTest.py \
              -filename=tsp/${filename}.tsp \
               --selection=$selection \
               --mutation=$mutation \
               --crossover=$crossover \
               --unit_num=$unit_num \
               --max_gen=$max_gen
    done
done


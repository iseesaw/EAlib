#####################################
# @Date    : 2019-09-24 16:29:54
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# The script is used to run the top3 best algorithms on 10 tsps.
#####################################

# install the lib
#python setup.py install

# parameters
unit_nums=(10 20 50 100)
max_gens=(5000 10000 20000)

# filenames
filenames=(eil51 eil76 eil101 st70 kroA100 kroC100 kroD100 lin105 pcb442 pr2392)

# functions
selections=(rank tournament fitnetss)
mutations=(insert scramble inversion swap)
crossovers=(order cycle edge)

for s in ${selections[@]};
do
    for m in ${mutations[@]};
    do
        for c in ${crossovers[@]};
        do
            python test/EAlibTest.py \
                   -filename=tsp/eil51.tsp \
                   --selection=$s \
                   --mutation=$m \
                   --crossover=$c \
                   --unit_num=50 \
                   --max_gen=100
        done
    done
done


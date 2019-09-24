#####################################
# @Date    : 2019-09-24 16:29:54
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# The script is used to find the top3 best algorithms by Grid Search.
#####################################

# install
python setup.py install

# functions
selections=(rank tournament fitnetss)
mutations=(insert scramble inversion swap)
crossovers=(order cycle edge)

filenames=(eil51 eil76 eil101 st70 kroA100 kroC100 kroD100 lin105 pcb442 pr2392)

for file in ${filenames[@]}:
  do
  for s in ${selections[@]};
  do
      for m in ${mutations[@]};
      do
          for c in ${crossovers[@]};
          do
              python test/EAlibTest.py \
                     -filename=tsp/${file}.tsp \
                     --selection=$s \
                     --mutation=$m \
                     --crossover=$c \
                     --unit_num=50 \
                     --max_gen=1000
          done
      done
  done
done

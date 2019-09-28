## EAlib

Members：

| Name           | Students numbers | email addresse            |
| -------------- | ---------------- | ------------------------- |
| Zhang Kaiyan   | 1160300607       | kyzhang@ir.hit.edu.cn     |
| Wu Jiaming     | 1160300612       | 1160300612@stu.hit.edu.cn |
| Li Yangfan     | 1160300627       | 1440241051@qq.com         |
| Wang Zhongyuan | 1160300629       | zywang@ir.hit.edu.cn      |
| Sun Runxin     | 1160300911       | 448393580@qq.com          |

Video Here:
- [OneDriver](https://1drv.ms/v/s!Al3M6DKQN2ZdmVhEGCHBqPbyBcHo?e=kHUzvY) 
- [YouTube](https://youtu.be/izNkwlp6rEs)

### **Get Started**

> numpy = 1.16.4 is required.

**Just One Line Code**

```bash
$ python setup.py install && python test/EAlibTest.py -filename=tsp/eil51.tsp && python test/visual.py -filename=eil51.tsp
```

----------

**You can also** clone the code from **GitHub**, and run the commands as follows in terminal:

```bash
$ git clone https://github.com/iseesaw/EAlib
$ cd EAlib
$ python setup.py install
```

Then you can run our best  **Evolutionary Computation** algorithm on the tsp problems under the `tsp` directory:

```bash
$ python test/EAlibTest.py -filename=tsp/eil51.tsp
```

The results are saved in `ouput/ei151.tsp.json`.

You can visual the evolutionary process:

```bash
$ python test/visual.py -filename=ei151.tsp
```

### Tutorials

- **Usage**

  You can use our python library, EAlib:

  ```python
  from EAlib.ea import Naive_Ea
  Naive_Ea(filename="tsp/att48.tsp")
  ```

  

- **Run Scripts**

  - **Grid Search**, which is used to find the best topk combinations.

    ```bash
    bash search.sh
    ```

    This script is running `4 x 4 x 3 = 48` algorithms on nine datasets(Not including pr2392).

    You can get the results in `output/grid_search`

  - **Run top3 best algorithms** 10 datasets with 4 population sizes.

    ```bash
    bash run.sh selection_func crossover_func mutation_func
    ```

    You can find the functions' name in Mapping parameters to functions.

    And the results are save in `output/{filename}.{selection_func}.{crossover_func}.{mutation_func}.{unit_num}.{max_gen}.json`.

    At the end, you can get `4 x 10 = 40` results on the algorithm.
    
  - **Visualization**

    ```bash
    python test\visual.py -filename=att48.tsp.basic_selection.basic_crossover.basic_mutation.50.100
    ```

    | parameter | type  | default                             | usage                   |
    | --------- | ----- | ----------------------------------- | ----------------------- |
    | filename  | str   | None                                | output result file name |
    | tsp       | str   | None<br>(default get from filename) | tsp problem file        |
    | pause     | float | 0.5                                 | time to pause           |

  - **Run Best algorithm on ten dataset for N iterations **

    ```bash
    bash run_best.sh
    ```


### Appendix

Here comes the information about `EAlibTest.py`.

- **Arguments**

| parameter     | type  | default       | help                                                     |
| ------------- | ----- | ------------- | -------------------------------------------------------- |
| -filename     | str   | tsp/att48.tsp | tsp problem file (under the tsp dir)                     |
| --selection   | str   | basic         | [Optional] <br>basic, elitism, tournament, fitnetss      |
| --crossover   | str   | basic         | [Optional] <br/>basic, order, cycle, edge                |
| --mutation    | str   | basic         | [Optional] <br/>basic, insert, scramble, inversion, swap |
| --unit_num    | int   | 20            | unit num of the population                               |
| --max_gen     | int   | 100           | max generations                                          |
| --prob_c      | float | 0.5           | probability of crossover                                 |
| --prob_m      | float | 0.3           | probability of mutation                                  |
| --print_every | int   | 50            | how many times to print the best one                     |
| --output_dir  | str   | output        | output the best one record                               |

- **Mapping parameter to functions**

  ```python
      selections = {
          "basic": basic_selection,
          "rank": rank_based,
          "tournament": tournament_selection,
          "fitnetss": fitnetss_proporitional
      }
  
      mutations = {
          "basic": basic_mutation,
          "insert": insert_mutation,
          "scramble": scramble_mutation,
          "inversion": inversion_mutation,
          "swap": swap_mutation
      }
  
      crossovers = {
          "basic": basic_crossover,
          "order": Order_Crossover,
          "cycle": Cy_cle_Crossover,
          "edge": Edge_Recombination,
          "pmx": PMX_Crossover
      }
  
  ```

  

### Files Structure

```python
EAlib
|-- EAlib # Our Core Algorithms
|   |-- __init__.py
|   |-- basic # basic classes
|   |   |-- __init__.py
|   |   |-- individual.py
|   |   |-- population.py
|   |   `-- tspproblem.py
|   |-- ea # main function
|   |   |-- __init__.py
|   |   `-- naive_ea.py
|   |-- log # log
|   |   |-- __init__.py 
|   |   |-- log.conf
|   |   `-- log.py
|   |-- operators
|   |   |-- __init__.py
|   |   |-- crossover.py
|   |   |-- mutation.py
|   |   `-- selection.py
|   `-- utils
|       |-- __init__.py
|       `-- dataloader.py
|-- LICENSE
|-- README.md
|-- log.log # running log
|-- history.log # more log to show in the history
|-- output # output result files
|   |-- best_algorithm.json  #### the log for the best algorithm ###
|   |-- eil51.tsp
|   |-- eil51.tsp.json # output file while you run the first command above
|   `-- top5_algorithms.json ### the log for results of 3（5） algorithms ###
|-- run_best.sh  # script
|-- run_grid_search.sh # script 
|-- run_top3.sh # script
|-- setup.py
|-- test  # experiments
|   |-- EAlibTest.py
|   |-- TSPProblemTest.py
|   |-- analyze.py
|   |-- dataloader.log
|   |-- dataloadertest.py
|   `-- visual.py
`-- tsp # tsp problems
```

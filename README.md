## EAlib

- **Install**

  ```bash
  python setup.py install
  ```

  

- **Usage**

  ```python
  from EAlib.ea import Naive_Ea
  
  Naive_Ea(filename="tsp/att48.tsp")
  ```
  
  
  
- **Run Test**

  - **Command**
  
  ```bash
  $ ls
  EAlib ref test tsp README.md setup.py
  
  $ python test/EAlibTest.py --filename=tsp/att48.tsp
  2019-09-22 14:21:37,699 - EAlib - INFO - Welcome to Naive Evolution Algorithm System.
  Load TSP Problem tsp/att48.tsp Successfully!
  2019-09-22 14:21:37,711 - EAlib - INFO - Selection: basic_selection
  2019-09-22 14:21:37,711 - EAlib - INFO - Crossover: basic_crossover
  2019-09-22 14:21:37,711 - EAlib - INFO - Mutation: basic_mutation
  2019-09-22 14:21:37,843 - EAlib - INFO - 49th
  Fitness 110371.2565276248
  Gene [26, 36, 27, 19, 22, 7, 13, 32, 0, 37, 39, 4, 33, 30, 35, 25, 23, 11, 42, 6, 17, 9, 43, 16, 45, 21, 10, 1, 41, 34, 3, 40, 2, 31, 12, 8, 15, 38, 47, 28, 44, 46, 20, 14, 24, 29, 18, 5]
  2019-09-22 14:21:37,973 - EAlib - INFO - 99th
  Fitness 101795.57594933052
  Gene [26, 36, 27, 42, 29, 46, 13, 32, 0, 37, 39, 4, 20, 41, 2, 22, 23, 11, 19, 6, 17, 44, 31, 16, 45, 21, 10, 1, 25, 34, 3, 40, 35, 43, 14, 30, 15, 38, 47, 28, 9, 24, 33, 12, 7, 8, 18, 5]
  2019-09-22 14:21:37,975 - EAlib - INFO - Save results to output
  2019-09-22 14:21:37,991 - EAlib - INFO - That' all.
  ```
  
  - **Parameters**
  
  | parameter   | type  | default       | help                                                     |
  | ----------- | ----- | ------------- | -------------------------------------------------------- |
  | filename    | str   | tsp/att48.tsp | tsp problem file (under the tsp dir)                     |
  | selection   | str   | basic         | [Optional] <br>basic, elitism, tournament, fitnetss      |
  | crossover   | str   | basic         | [Optional] <br/>basic, order, cycle, edge                |
  | mutation    | str   | basic         | [Optional] <br/>basic, insert, scramble, inversion, swap |
  | unit_num    | int   | 20            | unit num of the population                               |
  | max_gen     | int   | 100           | max generations                                          |
  | prob_c      | float | 0.5           | probability of crossover                                 |
  | prob_m      | float | 0.3           | probability of mutation                                  |
  | print_every | int   | 50            | how many times to print the best one                     |
  | output_dir  | str   | output        | output the best one record                               |
  
  
  
- **Development**

  - *operators*

    > You can just write your function in crossover/mutation/selection.py.  
    >
    > And then run the ea/naive_ea.py file to test  your code as follows:
    >
    > step1, **import** your method in the head (About **line 14-16**)
    >
    > step2, change parameters at **line 24-26**
    >
    > step3,  goto the **root dir** (`ls`, you can see `EAlib ref test tsp README.md .etc`)
    >
    > step4, `python -m EAlib.ea.naive_ea`

  - LOOK

    -  cities' distance is stored in this adjacent  matrix (You can see `TSPProblem class`), you can call it from `Population class` by `population.problem.DM`
    - you can get the cost of a solution (individual as well) by `Individual.fitness`
    - `Individual.gene` is a optional solution (List type, it must satisty the define of TSP Problem, like **No Repeat** and **All Occur Once**)

- **TODO**

  - dataloader (at least two types)
  - fitness function (Should according to the data (geography or not))
  - performance (That's importance, high-efficient?)
  - waiting to see

  

- **File Structure**

```bash
TSP
|-- EAlib
|   |-- __init__.py
|   |-- basic	# basic components
|   |   |-- __init__.py
|   |   |-- individual.py
|   |   |-- population.py
|   |   `-- tspproblem.py
|   |-- ea	# main
|   |   |-- __init__.py
|   |   `-- naive_ea.py
|   |-- log
|   |   |-- log.conf
|   |   `-- logging.log
|   |-- operators	# TODO
|   |   |-- __init__.py
|   |   |-- crossover.py
|   |   |-- mutation.py
|   |   `-- selection.py
|   `-- utils	# TODO
|       |-- __init__.py
|       `-- dataloader.py
|-- LICENSE
|-- README.md
|-- ref
|   |-- about.md
|   |-- assignment-TSP.pdf
|   `-- assignment.md
|-- setup.py
|-- test
|   |-- EAlibTest.py	# run test here
|   |-- TSPProblemTest.py
|   `-- dataloadertest.py
`-- tsp

```






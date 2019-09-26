## EAlib

- **Install**

  ```bash
  python setup.py install
  ```

  

- **Usage**

  You can write your own code with EAlib.
  
  ```python
  from EAlib.ea import Naive_Ea
  
  Naive_Ea(filename="tsp/att48.tsp")
  ```
  
  
  
- **Run Test**

  - **Run Python files**
  
  ```bash
  $ ls
  EAlib ref test tsp README.md setup.py
  $ python test/EAlibTest.py --filename=tsp/att48.tsp
  ```
  
  - **Arguments in the file**
  
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

    

- **Development**

  - *Write your own operators*

    - ``
  
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






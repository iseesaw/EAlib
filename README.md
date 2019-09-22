## EAlib

- **Install**

  ```bash
  python setup.py install
  ```

  

- **Usage**

  ```python
  from EAlib.ea import Naive_Ea
  
  Naive_Ea("att48.tsp")
  ```
  
  
  
- **Run Example**

  ```bash
  $ ls
  EAlib ref test tsp README.md setup.py
  
  $ python -m EAlib.ea.navie_ea
  hello
  Load TSP Problem D:\ACourse\2019Fall\EvolutionaryComputation\TSP\tsp\att48.tsp Successfully! Begin computing distance matrix
  Ending computing distance matrix
  0
  Fitness
  126684.4987803689
  Gene
  [41, 39, 29, 37, 45, 24, 42, 35, 20, 10, 12, 7, 16, 5, 4, 13, 23, 9, 28, 15, 18, 27, 36, 38, 21, 31, 46, 40, 0, 33, 2, 1, 19, 14, 30, 6, 44, 34, 3, 47, 17, 8, 43, 26, 25, 22, 32, 11]
  50
  Fitness
  101200.64871772051
  Gene
  [46, 39, 29, 6, 14, 19, 42, 27, 3, 25, 40, 7, 16, 5, 2, 13, 23, 9, 28, 15, 18, 10, 36, 21, 38, 31, 20, 12, 0, 33, 4, 1, 24, 45, 30, 37, 44, 34, 41, 47, 22, 8, 43, 26, 35, 17, 32, 11]
  ```
  
  

### File Structure

```bash
|-- EAlib
|   |-- __init__.py
|   |-- basic
|   |   |-- Individual.py
|   |   |-- Population.py
|   |   |-- TSPProblem.py	# TODO judge and evolve process
|   |   `-- __init__.py
|   |-- ea	# evolution algorightms 
|   |   |-- __init__.py
|   |   `-- naive_ea.py
|   |-- operators	# TODO HERE!!!
|   |   |-- __init__.py
|   |   |-- crossover.py
|   |   |-- mutation.py
|   |   `-- selection.py
|   `-- utils	# TODO more DataLoader API
|       |-- DataLoader.py
|       `-- __init__.py
|-- LICENSE
|-- README.md
|-- ref
|   |-- about.md
|   |-- assignment-TSP.pdf
|   `-- assignment.md
|-- setup.py
|-- test	# TODO more test here
|   |-- TSPProblemTest.py
|   `-- dataloadertest.py
`-- tsp # all tsp data here
```






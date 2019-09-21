## EAlib

- **Install**

  ```bash
  python setup.py install
  ```

- **Usage**

  TODO



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






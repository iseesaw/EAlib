## EA For TSP

> 进化算法包含遗传算法

### 1 遗传算法

- 遗传算法的一般步骤：
  - 1、评估每条染色体所对应个体的适应度。
  - 2、遵照适应度越高，选择概率越大的原则，从种群中选择两个个体作为父方和母方。
  - 3、抽取父母双方的染色体，进行交叉，产生子代。
  - 4、对子代的染色体进行变异。
  - 5、重复2，3，4步骤，直到新种群的产生。
- 结束循环。



![](https://www.researchgate.net/profile/Nagham_Al-Madi/publication/242468271/figure/fig1/AS:341130517467154@1458343261324/Figure-1-Evolution-flow-of-genetic-algorithm-5.png)



### 2 代码实现

#### 2.1 代码

- 面向对象

- 模块化

  ```shell
  - # 根目录
  	- basic # 用于继承的基础父类
  		- TSPProblem
  		- Individual
  		- Population
  	- selection # 选择算子
  		- fitnetss_proportional
  		- tournament
  		- elitism
  	- mutation # 变异算子
  		- insert
  		- swap
  		- inversion
  		- scramble
  	- crossover # 交叉算子
  		- Order
  		- PMX
  		- Cy_cle
  		- Edge_Recombination
  	- eas # 进化算法
  	- test # 实验
  	- exception # 异常类(可选)
  	- log # 日志文件
  	- README.md
  ```

  

- 注释

  - 文件头

    ```python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # @Date    : 2019-09-16 11:00:13
    # @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
    # @Link    : https://github.com/iseesaw
    # @Version : $Id$
    
    """
    description
    """
    ```

  - 类注释

    ```python
    class ClassName(object):
        """docstring for ClassName"""
        def __init__(self, arg):
            super(ClassName, self).__init__()
            self.arg = arg
    ```

    

  - 函数注释

    ```python
    
    def func(param1, param2):
    	"""
    	:param param1: ...
    	:param param2: ...
    	:return: ...
    	"""
    ```

- 日志

  ```python
  # 使用 Python logging库
  import logging
  logging.basicConfig(level=logging.INFO,
                      filename='log/log.log',
                      datefmt='%Y/%m/%d %H:%M:%S',
                      format='%(asctime)s - %(levelname)s - %(message)s')
  ```

- 参数

  - 交叉概率，prob_c
  - 变异概率，prob_m
  - 保留概率，prob_s
  - 最大代数，max_gen
  - 群体规模，unit_num
  - 城市坐标，city_loc
  - 城市距离，cite_dis
  - 每一代最优解，best_ones

- 基本类

  - TSPProblem

    - filename，readfile
    - cite_loc -> cite_dis

  - Population

    - param：best_one，max_gen，unit_num，prob_c，prob_m，prob_s

    - initPopulation

      ```python
      self.individuals = []
      for i in range(self.unit_num):
          gene = [x for x in range(self.n)]
          random.shuffle(gene)
          individual = Individual(gene)
          self.individuals.append(individual)
      ```

      

    - judge

      ```python
      
      ```

      

    - newChild

      ```python
      parent1 = select(self.individuals)
      rate = random.random()
      if rate < prob_c:
          parent2 = select(self.individuals)
          gene = cross(parent1, parent2)
       else:
          gene = parent1
          
      rate = random.random()
      if rate < prob_m:
          gene = mutation(gene)
      
      return Individual(gene)
      ```

      

    - evolve

      ```python
      newIndividuals = []
      for i in range(unit_num):
          newIndividuals.append(newChild())
      self.individuals = newIndividuals
      self.generation += 1
      log(...)
      ```

      

  - Individual（基因编码方法：二进制、实数）

    - parameter：n，fitness，seq

    - n 个城市序号的序列
    - 自我检测，无重复，都有一次
    - 

- 操作

  - 步骤
    - step1，初始化
    - step2，评估
    - step3，选择
    - step4，交叉
    - step5，变异
    - 重复2-5，直到达到 max_gen
  - 辅助
    - 初始化种群，random_init
    - 适应度函数
      - 多种选择
      - $fitness = \frac{1}{\sum \limits_{i=2}^{N}{Disctance(i-1, i)}}$
    - 日志信息，logging
    - 错误信息，exception
    - 可视化解

#### 2.2 Class

##### 2.2.1 `class TSPProblem`



##### 2.2.2 `class Individual`



##### 2.2.3 `class Population`



#### 2.3 模块

> Slide [**02-Genetic Algorithms**]()

##### 2.3.1 mutation operators

- *insert*



- *swap*



- *inversion*



- scramble*



##### 2.3.2 crossover operators

> [遗传算法中几种交叉算子小结](https://blog.csdn.net/u012750702/article/details/54563515)

- *Order Crossover*



- *PMX Crossover*



- *Cy-cle Crossover*



- *Edge Recombination*





##### 2.3.3 selection methods

> [遗传算法中几种不同选择算子](https://zhuanlan.zhihu.com/p/29474851)

- *fitnetss-proportional*

> 轮盘赌策略



- *tournament selection*

> 锦标赛选择



- *elitism*

> 精英策略



### 3 实验

> 基于不同模块，使用交叉和变异实现三种不同的遗传算法



- **实验1**

  - TSPlib中数据集
    - EIL51、EIL76、EIL101、ST70、KROA100、KROC100、KROD100、LIN105、PCB442、PR2392
  - 种群大小设置
    - 10、20、50、100
  - 迭代次数（繁衍代数）
    - 5000、10000、20000
  - 总计：3 种算法 * 4 种种群大小 * 10 个数据集 = 120 个实验

  

- **实验2**

  - *Run the best algorithm with a population size of 50 for 10000 generations on the ten TSPlib instances.*
  - *Report for each instance*
    - *either (1) the average cost and the standard deviation*
    - *or (2) the median cost and the interquartile range*



### 4 Reference

- [Introduction to Genetic Algorithms](https://blog.floydhub.com/introduction-to-genetic-algorithms/)

- [遗传算法 - 维基百科]([https://zh.wikipedia.org/wiki/%E9%81%97%E4%BC%A0%E7%AE%97%E6%B3%95](https://zh.wikipedia.org/wiki/遗传算法))

- [【算法】超详细的遗传算法(Genetic Algorithm)解析](https://www.jianshu.com/p/ae5157c26af9)

- [https://blog.csdn.net/u010451580/article/details/51178225](https://blog.csdn.net/u010451580/article/details/51178225)
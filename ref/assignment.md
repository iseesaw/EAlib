## *The Traveling Salesman Problem*

> Implementation + Videos Report
>
> **Due Data: 11:55pm, 27 September 2019**



### *Overview*

> 关键词：进化算法、**遗传算法**、**旅行商问题**

- 完成 EA 算法的不同模块，并解决 TSP 问题
- 用于 TSP 问题的 EA 算法需要在 TSPlib 的 *benchmarks*  上进行测试



### *Assignment*

- *TSP* 问题

  - *Input*： $n$ 个城市，城市 $i$ 和 $j$ 之间（$1 \leq i,j \leq n$）的距离 $d_{ij}$

  - *Output*：求解访问每一座城市一次并回到起始城市的最短回路

- 目标：针对 *TSP* 问题，设计一个库并实现 *EA* 算法

  - 面向对象
  - 模块化
  - 便于拓展不同的表示
    - *individual representations*、*operators*、*selection methods*



### *Exercise*

- *Problem Representation and  TSPlib*
  - class ***TSPProblem***
    - *TSP* 问题表示
    - 参考 *TSPlib* 中相关文件
    - [the problem files](http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/tsp/)
    - [more information](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)

- *Individual and Population Representation*
  - class ***Individual***
    - 将 TSP 的可能解表示为给定城市的的一个排列（一个解表示一个个体）
    - 随机初始化可能解（要求 $O(n)$ 时间复杂度）
  - class ***Population***
    - 一个解（个体）的集合表示一个种群
    - 确保能够针对给定问题来评价解的质量
- *Variation operators*
  - 实现不同的变异算子（***mutation operators***）
    - *insert*
    - *swap*
    - *inversion*
    -  *scramble*
  - 实现不同的交叉算子（***crossover operators***）
    - *Order Crossover*
    - *PMX Crossover*
    - *Cy-cle Crossover*
    - *Edge Recombination*

- *Selection*
  - 实现不同的选择方法（***selection methods***）
    - *fitnetss-proportional*
    - *tournament selection*
    - *elitism*
- *Evolutionary Algorithms and Benchmarking*
  - 基于不同模块，使用交叉和变异实现三种不同的遗传算法
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
- *Notes*
  - ~~for the large instance~~
  - 重复实验最好的算法，10次以上（30或100更好）
  - 对于实验1和实验2分别提交一个结果文件（要求 *plain text file，no Excel sheet*）
  - 详细的说明文档以及README（便于复现）

- *Video Report*

  - **4-5 分钟英文小视频**
    - 介绍小组
    - 阐述实验1中设计的三种算法以及设计动机
    - 报告实验2中最优算法的实验结果
    - 未来的改进
  - 使用插图、表格、动画等
  - 提交视频链接（优酷、Youtube）

  

### *Marking*

- 评分标注
  - 25%，**全部正确的实现**
  - 50%，**代码质量**（简洁、面向对象、类结构）
  - 25%、**代码注释**
- Refer to [Feedback](https://cs.adelaide.edu.au/~markus/teaching/feedback.txt)



### *Requirements*

- 源代码
- 配置文件
- ***README.txt***
  - 代码运行方法
  - 成员姓名、学号、邮箱地址
- 两个纯文本的结果文件
  - 三种算法实验结果
  - 最优算法实验结果
- 日志文件
  - *A short **log-files** that still show the overall optimisation*
    - *e.g. output the "best fitness in the current population" every 100 generations*
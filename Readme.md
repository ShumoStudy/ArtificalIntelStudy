# Artificial Intelligence Study Homework From PXXU

## week2

### question1:add
    
    Return the sum of a and b

### question2:

    To run this script, type
    
    python buyLotsOfFruit.py
    
    Once you have correctly implemented the buyLotsOfFruit function,
    the script should produce the output:
    
    Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25

### question3:

    Here's the intended output of this script, once you fill it in:
    
    Welcome to shop1 fruit shop
    Welcome to shop2 fruit shop
    For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
    For orders:  [('apples', 3.0)] best shop is shop2

## week3-4

### question:

    In search.py, you will implement generic search algorithms which are called by
    Pacman agents (in searchAgents.py). 

### question1:

    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    该算法要求首先搜索搜索树中最深的节点。
    您的搜索算法需要返回到达目标的操作列表，并且必须实现图搜索算法。
    为了开始解决问题，您可以尝试使用一些简单的命令来理解传入算法的搜索问题。
    以下是一些示例命令：
    
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
代码解释

    这段代码实现了一个使用深度优先搜索（DFS）算法的通用搜索算法，以求解问题（problem）的解决方案。
    它将起始状态（initState）加入一个堆栈（frontier）中，并通过使用节点指针（parentOf、actionTo 和 pathCostOf）
    和探索集合（exploredSet）来跟踪搜索过程中访问过的状态。
    在算法的主循环中，每次从堆栈中取出一个节点（thisNode），并检查它是否是目标状态。
    如果是，算法将使用指针回溯到起始状态，并将路径上的每个动作添加到一个列表中，并将该列表反转并返回作为最终的解决方案。
    如果当前节点不是目标状态，则算法会将其所有的未探索子节点添加到堆栈中，并将其加入探索集合。
    然后，算法更新指针和路径成本，并继续迭代堆栈，直到找到目标状态或堆栈为空。如果搜索完整个状态空间后，仍然没有找到解决方案，则算法返回一个空列表。
    
### question2:

    Search the shallowest nodes in the search tree first.
    首先搜索搜索树中最浅的节点

### question3:

    Search the node of least total cost first.
    首先搜索总成本最低的节点

### question4:

    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    启发式函数估计从当前状态到最近状态的成本
    提供的 SearchProblem 中的目标。这种启发式是微不足道的。

### question5:

    Search the node that has the lowest combined cost and heuristic first.
    首先搜索具有最低组合成本和启发式的节点。

### question6:

### question7:

### question8:
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# question1
def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    "搜索深度优先搜索（DFS）算法，应该返回到达目标状态的行动列表。需要实现图搜索算法。"

    visited = set()
    stack = util.Stack()

    # Push the starting state and path to the stack
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        state, actions = stack.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in visited:
                    # Add the successor and the actions required to reach it
                    stack.push((successor, actions + [action]))

    return []

# question2

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    "搜索广度优先搜索（BFS）算法，应该返回到达目标状态的行动列表。"
    from util import Queue
    queue = Queue()
    visited = set()
    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        state, actions = queue.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.add(state)
            for successor, action, step_cost in problem.getSuccessors(state):
                queue.push((successor, actions + [action]))

    return []

# question3
def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "YOUR CODE HERE"
    # 用了一个集合 visited 来存储已经访问过的状态
    # 我们避免了在队列中搜索来检查状态是否已经访问过的开销，从而使算法的时间复杂度更低。
    from util import Queue
    queue = Queue()
    visited = set()
    start_state = problem.getStartState()
    queue.push((start_state, []))
    visited.add(start_state)

    while not queue.isEmpty():
        state, actions = queue.pop()
        if problem.isGoalState(state):
            return actions
        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in visited:
                visited.add(successor)
                queue.push((successor, actions + [action]))

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# question4
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    "搜索A*搜索算法，应该返回到达目标状态的行动列表。使用提供的启发式函数估计从当前状态到最近目标的成本"
    visited = set()  # 已访问状态集合
    pq = util.PriorityQueue()  # 优先队列，按照总代价从小到大存储状态节点
    pq.push((problem.getStartState(), [], 0), 0)  # 将初始状态加入队列中

    while not pq.isEmpty():  # 当队列不为空时
        currState, actions, currCost = pq.pop()  # 取出队列中的节点

        if problem.isGoalState(currState):  # 判断当前状态是否为目标状态
            return actions

        if currState not in visited:  # 当前状态未被访问
            visited.add(currState)  # 将当前状态加入已访问集合中

            for nextState, action, stepCost in problem.getSuccessors(currState):  # 遍历当前状态的所有子节点
                nextActions = actions + [action]  # 更新路径
                nextCost = currCost + stepCost + heuristic(nextState, problem)  # 更新总代价
                pq.push((nextState, nextActions, currCost + stepCost), nextCost)  # 将子节点加入优先队列中

    return []  # 未找到路径，返回空列表

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

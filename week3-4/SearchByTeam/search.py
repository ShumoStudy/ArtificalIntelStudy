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
    n = Directions.NORTH
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    return  [s, s, w, s, w, w, s, w]

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
    # stack 有权重的队列
    stack = util.Stack()
    # seen 是否遍历过
    seen = set()
    # nodes 节点的信息
    node = util.Counter({"state": problem.getStartState(), "path": []})

    stack.push(node)
    while True:
        if stack.isEmpty():
            return None
        node = stack.pop()
        if problem.isGoalState(node["state"]):
            return node["path"]
        elif node["state"] not in seen:
            seen.add(node["state"])
            nodes = problem.getSuccessors(node["state"])
            for childnode in nodes:
                childnode = {"state": childnode[0], "path": node["path"] + [childnode[1]]}
                stack.push(childnode)

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***" 
    """ Look for only one goal """
    # # queue 队列
    # queue = util.Queue()
    # # seen 是否遍历过
    # seen = set()
    # # nodes 节点的信息
    # node = util.Counter({"state": problem.getStartState(), "path": []})

    # queue.push(node)
    # while True:
    #     if queue.isEmpty():
    #         return None
    #     node = queue.pop()
    #     if problem.isGoalState(node["state"]):
    #         return node["path"]
    #     elif node["state"] not in seen:
    #         seen.add(node["state"])
    #         nodes = problem.getSuccessors(node["state"])
    #         for childnode in nodes:
    #             childnode = {"state": childnode[0], "path": node["path"] + [childnode[1]]}
    #             queue.push(childnode)
    """ Look for multiple targets, but not all corners """
    # # queue 队列
    # queue = util.Queue()
    # # seen 是否遍历过
    # seen = set()
    # # nodes 节点的信息
    # node = util.Counter({"state": problem.getStartState(), "path": []})
    # # paths 记录总路径
    # # paths = []

    # queue.push(node)
    # while True:
    #     if queue.isEmpty():
    #         return None
    #     node = queue.pop()
    #     isGoalState = problem.isGoalState(node["state"])
    #     if isGoalState[0]:
    #         # paths += node["path"]
    #         if isGoalState[1]:
    #             return node["path"]
    #         node = util.Counter({"state": node["state"], "path": node["path"]})
    #         while not queue.isEmpty():
    #             queue.pop()
    #         queue.push(node)
    #         seen = set()
    #     elif node["state"] not in seen:
    #         seen.add(node["state"])
    #         nodes = problem.getSuccessors(node["state"])
    #         for childnode in nodes:
    #             childnode = {"state": childnode[0], "path": node["path"] + [childnode[1]]}
    #             queue.push(childnode)
    """ all """
    # # 初始化(有权)
    # # 初始位置
    # start_state = problem.getStartState()
    # # seen 是否遍历过
    # seen = set()
    # # seen.add(start_state)
    # # nodes 节点的信息
    # node = util.Counter({"state": start_state, "path": []})
    # # queue 队列
    # queue = util.Queue()
    # queue.push(node)

    # while not queue.isEmpty():
    #     node = queue.pop()
    #     if problem.isGoalState(node["state"]):
    #         return node["path"]
    #     elif node["state"][0] not in seen:
    #         seen.add(node["state"])
    #         childnodes = problem.getSuccessors(node["state"])
    #         for childnode in childnodes:
    #             childnode = {"state": childnode[0], "path": node["path"] + [childnode[1]]}
    #             queue.push(childnode)
    # return None

    # 初始化数据结构
    start_state = problem.getStartState()
    seen = set()
    seen.add(start_state)
    queue = util.Queue()
    node = {"state": start_state, "path": []}
    queue.push(node)

    while not queue.isEmpty():
        node = queue.pop()
        if problem.isGoalState(node["state"]):
            return node["path"]
        for childnode in problem.getSuccessors(node["state"]):
            if childnode[0] not in seen:
                seen.add(childnode[0])
                childnode = {"state": childnode[0], "path": node["path"]+[childnode[1]]}
                queue.push(childnode)

    # 如果搜索失败，返回空列表
    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # PriorityQueue 有权重的队列
    priorityqueue = util.PriorityQueue()
    # seen 是否遍历过
    seen = set()
    # nodes 节点的信息
    node = util.Counter({"state": problem.getStartState(), "path": [], "cost": 0})

    priorityqueue.push(node, node["cost"])
    while True:
        if priorityqueue.isEmpty():
            return None
        node = priorityqueue.pop()
        if problem.isGoalState(node["state"]):
            return node["path"]
        elif node["state"] not in seen:
            seen.add(node["state"])
            nodes = problem.getSuccessors(node["state"])
            for childnode in nodes:
                childnode = {"state": childnode[0], "path": node["path"] + [childnode[1]], "cost": node["cost"] + childnode[2]}
                priorityqueue.update(childnode, childnode["cost"])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# tm = 0
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # pqf 有权重的队列
    # print(heuristic.__name__)
    # def fn(item):
    #     ret = heuristic(item["state"], problem) + item['cost']
    #     if globals()['tm'] < 100:
    #         globals()['tm'] += 1
    #         print(item)
    #         print(ret)
    #     return ret
    pqf = util.PriorityQueueWithFunction(lambda x: heuristic(x["state"], problem)+x["cost"])
    # seen 是否遍历过
    seen = set()
    # nodes 节点的信息
    node = util.Counter({"state": problem.getStartState(), "path": [], "cost": 0})

    pqf.push(node)
    while True:
        if pqf.isEmpty():
            return None
        node = pqf.pop()
        if problem.isGoalState(node["state"]):
            return node["path"]
        elif node["state"] not in seen:
            seen.add(node["state"])
            nodes = problem.getSuccessors(node["state"])
            for childnode in nodes:
                childnode = {"state": childnode[0], "path": node["path"] + [childnode[1]], "cost": node["cost"] + childnode[2]}
                pqf.push(childnode)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

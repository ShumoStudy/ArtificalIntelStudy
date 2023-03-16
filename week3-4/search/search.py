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
    stack = [(problem.getStartState(), [problem.getStartState()])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if problem.isGoalState(node):
            return path
        visited.add(node)
        for neighbor in problem.getSuccessors(node):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return []

# question2

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # 使用队列保存待搜索的节点
    queue = util.Queue()
    # 将起始节点放入队列中
    queue.append(problem.getStartState())
    # 使用一个字典记录已经访问过的节点
    visited = {}
    visited[problem.getStartState()] = None

    # 开始搜索
    while queue:
        # 取出队列头部节点
        node = queue.popleft()
        # 如果该节点是目标节点，结束搜索并返回路径
        if problem.isGoalState(node):
            path = []
            while node is not None:
                path.append(node)
                node = visited[node]
            return path[::-1]
        # 否则，将该节点的所有未访问的邻居节点加入队列中
        for neighbor in problem.getSuccessors(node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = node

    # 搜索结束，未找到目标节点，返回空路径
    return []


    # util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    """
        最小代价优先搜索算法
        """
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    frontier = util.PriorityQueue()
    frontier.push((0, [startState], []))
    explored = set()

    while not frontier.empty():
        node = frontier.get()
        state = node[1][-1]
        path = node[2]

        if problem.isGoalState(state):
            return path

        if state not in explored:
            explored.add(state)

            for successor, action, cost in problem.getSuccessors(state):
                if successor not in explored:
                    totalCost = node[0] + cost
                    successorPath = path + [action]
                    frontier.put((totalCost, node[1] + [successor], successorPath))

    return None
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    print("Start:", problem.getStartState())
    print("Start heuristic: ", problem, heuristic(problem.getStartState(), problem))
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    visited, frontier = set(), [
        [
            problem.getStartState(),
            0,
            0
        ]
    ]

    while frontier:
        node = frontier.pop(0)
        if node[0] not in visited:
            visited.add(node[0])
            if problem.isGoalState(node[0]):
                rw = buildRocksWay(node)
                print (rw)
                return rw

            sucessors = problem.getSuccessors(node[0])
            for sucessor in sucessors:
                sucessor = list(sucessor)
                sucessor[2] += node[2]
                sucessor.append(node)
                fx = sucessor[2] + heuristic(sucessor[0], problem)
                print
                "f(x):", fx
                sucessor.append(fx)

                frontier.append(sucessor)

            frontier = sorted(frontier, key=lambda n: n[4])
    return False



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

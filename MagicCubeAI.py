from MagicCube import MagicCubeLogic
from copy import deepcopy
from PriorityQueue import PriorityQueue

def shuffleMagicCube(mc, stepCnt):
    from random import randint
    consec_cnt = 0
    prev_act = None
    actions = []
    for i in range(stepCnt):
        act = MagicCubeLogic.availActions[randint(0,len(MagicCubeLogic.availActions)-1)]
        if consec_cnt == 2:
            while act == prev_act:
                act = MagicCubeLogic.availActions[randint(0,len(MagicCubeLogic.availActions)-1)]

        if act == prev_act:
            consec_cnt += 1
        else:
            consec_cnt = 1
            prev_act = act
        mc.takeAction(act)
        actions.append(act)
    print actions
    return mc, actions[::-1]

class MagicCubeAI:

    def __init__(self, beginState):
        self.state = beginState

    @staticmethod
    def GetNextState(state, act):
        nextState = deepcopy(state)
        nextState.takeAction(act)
        return nextState

    # iterative depth first search, A* ? (what is heuristic?)
    # TODO:
    # add max consecutive step restriction
    def IDA(self, maxDepth=3):
        from random import randint
        pq = PriorityQueue(['h'])
        stack = [{"state": self.state, "depth": 0, "act": None, "actions": deepcopy(MagicCubeLogic.availActions), "prev":None}]

        while True:
            while len(stack) > 0:
                obj = stack[len(stack)-1]
                state = obj["state"]
                depth = obj["depth"]
                actions = obj["actions"]

                # if reach goal?
                if state.IsGoal():
                    path = []
                    while True:
                        act = obj["act"]
                        prev = obj["prev"]
                        if prev != None:
                            obj = prev
                        else:
                            break
                        path.append(act)
                    return path

                if depth == maxDepth:
                    pq.add({"obj": obj, "h": MagicCubeAI.heuristic(state)})
                    stack.pop()
                    continue

                if len(actions) == 0:
                    stack.pop()
                    continue
                act = actions.pop()
                nextState = MagicCubeAI.GetNextState(state, act)
                nextObj = {"state": nextState,
                           "depth": depth+1,
                           "act": act,
                           "actions": deepcopy(MagicCubeLogic.availActions),
                           "prev": obj}
                stack.append(nextObj)

            if len(pq.queue) > 1000:
                while len(pq.queue) > randint(2, 100):
                    pq.pop()
            elem = pq.pop()
            obj = elem["obj"]
            obj["depth"] = 0
            stack = [obj]
            print len(pq.queue)

    @staticmethod
    def heuristic(state):
        # this heuristic might be problematic
        # as the number of mispositioned cube != the number of steps required to get the goal

        # TODO:
        # cubes on the line: sum(number of dislocated faces of each cube / 2) / 4
        # cubes on the corner: sum(number of dislocated faces + 1 / 2) / 4
        # max(cubes on the line, cubes on the corner
        dist = 0
        for i in range(27):
            truePos = state.ori_order[i]
            curPos = state.cur_order[i]

            """
            x1 = truePos % 3
            y1 = truePos / 9
            z1 = truePos / 3

            x2 = curPos % 3
            y2 = curPos / 9
            z2 = curPos / 3

            if x1 != x2:
                dist += 1
            if y1 != y2:
                dist += 1
            if z1 != z2:
                dist += 1
            """
            if truePos != curPos:
                dist += 1

        return dist


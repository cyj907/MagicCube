from copy import deepcopy
from PriorityQueue import PriorityQueue
import MagicCubeConst

def shuffleMagicCube(mc, stepCnt):
    from random import randint
    consec_cnt = 0
    prev_act = None
    actions = []
    for i in range(stepCnt):
        act = MagicCubeConst.availActions[randint(0,len(MagicCubeConst.availActions)-1)]
        while prev_act != None and act == MagicCubeConst.pair_orients[prev_act]:
            act = MagicCubeConst.availActions[randint(0,len(MagicCubeConst.availActions)-1)]

        if consec_cnt == 2:
            while act == prev_act or prev_act != None and act == MagicCubeConst.pair_orients[prev_act]:
                act = MagicCubeConst.availActions[randint(0,len(MagicCubeConst.availActions)-1)]

        if act == prev_act:
            consec_cnt += 1
        else:
            consec_cnt = 1
            prev_act = act
        mc.takeAction(act)
        actions.append(act)
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
    # add max consecutive step restriction
    def IDA(self, maxDepth=5):
        from random import randint
        pq = PriorityQueue(['h'])
        stack = [{"state": self.state, "depth": 0, "act": None, "actions": deepcopy(MagicCubeConst.availActions), "prev":None}]

        while True:
            aaa = 0
            while len(stack) > 0:
                aaa += 1
                print aaa
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
                act = actions.pop(randint(0,len(actions)-1))
                # prevent actions cancelling out
                if MagicCubeConst.pair_orients[act] == obj["act"]:
                    if len(actions) == 0:
                        stack.pop()
                        continue
                    act = actions.pop(randint(0,len(actions)-1))
                # prevent the same consecutive actions
                if act == obj["act"]:
                    prev = obj["prev"]
                    if prev != None and prev["act"] == act:
                        if len(actions) == 0:
                            stack.pop()
                            continue
                        else:
                            act = actions.pop(randint(0,len(actions)-1))

                nextState = MagicCubeAI.GetNextState(state, act)
                nextObj = {"state": nextState,
                           "depth": depth+1,
                           "act": act,
                           "actions": deepcopy(MagicCubeConst.availActions),
                           "prev": obj}
                stack.append(nextObj)

            d = 12*maxDepth
            if len(pq.queue) > d:
                left = randint(3, min(d,len(pq.queue)))
                while len(pq.queue) > left:
                    pq.pop()
            print len(pq.queue)
            elem = pq.pop()
            obj = elem["obj"]
            obj["depth"] = 0
            stack = [obj]

    @staticmethod
    def heuristic(state):
        # this heuristic might be problematic
        # as the number of mispositioned cube != the number of steps required to get the goal

        # TODO:
        # cubes on the line: sum(number of dislocated faces of each cube / 2) / 4
        # cubes on the corner: sum(number of dislocated faces + 1 / 2) / 4
        # max(cubes on the line, cubes on the corner

        dist_edge = 0
        dist_corn = 0
        for i in range(27):
            id = state.cur_order[i]
            face_list = state.face_orients[id]
            cnt = 0
            for i in range(6):
                if MagicCubeConst.cube_visible_faces[id][i]:
                    cube_face_color = MagicCubeConst.colors[MagicCubeConst.faces2Indices[face_list[i]]]
                    orient_face_color = MagicCubeConst.colors[i]
                    if cube_face_color != orient_face_color:
                        cnt += 1
            if id in MagicCubeConst.edgeCubeIndices:
                dist_edge += cnt
            else:
                dist_corn += cnt + 1
        return (dist_edge + dist_corn) / 8



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


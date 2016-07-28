from MagicCube import MagicCubeLogic, ProjectionViewer
from MagicCubeAI import MagicCubeAI, shuffleMagicCube
import MagicCubeConst


class MagicCubeSimulation:
    @staticmethod
    def run():
        pv = ProjectionViewer(600, 600)
        initState = MagicCubeLogic()
        maxStep = 20
        shuffledState, steps = shuffleMagicCube(initState, maxStep)
        pv.runSteps(steps)
        SmartGuy = MagicCubeAI(shuffledState)
        steps = SmartGuy.IDA(maxStep)
        pv.runSteps(steps, True)

MagicCubeSimulation.run()

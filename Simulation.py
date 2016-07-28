from MagicCube import MagicCubeLogic, ProjectionViewer
from MagicCubeAI import MagicCubeAI, shuffleMagicCube


class MagicCubeSimulation:
    @staticmethod
    def run():
        pv = ProjectionViewer(600, 600)
        initState = MagicCubeLogic()
        shuffledState, steps = shuffleMagicCube(initState, 2)
        pv.runSteps(steps)
        SmartGuy = MagicCubeAI(shuffledState)
        steps = SmartGuy.IDA()
        pv.runSteps(steps, True)

MagicCubeSimulation.run()

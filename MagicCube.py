from Cube import Cube
import pygame
import math
from copy import deepcopy, copy

key_to_view = {
    pygame.K_q:      (lambda x: x.rotateAll('X',  0.1 * math.pi)),
    pygame.K_w:      (lambda x: x.rotateAll('X', -0.1 * math.pi)),
    pygame.K_a:      (lambda x: x.rotateAll('Y',  0.1 * math.pi)),
    pygame.K_s:      (lambda x: x.rotateAll('Y', -0.1 * math.pi)),
    pygame.K_z:      (lambda x: x.rotateAll('Z',  0.1 * math.pi)),
    pygame.K_x:      (lambda x: x.rotateAll('Z', -0.1 * math.pi))
}

# TODO: add more action
key2act = {
    pygame.K_f: "F",
    pygame.K_F: "F'",
    pygame.K_b: "B",
    pygame.K_B: "B'",
    pygame.K_l: "L",
    pygame.K_L: "L'",
    pygame.K_r: "R",
    pygame.K_R: "R'",
    pygame.K_u: "U",
    pygame.K_U: "U'",
    pygame.K_d: "D",
    pygame.K_D: "D'"
}


class MagicCubeLogic:
    def __init__(self):
        self.ori_order = [i for i in range(27)]
        self.cur_order = [i for i in range(27)]
        # add face related attributes (colors, orientation)
        # when an action is taken, the face attributes will be changed

    # add dist from each face of the small cube to the whole face of the correct magic cube
    # TODO

    availActions = ['F', 'B', 'L', 'R', 'U', 'D']

    cube_proj_func = {}
    cube_proj_func['F'] = [(18,20),(19,11),(20,2),(9,19),(0,18),(1,9),(11,1),(2,0)]
    cube_proj_func['B'] = [(24,6),(15,7),(6,8),(8,26),(7,17),(25,15),(26,24),(17,25)]
    cube_proj_func['L'] = [(24,18),(21,9),(18,0),(9,3),(0,6),(3,15),(6,24),(15,21)]
    cube_proj_func['R'] = [(26,8),(17,5),(8,2),(5,11),(2,20),(11,23),(20,26),(23,17)]
    cube_proj_func['U'] = [(24,26),(25,23),(26,20),(23,19),(20,18),(19,21),(18,24),(21,25)]
    cube_proj_func['D'] = [(8,6),(7,3),(6,0),(3,1),(0,2),(1,5),(2,8),(5,7)]


    def takeAction(self, action):
        prev_order = deepcopy(self.cur_order)
        for a, b in MagicCubeLogic.cube_proj_func[action]:
            self.cur_order[b] = prev_order[a]

    def IsGoal(self):
        isGoal = True
        for i in range(27):
            if self.ori_order[i] != self.cur_order[i]:
                isGoal = False
                break
        return isGoal

    def __deepcopy__(self, memo):
        obj = copy(self)
        obj.ori_order = deepcopy(self.ori_order)
        obj.cur_order = deepcopy(self.cur_order)
        return obj

class MagicCubeDisplay:
    def __init__(self, center, d):
        self.magicCubeCenter = center
        self.cubeCenters = []
        self.cubeRadius = d / 6
        self.cubes = []

        # bottom
        self.cubeCenters.append([center[0],center[1]-self.cubeRadius*2-1,center[2]])
        # front
        self.cubeCenters.append([center[0],center[1],center[2]-self.cubeRadius*2-1])
        # left
        self.cubeCenters.append([center[0]-self.cubeRadius*2-1,center[1], center[2]])
        # back
        self.cubeCenters.append([center[0],center[1],center[2]+self.cubeRadius*2+1])
        # right
        self.cubeCenters.append([center[0]+self.cubeRadius*2+1,center[1], center[2]])
        # top
        self.cubeCenters.append([center[0],center[1]+self.cubeRadius*2+1,center[2]])

        # top nine cubes
        self.cubes.append([Cube((self.cubeCenters[5][0]-self.cubeRadius*2-1,
                                self.cubeCenters[5][1],
                                self.cubeCenters[5][2]-self.cubeRadius*2-1), self.cubeRadius),
                           [False,True,True,False,False,True]])
        self.cubes.append([Cube((self.cubeCenters[5][0],
                                self.cubeCenters[5][1],
                                self.cubeCenters[5][2]-self.cubeRadius*2-1), self.cubeRadius),
                           [False,True,False,False,False,True]])
        self.cubes.append([Cube((self.cubeCenters[5][0]+self.cubeRadius*2+1,
                                self.cubeCenters[5][1],
                                self.cubeCenters[5][2]-self.cubeRadius*2-1), self.cubeRadius),
                           [False,True,False,False,True,True]])
        self.cubes.append([Cube((self.cubeCenters[5][0]-self.cubeRadius*2-1,
                                self.cubeCenters[5][1],
                                self.cubeCenters[5][2]), self.cubeRadius),
                           [False,False,True,False,False,True]])
        self.cubes.append([Cube((self.cubeCenters[5][0],
                                self.cubeCenters[5][1],
                                self.cubeCenters[5][2]), self.cubeRadius),
                           [False,False,False,False,False,True]])
        self.cubes.append([Cube((self.cubeCenters[5][0]+self.cubeRadius*2+1,
                                self.cubeCenters[5][1],
                                self.cubeCenters[5][2]), self.cubeRadius),
                           [False,False,False,False,True,True]])
        self.cubes.append([Cube((self.cubeCenters[5][0]-self.cubeRadius*2-1,
                                self.cubeCenters[5][1],
                                self.cubeCenters[5][2]+self.cubeRadius*2+1), self.cubeRadius),
                           [False,False,True,True,False,True]])
        self.cubes.append([Cube((self.cubeCenters[5][0],
                                self.cubeCenters[5][1],
                                self.cubeCenters[5][2]+self.cubeRadius*2+1), self.cubeRadius),
                           [False,False,False,True,False,True]])
        self.cubes.append([Cube((self.cubeCenters[5][0]+self.cubeRadius*2+1,
                                self.cubeCenters[5][1],
                                self.cubeCenters[5][2]+self.cubeRadius*2+1), self.cubeRadius),
                           [False,False,False,True,True,True]])



        # middle nine cubes
        self.cubes.append([Cube((self.magicCubeCenter[0]-self.cubeRadius*2-1,
                                self.magicCubeCenter[1],
                                self.magicCubeCenter[2]-self.cubeRadius*2-1), self.cubeRadius),
                           [False,True,True,False,False,False]])
        self.cubes.append([Cube((self.magicCubeCenter[0],
                                self.magicCubeCenter[1],
                                self.magicCubeCenter[2]-self.cubeRadius*2-1), self.cubeRadius),
                           [False,True,False,False,False,False]])
        self.cubes.append([Cube((self.magicCubeCenter[0]+self.cubeRadius*2+1,
                                self.magicCubeCenter[1],
                                self.magicCubeCenter[2]-self.cubeRadius*2-1), self.cubeRadius),
                           [False,True,False,False,True,False]])
        self.cubes.append([Cube((self.magicCubeCenter[0]-self.cubeRadius*2-1,
                                self.magicCubeCenter[1],
                                self.magicCubeCenter[2]), self.cubeRadius),
                           [False,False,True,False,False,False]])
        self.cubes.append([Cube((self.magicCubeCenter[0],
                                self.magicCubeCenter[1],
                                self.magicCubeCenter[2]), self.cubeRadius),
                           [False,False,False,False,False,False]])
        self.cubes.append([Cube((self.magicCubeCenter[0]+self.cubeRadius*2+1,
                                self.magicCubeCenter[1],
                                self.magicCubeCenter[2]), self.cubeRadius),
                           [False,False,False,False,True,False]])
        self.cubes.append([Cube((self.magicCubeCenter[0]-self.cubeRadius*2-1,
                                self.magicCubeCenter[1],
                                self.magicCubeCenter[2]+self.cubeRadius*2+1), self.cubeRadius),
                           [False,False,True,True,False,False]])
        self.cubes.append([Cube((self.magicCubeCenter[0],
                                self.magicCubeCenter[1],
                                self.magicCubeCenter[2]+self.cubeRadius*2+1), self.cubeRadius),
                           [False,False,False,True,False,False]])
        self.cubes.append([Cube((self.magicCubeCenter[0]+self.cubeRadius*2+1,
                                self.magicCubeCenter[1],
                                self.magicCubeCenter[2]+self.cubeRadius*2+1), self.cubeRadius),
                           [False,False,False,True,True,False]])

        # bottom nine cubes
        self.cubes.append([Cube((self.cubeCenters[1][0]-self.cubeRadius*2-1,
                                self.cubeCenters[1][1]-self.cubeRadius*2-1,
                                self.cubeCenters[1][2]), self.cubeRadius),
                           [True,True,True,False,False,False]])
        self.cubes.append([Cube((self.cubeCenters[1][0],
                                self.cubeCenters[1][1]-self.cubeRadius*2-1,
                                self.cubeCenters[1][2]), self.cubeRadius),
                           [True,True,False,False,False,False]])
        self.cubes.append([Cube((self.cubeCenters[0][0]+self.cubeRadius*2+1,
                                self.cubeCenters[0][1],
                                self.cubeCenters[0][2]-self.cubeRadius*2-1), self.cubeRadius),
                           [True,True,False,False,True,False]])
        self.cubes.append([Cube((self.cubeCenters[0][0]-self.cubeRadius*2-1,
                                self.cubeCenters[0][1],
                                self.cubeCenters[0][2]), self.cubeRadius),
                           [True,False,True,False,False,False]])
        self.cubes.append([Cube((self.cubeCenters[0][0],
                                self.cubeCenters[0][1],
                                self.cubeCenters[0][2]), self.cubeRadius),
                           [True,False,False,False,False,False]])
        self.cubes.append([Cube((self.cubeCenters[0][0]+self.cubeRadius*2+1,
                                self.cubeCenters[0][1],
                                self.cubeCenters[0][2]), self.cubeRadius),
                           [True,False,False,False,True,False]])
        self.cubes.append([Cube((self.cubeCenters[0][0]-self.cubeRadius*2-1,
                                self.cubeCenters[0][1],
                                self.cubeCenters[0][2]+self.cubeRadius*2+1), self.cubeRadius),
                           [True,False,True,True,False,False]])
        self.cubes.append([Cube((self.cubeCenters[0][0],
                                self.cubeCenters[0][1],
                                self.cubeCenters[0][2]+self.cubeRadius*2+1), self.cubeRadius),
                           [True,False,False,True,False,False]])
        self.cubes.append([Cube((self.cubeCenters[0][0]+self.cubeRadius*2+1,
                                self.cubeCenters[0][1],
                                self.cubeCenters[0][2]+self.cubeRadius*2+1), self.cubeRadius),
                           [True,False,False,True,True,False]])

class ProjectionViewer:
    """ Displays 3D objects on a Pygame screen """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Magic Cube Display')
        self.background = (10,10,50)

        self.magicCubeDisplay = MagicCubeDisplay((width/2,width/2,width/12*3+1), width / 2)
        self.nodeColour = (255,255,255)
        self.edgeColour = (255,255,255)
        self.faceColours = [(255, 255, 0),(255,0,0), (0,255,0), (255,0,255), (0,0,255), (255,255,255)]
        self.nodeRadius = 4

    def showAnimation(self, action):
        if action == 'F':
            center = self.magicCubeDisplay.cubes[10][0].center
            for i in [0,1,2,9,10,11,18,19,20]:
                cube, colorDisplay = self.magicCubeDisplay.cubes[i]
                cube.rotateLine(self.magicCubeDisplay.magicCubeCenter, tuple(center), -math.pi/20)
        elif action == 'B':
            center = self.magicCubeDisplay.cubes[16][0].center
            for i in [6,7,8,15,16,17,24,25,26]:
                cube, colorDisplay = self.magicCubeDisplay.cubes[i]
                cube.rotateLine(self.magicCubeDisplay.magicCubeCenter, tuple(center), -math.pi/20)
        elif action == 'L':
            center = self.magicCubeDisplay.cubes[12][0].center
            for i in [0,3,6,9,12,15,18,21,24]:
                cube, colorDisplay = self.magicCubeDisplay.cubes[i]
                cube.rotateLine(self.magicCubeDisplay.magicCubeCenter, tuple(center), -math.pi/20)
        elif action == 'R':
            center = self.magicCubeDisplay.cubes[14][0].center
            for i in [2,5,8,11,14,17,20,23,26]:
                cube, colorDisplay = self.magicCubeDisplay.cubes[i]
                cube.rotateLine(self.magicCubeDisplay.magicCubeCenter, tuple(center), -math.pi/20)
        elif action == 'U':
            center = self.magicCubeDisplay.cubes[22][0].center
            for i in [18,19,20,21,22,23,24,25,26]:
                cube, colorDisplay = self.magicCubeDisplay.cubes[i]
                cube.rotateLine(self.magicCubeDisplay.magicCubeCenter, tuple(center), -math.pi/20)
        elif action == 'D':
            center = self.magicCubeDisplay.cubes[4][0].center
            for i in [0,1,2,3,4,5,6,7,8]:
                cube, colorDisplay = self.magicCubeDisplay.cubes[i]
                cube.rotateLine(self.magicCubeDisplay.magicCubeCenter,tuple(center), -math.pi/20)

    def runSteps(self, steps, forever_run=False):
        running = True
        cnt = 0
        isAnimated = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in key_to_view:
                        key_to_view[event.key](self)
                        continue

            if cnt == 0 and isAnimated:
                step = steps.pop()

            if isAnimated:
                self.showAnimation(step)
                cnt += 1
            elif cnt == 0 and not forever_run:
                pygame.time.wait(1000)
                break

            if cnt == 10:
                cnt = 0
                if len(steps) == 0:
                    isAnimated = False

                tmpCubes = []
                for cube, colorDisplay in self.magicCubeDisplay.cubes:
                    tmpCubes.append([deepcopy(cube), deepcopy(colorDisplay)])
                for a, b in MagicCubeLogic.cube_proj_func[step]:
                    tmpCubes[b] = [deepcopy(self.magicCubeDisplay.cubes[a][0]),
                                    deepcopy(self.magicCubeDisplay.cubes[a][1])]
                self.magicCubeDisplay.cubes = tmpCubes

            self.display()
            pygame.display.flip()

    def run(self):
        """ Create a pygame screen until it is closed. """

        running = True
        cnt = 0
        isAnimated = False
        curAct = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in key_to_view:
                        key_to_view[event.key](self)
                    else:
                        isAnimated = True
                        curAct = key2act[event.key]

            if isAnimated:
                self.showAnimation(curAct)
                cnt += 1

            if cnt == 10:
                cnt = 0
                isAnimated = False

                tmpCubes = []
                for cube, colorDisplay in self.magicCubeDisplay.cubes:
                    tmpCubes.append([deepcopy(cube), deepcopy(colorDisplay)])
                for a, b in MagicCubeLogic.cube_proj_func[curAct]:
                    tmpCubes[b] = [deepcopy(self.magicCubeDisplay.cubes[a][0]),
                                    deepcopy(self.magicCubeDisplay.cubes[a][1])]
                self.magicCubeDisplay.cubes = tmpCubes

            self.display()
            pygame.display.flip()

    def display(self):
        """ Draw the wireframes on the screen. """

        self.screen.fill(self.background)

        avg_z = []
        for k in range(27):
            cube = self.magicCubeDisplay.cubes[k][0]
            for i, [n1, n2, n3, n4] in enumerate(cube.faces):
                z = (cube.nodes[n1][2]+cube.nodes[n2][2]+cube.nodes[n3][2]+cube.nodes[n4][2])/4.0
                avg_z.append([k,i,z])

        for i in range(len(avg_z)):
            for j in range(i+1,len(avg_z)):
                if avg_z[i][2] < avg_z[j][2]:
                    tmp = avg_z[i]
                    avg_z[i] = avg_z[j]
                    avg_z[j] = tmp

        for k, i, _ in avg_z:
            cube = self.magicCubeDisplay.cubes[k][0]
            colorShown = self.magicCubeDisplay.cubes[k][1][i]
            n1, n2, n3, n4 = self.magicCubeDisplay.cubes[k][0].faces[i]
            point_list = [(cube.nodes[n1][0], cube.nodes[n1][1]),
                          (cube.nodes[n2][0], cube.nodes[n2][1]),
                          (cube.nodes[n3][0], cube.nodes[n3][1]),
                          (cube.nodes[n4][0], cube.nodes[n4][1])]

            if colorShown:
                pygame.draw.polygon(self.screen, self.faceColours[i], point_list)
                pygame.draw.line(self.screen, self.edgeColour, (cube.nodes[n1][0], cube.nodes[n1][1]), (cube.nodes[n2][0], cube.nodes[n2][1]), 5)
                pygame.draw.line(self.screen, self.edgeColour, (cube.nodes[n2][0], cube.nodes[n2][1]), (cube.nodes[n3][0], cube.nodes[n3][1]), 5)
                pygame.draw.line(self.screen, self.edgeColour, (cube.nodes[n3][0], cube.nodes[n3][1]), (cube.nodes[n4][0], cube.nodes[n4][1]), 5)
                pygame.draw.line(self.screen, self.edgeColour, (cube.nodes[n4][0], cube.nodes[n4][1]), (cube.nodes[n1][0], cube.nodes[n1][1]), 5)

    def rotateAll(self, axis, theta):
        """ Rotate all cubes about their centre, along a given axis by a given angle. """

        rotateFunction = 'rotate' + axis

        for cube, colorDisplay in self.magicCubeDisplay.cubes:
            getattr(cube, rotateFunction)(self.magicCubeDisplay.magicCubeCenter, theta)


if __name__ == '__main__':
    pv = ProjectionViewer(600, 600)
    pv.run()
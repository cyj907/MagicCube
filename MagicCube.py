from Cube import Cube
import pygame
import math
from copy import deepcopy

key_to_function = {
    pygame.K_q:      (lambda x: x.rotateAll('X',  0.1 * math.pi)),
    pygame.K_w:      (lambda x: x.rotateAll('X', -0.1 * math.pi)),
    pygame.K_a:      (lambda x: x.rotateAll('Y',  0.1 * math.pi)),
    pygame.K_s:      (lambda x: x.rotateAll('Y', -0.1 * math.pi)),
    pygame.K_z:      (lambda x: x.rotateAll('Z',  0.1 * math.pi)),
    pygame.K_x:      (lambda x: x.rotateAll('Z', -0.1 * math.pi)),
    pygame.K_f:     (lambda x: x.showAnimation('F')),
    pygame.K_b:     (lambda x: x.showAnimation('B')),
    pygame.K_l:     (lambda x: x.showAnimation('L')),
    pygame.K_r:     (lambda x: x.showAnimation('R')),
    pygame.K_u:     (lambda x: x.showAnimation('U')),
    pygame.K_d:     (lambda x: x.showAnimation('D'))
}

class MagicCubeLogic:
    def __init__(self):
        self.ori_order = [i for i in range(27)]
        self.cur_order = [i for i in range(27)]

    def takeAction(self, action):
        if action == 'F':
            tmp = self.cur_order[20]
            self.cur_order[20] = self.cur_order[18]
            self.cur_order[18] = self.cur_order[0]
            self.cur_order[0] = self.cur_order[2]
            self.cur_order[2] = tmp

            tmp = self.cur_order[11]
            self.cur_order[11] = self.cur_order[19]
            self.cur_order[19] = self.cur_order[9]
            self.cur_order[9] = self.cur_order[1]
            self.cur_order[1] = tmp
        elif action == "F'":
            tmp = self.cur_order[18]
            self.cur_order[18] = self.cur_order[20]
            self.cur_order[20] = self.cur_order[2]
            self.cur_order[2] = self.cur_order[0]
            self.cur_order[0] = tmp

            tmp = self.cur_order[9]
            self.cur_order[9] = self.cur_order[19]
            self.cur_order[19] = self.cur_order[11]
            self.cur_order[11] = self.cur_order[1]
            self.cur_order[1] = tmp
        elif action == 'B':
            tmp = self.cur_order[6]
            self.cur_order[6] = self.cur_order[24]
            self.cur_order[24] = self.cur_order[26]
            self.cur_order[26] = self.cur_order[8]
            self.cur_order[8] = tmp

            tmp = self.cur_order[7]
            self.cur_order[7] = self.cur_order[15]
            self.cur_order[15] = self.cur_order[25]
            self.cur_order[25] = self.cur_order[17]
            self.cur_order[17] = tmp
        elif action == "B'":
            tmp = self.cur_order[26]
            self.cur_order[26] = self.cur_order[24]
            self.cur_order[24] = self.cur_order[6]
            self.cur_order[6] = self.cur_order[8]
            self.cur_order[8] = tmp

            tmp = self.cur_order[17]
            self.cur_order[17] = self.cur_order[25]
            self.cur_order[25] = self.cur_order[15]
            self.cur_order[15] = self.cur_order[7]
            self.cur_order[7] = tmp
        elif action == 'L':
            tmp = self.cur_order[18]
            self.cur_order[18] = self.cur_order[24]
            self.cur_order[24] = self.cur_order[6]
            self.cur_order[6] = self.cur_order[0]
            self.cur_order[0] = tmp

            tmp = self.cur_order[9]
            self.cur_order[9] = self.cur_order[21]
            self.cur_order[21] = self.cur_order[15]
            self.cur_order[15] = self.cur_order[3]
            self.cur_order[3] = tmp
        elif action == "L'":
            tmp = self.cur_order[6]
            self.cur_order[6] = self.cur_order[24]
            self.cur_order[24] = self.cur_order[18]
            self.cur_order[18] = self.cur_order[0]
            self.cur_order[0] = tmp

            tmp = self.cur_order[3]
            self.cur_order[3] = self.cur_order[15]
            self.cur_order[15] = self.cur_order[21]
            self.cur_order[21] = self.cur_order[9]
            self.cur_order[9] = tmp
        elif action == 'R':
            tmp = self.cur_order[8]
            self.cur_order[8] = self.cur_order[26]
            self.cur_order[26] = self.cur_order[20]
            self.cur_order[20] = self.cur_order[2]
            self.cur_order[2] = tmp

            tmp = self.cur_order[5]
            self.cur_order[5] = self.cur_order[17]
            self.cur_order[17] = self.cur_order[23]
            self.cur_order[23] = self.cur_order[11]
            self.cur_order[11] = tmp
        elif action == "R'":
            tmp = self.cur_order[20]
            self.cur_order[20] = self.cur_order[26]
            self.cur_order[26] = self.cur_order[8]
            self.cur_order[8] = self.cur_order[2]
            self.cur_order[2] = tmp

            tmp = self.cur_order[11]
            self.cur_order[11] = self.cur_order[23]
            self.cur_order[23] = self.cur_order[17]
            self.cur_order[17] = self.cur_order[5]
            self.cur_order[5] = tmp
        elif action == 'U':
            tmp = self.cur_order[26]
            self.cur_order[26] = self.cur_order[24]
            self.cur_order[24] = self.cur_order[18]
            self.cur_order[18] = self.cur_order[20]
            self.cur_order[20] = tmp

            tmp = self.cur_order[23]
            self.cur_order[23] = self.cur_order[25]
            self.cur_order[25] = self.cur_order[21]
            self.cur_order[21] = self.cur_order[19]
            self.cur_order[19] = tmp
        elif action == "U'":
            tmp = self.cur_order[24]
            self.cur_order[24] = self.cur_order[26]
            self.cur_order[26] = self.cur_order[20]
            self.cur_order[20] = self.cur_order[18]
            self.cur_order[18] = tmp

            tmp = self.cur_order[21]
            self.cur_order[21] = self.cur_order[25]
            self.cur_order[25] = self.cur_order[23]
            self.cur_order[23] = self.cur_order[19]
            self.cur_order[19] = tmp
        elif action == 'D':
            tmp = self.cur_order[6]
            self.cur_order[6] = self.cur_order[8]
            self.cur_order[8] = self.cur_order[2]
            self.cur_order[2] = self.cur_order[0]
            self.cur_order[0] = tmp

            tmp = self.cur_order[3]
            self.cur_order[3] = self.cur_order[7]
            self.cur_order[7] = self.cur_order[5]
            self.cur_order[5] = self.cur_order[1]
            self.cur_order[1] = tmp
        else:
            tmp = self.cur_order[8]
            self.cur_order[8] = self.cur_order[6]
            self.cur_order[6] = self.cur_order[0]
            self.cur_order[0] = self.cur_order[2]
            self.cur_order[2] = tmp

            tmp = self.cur_order[5]
            self.cur_order[5] = self.cur_order[7]
            self.cur_order[7] = self.cur_order[3]
            self.cur_order[3] = self.cur_order[1]
            self.cur_order[1] = tmp

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

        self.magicCubeLogic = MagicCubeLogic()
        self.isAnimated = False
        self.key = None

        self.alpha = 0
        self.beta = 0
        self.gamma = 0

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
        elif action == 'D':
            center = self.magicCubeDisplay.cubes[22][0].center
            for i in [18,19,20,21,22,23,24,25,26]:
                cube, colorDisplay = self.magicCubeDisplay.cubes[i]
                cube.rotateLine(self.magicCubeDisplay.magicCubeCenter, tuple(center), -math.pi/20)
        elif action == 'U':
            center = self.magicCubeDisplay.cubes[4][0].center
            for i in [0,1,2,3,4,5,6,7,8]:
                cube, colorDisplay = self.magicCubeDisplay.cubes[i]
                cube.rotateLine(self.magicCubeDisplay.magicCubeCenter,tuple(center), -math.pi/20)

    def run(self):
        """ Create a pygame screen until it is closed. """

        running = True
        cnt = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in key_to_function:
                        if event.key == pygame.K_f or \
                                event.key == pygame.K_b or \
                                event.key == pygame.K_l or \
                                event.key == pygame.K_r or \
                                event.key == pygame.K_u or \
                                event.key == pygame.K_d:
                            self.isAnimated = True
                            self.key = event.key

                            if event.key == pygame.K_f:
                                self.magicCubeLogic.takeAction('F')
                            elif event.key == pygame.K_b:
                                self.magicCubeLogic.takeAction('B')
                            elif event.key == pygame.K_l:
                                self.magicCubeLogic.takeAction('L')
                            elif event.key == pygame.K_r:
                                self.magicCubeLogic.takeAction('R')
                            elif event.key == pygame.K_u:
                                self.magicCubeLogic.takeAction('U')
                            else:
                                self.magicCubeLogic.takeAction('D')

                        else:
                            key_to_function[event.key](self)

            if self.isAnimated:
                key_to_function[self.key](self)
                cnt += 1

            if cnt == 10:
                cnt = 0
                self.isAnimated = False

            self.display()
            pygame.display.flip()

    def display(self):
        """ Draw the wireframes on the screen. """

        self.screen.fill(self.background)

        avg_z = []
        for id in range(27):
            k = self.magicCubeLogic.cur_order[id]
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
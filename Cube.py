import math
from copy import copy, deepcopy

class Cube:
    def __init__(self, (x,y,z), r):
        self.r = r
        self.x = x
        self.y = y
        self.z = z
        self.nodes = []
        self.edges = []
        self.faces = []
        self.center = [x,y,z]

        self.__add_nodes__()
        self.__add_edges__()
        self.__add_faces__()

    def __add_nodes__(self):
        # bottom four nodes (clockwise)
        self.nodes.append([self.x-self.r,self.y-self.r,self.z-self.r])
        self.nodes.append([self.x-self.r,self.y-self.r,self.z+self.r])
        self.nodes.append([self.x+self.r,self.y-self.r,self.z+self.r])
        self.nodes.append([self.x+self.r,self.y-self.r,self.z-self.r])

        # top four nodes (clockwise)
        self.nodes.append([self.x-self.r,self.y+self.r,self.z-self.r])
        self.nodes.append([self.x-self.r,self.y+self.r,self.z+self.r])
        self.nodes.append([self.x+self.r,self.y+self.r,self.z+self.r])
        self.nodes.append([self.x+self.r,self.y+self.r,self.z-self.r])

    def __add_edges__(self):
        # bottom four edges (clockwise)
        self.edges.append([3,0])
        self.edges.append([0,1])
        self.edges.append([1,2])
        self.edges.append([2,3])

        # middle four edges (clockwise)
        self.edges.append([0,4])
        self.edges.append([1,5])
        self.edges.append([2,6])
        self.edges.append([3,7])

        # top four edges (clockwise)
        self.edges.append([7,4])
        self.edges.append([4,5])
        self.edges.append([5,6])
        self.edges.append([6,7])

    def __add_faces__(self):
        # bottom (nodes arranged in counter clock wise order)
        self.faces.append([0,3,2,1])
        # front
        self.faces.append([0,4,7,3])
        # left
        self.faces.append([0,4,5,1])
        # back
        self.faces.append([1,2,6,5])
        # right
        self.faces.append([2,3,7,6])
        # top
        self.faces.append([4,5,6,7])

    def rotateX(self, (cx,cy,cz), radians):
        for i, [x, y, z] in enumerate(self.nodes):
            y      = y - cy
            z      = z - cz
            d      = math.hypot(y, z)
            theta  = math.atan2(y, z) + radians
            self.nodes[i][2] = cz + d * math.cos(theta)
            self.nodes[i][1] = cy + d * math.sin(theta)

        dy = self.center[1] - cy
        dz = self.center[2] - cz
        d = math.hypot(dy,dz)
        theta = math.atan2(dy,dz)+radians
        self.center[1] = cy + d * math.sin(theta)
        self.center[2] = cz + d * math.cos(theta)

    def rotateY(self, (cx,cy,cz), radians):
        for i, [x, y, z] in enumerate(self.nodes):
            x      = x - cx
            z      = z - cz
            d      = math.hypot(x, z)
            theta  = math.atan2(x, z) + radians
            self.nodes[i][2] = cz + d * math.cos(theta)
            self.nodes[i][0] = cx + d * math.sin(theta)

        dx = self.center[0] - cx
        dz = self.center[2] - cz
        d = math.hypot(dx, dz)
        theta = math.atan2(dx, dz) + radians
        self.center[0] = cx + d * math.sin(theta)
        self.center[2] = cz + d * math.cos(theta)

    def rotateZ(self, (cx,cy,cz), radians):
        for i, [x, y, z] in enumerate(self.nodes):
            x      = x - cx
            y      = y - cy
            d      = math.hypot(y, x)
            theta  = math.atan2(y, x) + radians
            self.nodes[i][0] = cx + d * math.cos(theta)
            self.nodes[i][1] = cy + d * math.sin(theta)

        dx = self.center[0] - cx
        dy = self.center[1] - cy
        d = math.hypot(dy, dx)
        theta = math.atan2(dy,dx)+radians
        self.center[0] = cx + d * math.cos(theta)
        self.center[1] = cy + d * math.sin(theta)

    def rotateLine(self, (a,b,c), (d,e,f), radians):
        u = d - a
        v = e - b
        w = f - c
        L = u*u + v*v + w*w
        for i, [x, y, z] in enumerate(self.nodes):
            self.nodes[i][0] = (a*(v*v+w*w)-u*(b*v+c*w-u*x-v*y-w*z))*(1-math.cos(radians))+L*x*math.cos(radians)+\
                math.sqrt(L)*(-c*v+b*w-w*y+v*z)*math.sin(radians)
            self.nodes[i][0] /= L

            self.nodes[i][1] = (b*(u*u+w*w)-v*(a*u+c*w-u*x-v*y-w*z))*(1-math.cos(radians))+L*y*math.cos(radians)+\
                math.sqrt(L)*(c*u-a*w+w*x-u*z)*math.sin(radians)
            self.nodes[i][1] /= L

            self.nodes[i][2] = (c*(u*u+v*v)-w*(a*u+b*v-u*x-v*y-w*z))*(1-math.cos(radians))+L*z*math.cos(radians)+\
                math.sqrt(L)*(-b*u+a*v-v*x+u*y)*math.sin(radians)
            self.nodes[i][2] /= L

    def __deepcopy__(self, memo):
        obj = copy(self)
        obj.nodes = []
        for node in self.nodes:
            obj.nodes.append(deepcopy(node))

        obj.edges = []
        for edge in self.edges:
            obj.edges.append(deepcopy(edge))

        obj.faces = []
        for face in self.faces:
            obj.faces.append(deepcopy(face))

        obj.center = deepcopy(self.center, memo)
        return obj








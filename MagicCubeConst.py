faces = {"F": [0,1,2,9,10,11,18,19,20],
         "B": [6,7,8,15,16,17,24,25,26],
         "L": [0,3,6,9,12,15,18,21,24],
         "R": [2,5,8,11,14,17,20,23,26],
         "U": [18,19,20,21,22,23,24,25,26],
         "D": [0,1,2,3,4,5,6,7,8]}
faceCenters = {"F":10,"B":16,"L":12,"R":14,"U":22,"D":4}
# top, front, left, back, right, bottom
colors = [(255,255,255),(255,0,0),(0,255,0),(245,143,22),(0,0,255),(245,227,22)]
availActions = ['F', "F'", 'B', "B'", 'L', "L'", 'R', "R'", 'U', "U'", 'D', "D'"]

cube_proj_func = {}
cube_proj_func["F"] = [(18,20),(19,11),(20,2),(9,19),(0,18),(1,9),(11,1),(2,0)]
cube_proj_func["F'"] = [(20,18),(19,9),(18,0),(11,19),(2,20),(1,11),(0,2),(9,1)]
cube_proj_func['B'] = [(24,6),(15,7),(6,8),(8,26),(7,17),(25,15),(26,24),(17,25)]
cube_proj_func["B'"] = [(24,26),(25,17),(26,8),(17,7),(8,6),(7,15),(6,24),(15,25)]
cube_proj_func['L'] = [(24,18),(21,9),(18,0),(9,3),(0,6),(3,15),(6,24),(15,21)]
cube_proj_func["L'"] = [(24,6),(15,3),(6,0),(3,9),(0,18),(9,21),(18,24),(21,15)]
cube_proj_func['R'] = [(26,8),(17,5),(8,2),(5,11),(2,20),(11,23),(20,26),(23,17)]
cube_proj_func["R'"] = [(26,20),(23,11),(20,2),(11,5),(2,8),(5,17),(8,26),(17,23)]
cube_proj_func['U'] = [(24,26),(25,23),(26,20),(23,19),(20,18),(19,21),(18,24),(21,25)]
cube_proj_func["U'"] = [(26,24),(25,21),(24,18),(21,19),(18,20),(19,23),(20,26),(23,25)]
cube_proj_func['D'] = [(8,6),(7,3),(6,0),(3,1),(0,2),(1,5),(2,8),(5,7)]
cube_proj_func["D'"] = [(6,8),(7,5),(8,2),(5,1),(2,0),(1,3),(0,6),(3,7)]

face_proj_func = {}
face_proj_func["F"] = {"F":"F","U":"R","L":"U","B":"B","D":"L","R":"D"}
face_proj_func["F'"] = {"F":"F","U":"L","L":"D","D":"R","R":"U","B":"B"}
face_proj_func["B"] = {"R":"U","U":"L","F":"F","L":"D","D":"R","B":"B"}
face_proj_func["B'"] = {"L":"U","U":"R","F":"F","R":"D","D":"L","B":"B"}
face_proj_func["L"] = {"U":"F","F":"D","L":"L","R":"R","D":"B","B":"U"}
face_proj_func["L'"] = {"F":"U","U":"B","B":"D","D":"F","L":"L","R":"R"}
face_proj_func["R"] = {"F":"U","U":"B","B":"D","D":"F","L":"L","R":"R"}
face_proj_func["R'"] = {"U":"F","F":"D","D":"B","B":"U","L":"L","R":"R"}
face_proj_func["U"] = {"U":"U","D":"D","F":"L","L":"B","B":"R","R":"F"}
face_proj_func["U'"] = {"U":"U","D":"D","F":"R","R":"B","B":"L","L":"F"}
face_proj_func["D"] = {"U":"U","D":"D","F":"R","R":"B","B":"L","L":"F"}
face_proj_func["D'"] = {"U":"U","D":"D","F":"L","L":"B","B":"R","R":"F"}

faces2Indices = {"U":0,"F":1,"L":2,"B":3,"R":4,"D":5}
indices2Faces = ["U","F","L","B","R","D"]

edgeCubeIndices = [1,3,5,7,9,11,15,17,19,21,23,25]
cornCubeIndices = [0,2,6,8,18,20,24,26]

cube_visible_faces = [
    [False,True,True,False,False,True],
    [False,True,False,False,False,True],
    [False,True,False,False,True,True],
    [False,False,True,False,False,True],
    [False,False,False,False,False,True],
    [False,False,False,False,True,True],
    [False,False,True,True,False,True],
    [False,False,False,True,False,True],
    [False,False,False,True,True,True],

    [False,True,True,False,False,False],
    [False,True,False,False,False,False],
    [False,True,False,False,True,False],
    [False,False,True,False,False,False],
    [False,False,False,False,False,False],
    [False,False,False,False,True,False],
    [False,False,True,True,False,False],
    [False,False,False,True,False,False],
    [False,False,False,True,True,False],

    [True,True,True,False,False,False],
    [True,True,False,False,False,False],
    [True,True,False,False,True,False],
    [True,False,True,False,False,False],
    [True,False,False,False,False,False],
    [True,False,False,False,True,False],
    [True,False,True,True,False,False],
    [True,False,False,True,False,False],
    [True,False,False,True,True,False],
]

pair_orients = {
    "F": "F'",
    "B": "B'",
    "L": "L'",
    "R": "R'",
    "U": "U'",
    "D": "D'",
    "F'": "F",
    "B'": "B",
    "L'": "L",
    "R'": "R",
    "U'": "U",
    "D'": "D"
}

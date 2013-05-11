from pyplasm import *
import scipy
from scipy import *
from larpy import *

"""ASSI"""
X=1
Y=2
Z=3

"""Funzione che trasla tutti i punti di un array della quantita indicata lungo il rispettivo asse."""
def pointTranslation(points, dx, dy, dz):
    newPoints = []
    for item in points:
        newItem = []
        newItem.append(item[0]+dx)
        newItem.append(item[1]+dy)
        newItem.append(item[2]+dz)
        newPoints.append(newItem)
    return newPoints


"""Funzione che accetta un array di curve di bezier e le interpola con una superficie"""
def bezierSurfaceInterpolator(curve):
    domain2 = DOMAIN_GRID([36,36])
    #domain2 = DOMAIN([[0,1],[0,1]])([36,36])
    result = None
    for item in curve:
        mappingFunc = BEZIER(S2)(item)
        surface = MAP(mappingFunc)(domain2)
        if result is None:
            result = surface
        else:
            result = STRUCT([result,surface])
    return result

"""Funzione che accetta come fattori di scala solo valori positivi, maggiori di 1 per ingrandire
e minori di 1 per rimpicciolire. Con valori negativi ribalta la figura sul quadrante opposto"""
def getScaledObject(scaleFactor, obj):
    obj = S([X,Y,Z])([scaleFactor,scaleFactor,scaleFactor])(obj)
    return obj

"""Funzione che crea una mezza sfera. Prende come parametri il raggio, il numero di "paralleli", e il colore."""
def drawCup(r,n,color):
    domain = DOMAIN([[0,1.1*PI],[0,2*PI]])([n,2*n])
    def mapping(p):
        u = p[0]
        v = p[1]
        return [r*COS(u)*COS(v),r*COS(u)*SIN(v),r*SIN(u)]
    cup = MAP(mapping)(domain)
    return COLOR(color)(cup)

"""Funzione che dato un punto avvicina tutti i punti di controllo dell'array controlPoints al punto dato"""
def controlPointsReducer(point, controlPoints):
    result = []
    for item in controlPoints:
        xpos = (point[0]+item[0])/2
        ypos = (point[1]+item[1])/2
        result.append([xpos,ypos,0])
    return result


"""Funzione che dato un array di punti li moltiplica tutti per un fattore di scala"""
def pointScale(controlPoints,scaleFactor):
    result = []
    for item in controlPoints:
        xpos = item[0]*scaleFactor
        ypos = item[1]*scaleFactor
        zpos = item[2]*scaleFactor
        result.append([xpos,ypos,zpos])
    return result

"""Funzione che ruota tutti i punti di un array, dell'angolo indicato, sull'asse indicato."""
def pointRotation(points, degree, axis):
    result = []
    rm = None
    if axis == X:
        rm = [[1,0,0],[0,COS(degree),-SIN(degree)],[0,SIN(degree),COS(degree)]]
    if axis==Y:
        rm = [[COS(degree),0,SIN(degree)],[0,1,0],[-SIN(degree),0,COS(degree)]]
    if axis==Z:
        rm = [[COS(degree),-SIN(degree),0],[SIN(degree),COS(degree),0],[0,0,1]]
    for item in points:
        result.append(prodottoMatVect(rm,item))
    return result 


"""Funzione che fa il prodotto tra una matrice e un vettore."""
def prodottoMatVect(mat, vect):
    result = []
    for item in mat:
        result.append(item[0]*vect[0]+item[1]*vect[1]+item[2]*vect[2])
    return result

"""Funzione per generare una griglia di complessi simpliciali. Necessita della libreria lar"""
def DOMAIN_GRID(args):
    model = ([[]],[[0]])
    for k,steps in enumerate(args):
        model = lar.larExtrude(model,steps*[1])
    V,cells = model
    verts = AA(list)(scipy.array(V)/AA(float)(args))
    return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])

def EXTRUDE(h):
    h0 = h[0]
    def EXTRUDE0(model):
        return PROD([model,Q(h0)])
    return EXTRUDE0

def DOMAIN(limits):
    def DOMAIN0(intervals):
        result = []
        for item in limits:
            int1 = INTERVALS(item[0])(intervals[limits.index(item)])
            int2 = INTERVALS(item[1])(intervals[limits.index(item)])
            result.append(DIFFERENCE([int2,int1]))
        return PROD(result)
    return DOMAIN0


def controlPointsAdjusterXY(controls):
    result = []
    for item in controls:
        item[0]=float(item[0])/100
        item[1]=float(item[1])/100
        item[1]=-item[1]
        item.append(0)
        result.append(item)
    return result

def controlPointsAdjusterZ(controls,z_value):
    result = []
    for item in controls:
        item[2]=z_value
        result.append(item)
    return result

def controlPointsAdjusterXZ(controls):
    result = []
    for item in controls:
        item[0]=float(item[0])/100
        item[1]=float(item[1])/100
        item.append(item[1])
        item[1]=0
        result.append(item)
    return result

def controlPointsAdjusterYZ(controls):
    result = []
    for item in controls:
        item[0]=float(item[0])/100
        item[1]=float(item[1])/100
        item[1]=-item[1]
        item.append(item[0])
        item[0]=0
        result.append(item)
    return result


def drawBezierCurve(controls,axis):
    domain1D = INTERVALS(1)(36)
    if(axis=="XY"):
        controlPoints = controlPointsAdjusterXY(controls)
    if(axis=="XZ"):
        controlPoints = controlPointsAdjusterXZ(controls)
    if(axis=="YZ"):
        controlPoints = controlPointsAdjusterYZ(controls)
    controlLine = POLYLINE(controlPoints)
    mapCurv = BEZIER(S1)(controlPoints)
    curve = MAP(mapCurv)(domain1D)
    #curve = STRUCT([curve, controlLine])
    return curve

def drawBezierCurveSimple(mapFun):
    domain1D = INTERVALS(1)(36)
    curve = MAP(mapFun)(domain1D)
    #curve = STRUCT([curve, controlLine])
    return curve

def bezierCurveMappings(controls,axis):
    if(axis=="XY"):
        controlPoints = controlPointsAdjusterXY(controls)
    if(axis=="XZ"):
        controlPoints = controlPointsAdjusterXZ(controls)
    if(axis=="YZ"):
        controlPoints = controlPointsAdjusterYZ(controls)
    mapCurv = BEZIER(S1)(controlPoints)
    return mapCurv
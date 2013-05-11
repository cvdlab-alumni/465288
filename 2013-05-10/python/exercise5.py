from pyplasm import *

"""CODICE UTILE"""
from funzioni_utili_auto import *
"""CODICE UTILE"""

"""ASSI"""
X=1
Y=2
Z=3

"""DOMINI"""
domain1D = INTERVALS(1)(36)
domain2D = DOMAIN_GRID([36,36])

"""MISURE"""
#MISURE RUOTA
raggioCopertone = 3
spessoreCopertone = 0.7
raggioCerchione = 2.7
spessoreCerchione = 2.2
larghezzaCerchione = 0.6
raggioCentroRuota = 1
spessoreCentroRuota = spessoreCerchione
spessoreRaggio = float(spessoreCentroRuota)/3
larghezzaRaggio = 0.6
lunghezzaRaggio = (raggioCerchione-larghezzaCerchione)
numRaggi = 6
raggioPerno = float(raggioCentroRuota)/2
spessorePerno =  0.2
lunghezzaComponentePerno = float(lunghezzaRaggio)/1.5
larghezzaComponentePerno = float(larghezzaRaggio)/3
spessoreComponentePerno = spessorePerno
numComponentiPerno = 3

#MISURE VOLANTE

"""MISURE"""


"""RUOTA"""
"""COPERTONE"""
domainCopertone = DOMAIN([[(1.2)*PI, (2.8)*PI],[0,2*PI]])([36,36]);
def mappingCopertone(v):
    alfa = v[0]
    beta = v[1]
    return [(spessoreCopertone*COS(alfa)+raggioCopertone)*COS(beta), (spessoreCopertone*COS(alfa)+raggioCopertone)*SIN(beta),spessoreCopertone*SIN(alfa)]

copertone = MAP(mappingCopertone)(domainCopertone)
copertone = COLOR(BLACK)(T([Z])([spessoreCopertone-0.1])(copertone))
copertone = S([Z])([1.8])(copertone)
#DRAW(copertone)
"""COPERTONE"""


"""CERCHIONE"""
def draw_arc(r1, r2, alpha):
  domainArc = DOMAIN([[0,alpha], [r1,r2]])([36,1])
  def mappingArc(v):
    angle = v[0];
    radius = v[1];
    return [radius*COS(angle), radius*SIN(angle)];
  return MAP(mappingArc)(domainArc);

arc = draw_arc(raggioCerchione-larghezzaCerchione,raggioCerchione,2*PI)
cerchione = EXTRUDE([spessoreCerchione])(arc)

"""RAGGI"""
centroRuota = CYLINDER([raggioCentroRuota, spessoreCentroRuota])(36) 
centroRuota = COLOR(RED)(centroRuota)
raggio = CUBOID([larghezzaRaggio,lunghezzaRaggio,spessoreRaggio])
raggio = T([X,Z])([-float(larghezzaRaggio)/2,0.05])(raggio)
raggi = raggio
raggi = STRUCT(NN(numRaggi)([raggi, R([X,Y])(2*PI/6)]))
raggi = COLOR(RED)(raggi)
"""RAGGI"""

cerchione = STRUCT([cerchione, centroRuota, raggi])
#DRAW(cerchione)
"""CERCHIONE"""

perno = CYLINDER([raggioPerno, spessorePerno])(36)

componentePerno = CUBOID([larghezzaComponentePerno,lunghezzaComponentePerno,spessoreComponentePerno])
componentePerno = T([X])([-float(larghezzaComponentePerno)/2])(componentePerno)
componentiPerno = componentePerno
componentiPerno = STRUCT(NN(numComponentiPerno)([componentiPerno, R([X,Y])(2*PI/3)]))
componentiPerno = R([X,Y])(2*PI/12)(componentiPerno)
perno = STRUCT([perno, componentiPerno])
perno = T([Z])([-spessorePerno])(perno)
ruota = STRUCT([copertone, cerchione, perno])
"""RUOTA"""

#VIEW(ruota)



"""VOLANTE"""
#MISURE VOLANTE
spessoreVolante = 0.3
raggioVolante = 3
raggioCentroVolante = 0.8
spessoreCentroVolante = spessoreVolante

domainVolante = DOMAIN([[0, 2*PI],[0,2*PI]])([36,36]);
def mappingVolante(v):
    alfa = v[0]
    beta = v[1]
    return [(spessoreVolante*COS(alfa)+raggioVolante)*COS(beta), (spessoreVolante*COS(alfa)+raggioVolante)*SIN(beta),spessoreVolante*SIN(alfa)]

contornoVolante = MAP(mappingVolante)(domainVolante)
contornoVolante = COLOR(BLACK)(T([Z])([spessoreVolante-0.1])(contornoVolante))
#VIEW(contornoVolante)

centroVolante = CYLINDER([raggioCentroVolante, spessoreCentroVolante])(36) 
centroVolante = T([Y,Z])([0.3,-0.4])(centroVolante)

controlli11 = [[213,189],[217,193],[237,193],[241,188]]
controlli11 = controlPointsAdjusterXY(controlli11)
controlLine = POLYLINE(controlli11)
mapCurv1 = BEZIER(S1)(controlli11)
curve11 = MAP(mapCurv1)(domain1D)
#VIEW(curve11)

controlli12 = [[220,271],[223,272],[230,272],[233,271]]
controlli12 = controlPointsAdjusterXY(controlli12)
controlli12 = controlPointsAdjusterZ(controlli12,0.15)
controlLine = POLYLINE(controlli12)
mapCurv2 = BEZIER(S1)(controlli12)
curve12 = MAP(mapCurv2)(domain1D)
#VIEW(curve12)

curve = STRUCT([curve11,curve12])
#VIEW(curve)

componenteVolante1 = bezierSurfaceInterpolator([[mapCurv1,mapCurv2]])
#componenteVolante = STRUCT([componenteVolante, curve])
componenteVolante1 = getScaledObject(2.5,componenteVolante1)
componenteVolante1 = T([X,Y])([-5.7,4.8])(componenteVolante1)
#VIEW(componenteVolante)

componenteVolante2 = R([X,Y])(PI/1.8)(componenteVolante1)
componenteVolante3 = R([X,Y])(-PI/1.8)(componenteVolante1)
componentiVolante = STRUCT([componenteVolante1,componenteVolante2,componenteVolante3])

componentiVolante = getScaledObject(1.5, componentiVolante)
componentiVolante = T([Y,Z])([0.2,-0.3])(componentiVolante)
volante = STRUCT([centroVolante,contornoVolante,componentiVolante])
#VIEW(volante)

volante = R([X,Z])(-PI/2)(volante)
volante = getScaledObject(0.15, volante)
volante = T([X,Y,Z])([3.5,1,0.5])(volante)
"""VOLANTE"""

"""SUPERFICI"""

"""PORTIERA"""
controlli1_portiera = [[370,152],[373,59],[396,67],[469,19]]
cur11S = drawBezierCurve(controlli1_portiera, "XY")
#VIEW(cur11S)

controlli2_portiera = [[469,19],[593,21]]
cur12S = drawBezierCurve(controlli2_portiera, "XY")
#VIEW(cur12S)

controlli3_portiera = [[593,21],[560,152]]
cur13S = drawBezierCurve(controlli3_portiera, "XY")
#VIEW(cur13S)

controlli4_portiera = [[560,152],[370,152]]
cur14S = drawBezierCurve(controlli4_portiera, "XY")
#VIEW(cur14S)

controlli5_portiera = [[389,79],[383,83],[374,135],[377,147]]
mapcur15S = bezierCurveMappings(controlli5_portiera, "XY")
cur15S = drawBezierCurveSimple(mapcur15S)

controlli6_portiera = [[578,77],[561,147]]
mapcur16S = bezierCurveMappings(controlli6_portiera, "XY")
cur16S = drawBezierCurveSimple(mapcur16S)


profilo_portiera1 = STRUCT([cur11S,cur12S,cur13S,cur14S])
profilo_portiera2 = STRUCT([cur15S,cur16S])
portiera1 = OFFSET([0.1,0.1,0.1])(profilo_portiera1)
portiera2 = bezierSurfaceInterpolator([[mapcur15S,mapcur16S]])
#portiera2 = EXTRUDE([0.1])(portiera2) Non ci sono riuscito...
portiera2 = T([Z])([0.1])(portiera2)

portiera = COLOR(BLUE)(STRUCT([portiera1, portiera2]))

controlli7_portiera = [[471,600],[464,502],[475,500],[498,501]]
mapcur17S = bezierCurveMappings(controlli7_portiera, "XZ")
cur17S = drawBezierCurveSimple(mapcur17S)

controlli8_portiera = [[594,600],[591,564],[563,495],[527,498]]
mapcur18S = bezierCurveMappings(controlli8_portiera, "XZ")
cur18S = drawBezierCurveSimple(mapcur18S)

portiera3 = bezierSurfaceInterpolator([[mapcur17S,mapcur18S]])
portiera3 = T([Y,Z])([-0.09,-5.9])(portiera3)

portiera = COLOR(BLUE)(STRUCT([portiera, portiera3]))
portiera = T([X,Y])([-4,2])(portiera)
#VIEW(portiera)

"""PORTIERA"""

"""COFANO"""
controlli1_cofano = [[106,394],[241,390]]
mapcur11S = bezierCurveMappings(controlli1_cofano, "XZ")
cur11S = drawBezierCurveSimple(mapcur11S)

cofano1 = OFFSET([0,0,0.1])(cur11S)
cofano2 = T([Z])([1.7])(cofano1)

controlli2_cofano = [[240,401],[240,560]]
mapcur12S = bezierCurveMappings(controlli2_cofano, "XZ")
cur12S = drawBezierCurveSimple(mapcur12S)

controlli3_cofano = pointTranslation(controlli2_cofano, -1.23, 0, 0)
mapcur13S = BEZIER(S1)(controlli3_cofano)
cur13S = drawBezierCurveSimple(mapcur13S)

controlli4_cofano = pointTranslation(controlli2_cofano, -1.23, -0.25, 0)
mapcur14S = BEZIER(S1)(controlli4_cofano)
cur14S = drawBezierCurveSimple(mapcur14S)
 
cofano3 = bezierSurfaceInterpolator([[mapcur12S,mapcur13S,mapcur14S]])

controlli5_portiera = [[87,394],[56,393],[60,574],[87,574]]
mapcur15S = bezierCurveMappings(controlli5_portiera, "XZ")
cur15S = drawBezierCurveSimple(mapcur15S)

controlli6_portiera = [[106,394],[106,574]]
mapcur16S = bezierCurveMappings(controlli6_portiera, "XZ")
cur16S = drawBezierCurveSimple(mapcur16S)

cofano4 = bezierSurfaceInterpolator([[mapcur15S,mapcur16S]])

cofano = COLOR(BLACK)(STRUCT([cofano1,cofano2,cofano3,cofano4]))
#VIEW(cofano)
"""COFANO"""


"""SUPERFICI"""


"""=========================================================================================================="""


"""PROFILO SX"""
"""PROFILO SUPERIORE SX"""
controlli1_curvaSup_profiloSx = [[18,150],[102,101],[165,59],[335,77]]
cur11S = drawBezierCurve(controlli1_curvaSup_profiloSx, "XY")
#VIEW(cur11S)

controlli2_curvaSup_profiloSx = [[335,77],[400,17],[470,2],[509,7]]
cur12S = drawBezierCurve(controlli2_curvaSup_profiloSx, "XY")
#VIEW(cur12S)

controlli3_curvaSup_profiloSx = [[509,7],[576,5],[718,37],[746,48]]
cur13S = drawBezierCurve(controlli3_curvaSup_profiloSx, "XY")
#VIEW(cur13S)

controlli4_curvaSup_profiloSx = [[746,48],[776,40],[860,75],[890,76]]
cur14S = drawBezierCurve(controlli4_curvaSup_profiloSx, "XY")
#VIEW(cur14S)

controlli5_curvaSup_profiloSx = [[890,76],[898,78],[912,74],[918,63]]
cur15S = drawBezierCurve(controlli5_curvaSup_profiloSx, "XY")
#VIEW(cur15S)
"""PROFILO SUPERIORE SX"""

"""PROFILO INFERIORE SX"""
controlli1_curvaInf_profiloSx = [[18,150],[47,222],[78,206],[147,209]]
cur11I = drawBezierCurve(controlli1_curvaInf_profiloSx, "XY")
#VIEW(cur11I)

controlli2_curvaInf_profiloSx = [[147,209],[137,75],[322,29],[327,206]]
cur22I = drawBezierCurve(controlli2_curvaInf_profiloSx, "XY")
#VIEW(cur22I)

controlli3_curvaInf_profiloSx = [[327,206],[680,207]]
cur33I = drawBezierCurve(controlli3_curvaInf_profiloSx, "XY")
#VIEW(cur33I)

controlli4_curvaInf_profiloSx = [[680,207],[652,59],[864,50],[850,180]]
cur44I = drawBezierCurve(controlli4_curvaInf_profiloSx, "XY")
#VIEW(cur44I)

controlli5_curvaInf_profiloSx = [[850,180],[883,184],[934,50],[918,63]]
cur55I = drawBezierCurve(controlli5_curvaInf_profiloSx, "XY")
#VIEW(cur55I)
"""PROFILO INFERIORE SX"""

profilo_SupSx = STRUCT([cur11S,cur12S,cur13S,cur14S,cur15S])
profilo_InfSx = STRUCT([cur11I,cur22I,cur33I,cur44I,cur55I])
profiloSx = STRUCT([profilo_SupSx,profilo_InfSx])
profiloSx = T([X,Y,Z])([-0.18,2,1.8])(profiloSx)
#VIEW(profiloSx)
"""PROFILO SX"""
profiloDx = T([Z])([-3.5])(profiloSx)
"""PROFILO DX"""



"""PROFILO TETTO"""
controlli1_curvaSup_tetto = [[18,475],[7,341],[74,304],[200,292]]
cur11S = drawBezierCurve(controlli1_curvaSup_tetto, "XZ")
#VIEW(cur11S)

controlli2_curvaSup_tetto = [[200,292],[246,279],[555,311],[602,302]]
cur12S = drawBezierCurve(controlli2_curvaSup_tetto, "XZ")
#VIEW(cur12S)

controlli3_curvaSup_tetto = [[602,302],[620,281],[625,297],[656,290]]
cur13S = drawBezierCurve(controlli3_curvaSup_tetto, "XZ")
#VIEW(cur13S)

controlli4_curvaSup_tetto = [[656,290],[770,257],[824,270],[876,304]]
cur14S = drawBezierCurve(controlli4_curvaSup_tetto, "XZ")
#VIEW(cur14S)

controlli5_curvaSup_tetto = [[876,304],[922,328],[916,327],[915,351]]
cur15S = drawBezierCurve(controlli5_curvaSup_tetto, "XZ")
#VIEW(cur15S)

controlli6_curvaSup_tetto = [[915,351],[915,475]]
cur16S = drawBezierCurve(controlli6_curvaSup_tetto, "XZ")
#VIEW(cur16S)

profilo_Sup = STRUCT([cur11S,cur12S,cur13S,cur14S,cur15S,cur16S])
profilo_Sup = T([Z])([-4.75])(profilo_Sup)
profilo_Inf = R([Y,Z])(PI)(profilo_Sup)
profiloTetto = STRUCT([profilo_Sup,profilo_Inf])
profiloTetto = T([Y])([2])(profiloTetto)
#VIEW(profiloTetto)
"""PROFILO TETTO"""

"""PROFILO FRONTALE"""
controlli1_curvaDx_frontale = [[1157,8],[1069,7],[1040,2],[997,48]]
cur11S = drawBezierCurve(controlli1_curvaDx_frontale, "YZ")
#VIEW(cur11S)

controlli2_curvaDx_frontale = [[997,48],[967,48],[952,64],[951,84]]
cur12S = drawBezierCurve(controlli2_curvaDx_frontale, "YZ")
#VIEW(cur12S)

controlli3_curvaDx_frontale = [[951,84],[950,89],[969,154],[983,170]]
cur13S = drawBezierCurve(controlli3_curvaDx_frontale, "YZ")
#VIEW(cur13S)

controlli4_curvaDx_frontale = [[983,170],[1010,210],[1027,214],[1157,213]]
cur14S = drawBezierCurve(controlli4_curvaDx_frontale, "YZ")
#VIEW(cur14S)


profilo_Dx = STRUCT([cur11S,cur12S,cur13S,cur14S])
profilo_Dx = T([Z])([-11.57])(profilo_Dx)
profilo_Sx = R([X,Z])(PI)(profilo_Dx)
profiloFronte = STRUCT([profilo_Dx,profilo_Sx])
profiloFronte = T([Y])([2.13])(profiloFronte)
#VIEW(profiloFronte)
"""PROFILO FRONTALE"""

"""PROFILO POSTERIORE"""
controlli1_curvaDx_posteriore = [[1157,257],[1084,257],[1030,255],[1002,301]]
cur11S = drawBezierCurve(controlli1_curvaDx_posteriore, "YZ")
#VIEW(cur11S)

controlli2_curvaDx_posteriore = [[1002,301],[976,296],[943,313],[954,357]]
cur12S = drawBezierCurve(controlli2_curvaDx_posteriore, "YZ")
#VIEW(cur12S)

controlli3_curvaDx_posteriore = [[954,357],[979,442],[987,436],[1157,435]]
cur13S = drawBezierCurve(controlli3_curvaDx_posteriore, "YZ")
#VIEW(cur13S)

profilo_Dx = STRUCT([cur11S,cur12S,cur13S])
profilo_Dx = T([Y,Z])([2.57,-11.57])(profilo_Dx)
profilo_Sx = R([X,Z])(PI)(profilo_Dx)
profiloPosteriore = STRUCT([profilo_Dx,profilo_Sx])
profiloPosteriore = T([X,Y])([9,2])(profiloPosteriore)
#VIEW(profiloPosteriore)
"""PROFILO POSTERIORE"""

profili2D = STRUCT([profiloSx,profiloDx,profiloTetto,profiloFronte,profiloPosteriore])
#VIEW(profili2D)


ruota = getScaledObject(0.23, ruota)
ruotaDx = R([Y,Z])(PI)(ruota)
ruotaDx = T([X,Y,Z])([2.2,0.2,1.9])(ruotaDx)
routeDx = STRUCT([ruotaDx, T([X])(5.3)(ruotaDx)])
ruotaSx = T([X,Y,Z])([2.2,0.2,-1.8])(ruota)
routeSx = STRUCT([ruotaSx, T([X])(5.3)(ruotaSx)])

portiera = T([X,Z])([3.5,1.8])(portiera)
cofano = T([Y,Z])([2,-4.7])(cofano)

modello = STRUCT([profili2D, routeSx,routeDx,volante,portiera,cofano])
VIEW(modello)

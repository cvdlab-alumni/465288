from pyplasm import *
import scipy
from scipy import *
from larpy import *

"""CODICE UTILE"""
from funzioni_utili import *
"""CODICE UTILE"""

DRAW = VIEW

"""ASSI"""
X=1
Y=2
Z=3

"""DOMINI"""
domain1D = INTERVALS(1)(36)
domain2D = DOMAIN_GRID([36,36])


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
VIEW(profili2D)


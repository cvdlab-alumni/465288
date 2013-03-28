//Base
var prato = COLOR([0.2,0.4,0.05])(SIMPLEX_GRID([[16],[0.1],[16]]));
var pavimento = SIMPLEX_GRID([[6],[0.1],[6]]);
//Muri
var muro_retro = COLOR([0.7,0.7,0.72])(SIMPLEX_GRID([[6],[4],[0.1]]));
var muro_laterale_sx = COLOR([0.7,0.7,0.72])(SIMPLEX_GRID([[0.1],[4],[6]]));
var muro_laterale_dx = T([0])([5.9])(muro_laterale_sx);
var muro_fronte = T([2])([6])(muro_retro);
//Porta e Finestra
var porta = CUBOID([1,2.5,0.01]);
porta = COLOR([92/255,51/255,23/255,1])(porta);
var maniglia = COLOR([0.7,0.7,0.72])(DISK(0.03)());
maniglia = EXTRUDE([0.05])(maniglia);
maniglia = T([0,1,2])([0.85,1.25,0.1])(maniglia);
porta = STRUCT([porta, maniglia]);
var cornice_porta = COLOR([0,0,0])(CUBOID([1.4,2.7,0.1]));
porta = T([0,2])([0.2,0.1])(porta);
porta = STRUCT([porta, cornice_porta]);
porta = T([0,2])([1.5,6.01])(porta);
var finestra = CUBOID([1,1.5,0.1]);
finestra = COLOR([0,0.8,1])(finestra);
var cornice_finestra = COLOR([0,0,0])(CUBOID([1.2,1.7,0.1]));
finestra = T([0,1,2])([0.1,0.1,0.01])(finestra);
finestra = STRUCT([finestra, cornice_finestra]);
finestra = T([0,1,2])([4,1,6.01])(finestra);
//Tetto
var vertici_tetto = [[0,4],[3,6],[6,4]];
var celle_tetto = [[0,1,2]];
var tetto = COLOR([0.6,0.05,0])(SIMPLICIAL_COMPLEX(vertici_tetto)(celle_tetto));
tetto = EXTRUDE([6.1])(tetto)
var comignolo = CUBOID([0.5,1.2,0.5]);
comignolo = T([0,1,2])([4.5,4.5,3.5])(comignolo);
tetto = STRUCT([tetto, comignolo]);
//Casa
var casa = STRUCT([pavimento,muro_fronte,muro_laterale_sx,muro_laterale_dx,muro_retro,porta,finestra,tetto]);
casa = T([0,1,2])([5,0.1,5])(casa);
DRAW(prato);
DRAW(casa);


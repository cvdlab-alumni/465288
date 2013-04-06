//========================== UTILITIES ============================================================

T = function (dims) {
	dims = dims.map(function(item){
		return item-1;
	});
	return function (values) {
		return function (object) {
			return object.clone().translate(dims,values);
		};
	};
}

S = function (dims) {
	dims = dims.map(function(item){
		return item-1;
	});
    return function (values) {
      return function (object) {
        return object.clone().scale(dims, values);
      };
    };
  }

 R = function (dims) {
 	dims = dims.map(function(item){
		return item-1;
	});
    return function (angle) {
      return function (object) {
        return object.clone().rotate(dims, angle);
      };
    };
  }

  S3 = S2;
  S2 = S1;
  S1 = S0;

  GRID = SIMPLEX_GRID

  VIEW = DRAW
//===================================================================================================

/*******************************************/
/****************ESERCIZIO 1****************/
/*******************************************/

/****************PIANO TERRA****************/

//Pilastro circolare
var circPill = EXTRUDE([2.45])(DISK(0.125)(36));
var circPill_firstRow_0 = T([1])([0.125])(circPill);

//Pilastro rettangolare
var squarePill = EXTRUDE([2.45])(CUBOID([0.25,0.25]));
squarePill = T([2])([-0.125])(squarePill);

//Blocchi di raccordo
var circJunction = EXTRUDE([0.25])(DISK(0.125)(36));
circJunction = T([1])([0.125])(circPill);
var squareJunction = EXTRUDE([0.25])(CUBOID([0.25,0.25]));
squareJunction = T([2])([-0.125])(squareJunction);

//Pilastri esterni, prima riga
var traslation = T([1])([2.75]);
var external_pillars_0 = STRUCT(REPLICA(5)([circPill_firstRow_0, traslation]));
var external_junctions_0 = STRUCT(REPLICA(5)([T([3])([-0.25])(circJunction), traslation]));
external_pillars_0 = STRUCT([external_pillars_0,external_junctions_0]);

//Pilastri interni, seconda riga
//Cilindrici
var circPill_secondRow_0 = T([2])([5.25])(circPill_firstRow_0);
//Cuboidi
var squarePill_secondRow_0 = T([1])([2.75])(squarePill);
squarePill_secondRow_0 = T([2])([5.25])(squarePill_secondRow_0);
internal_pillars_0 = STRUCT([circPill_secondRow_0, STRUCT(REPLICA(3)([squarePill_secondRow_0,traslation]))]);

var pillars0 = STRUCT([external_pillars_0,internal_pillars_0]);



/****************PRIMO PIANO****************/

var squarePill_short = EXTRUDE([2.25])(CUBOID([0.25,0.25]));
squarePill_short = T([2])([-0.125])(squarePill_short);
var circPill_short = EXTRUDE([2.25])(DISK(0.125)(36));
circPill_short = T([1])([0.125])(circPill_short);

//Pilastri esterni, prima riga, primo piano
var squarePill_firstRow_1 = T([3])([2.70])(squarePill_short);
var external_pillars_1 = STRUCT(REPLICA(5)([squarePill_firstRow_1, traslation]));

//Pilastri interni, seconda riga, primo piano
var squarePill_secondRow_1 = T([2])([5.25])(squarePill_firstRow_1);
var internal_pillars_1 = STRUCT(REPLICA(3)([squarePill_secondRow_1, traslation]));
var lastSquarePill_secondRow_1 = T([1])([11])(squarePill_secondRow_1);
//L'unico pilastro cilindrico
var third_circPill_secondoRow_1 = T([1,2,3])([8.25,5.25,2.70])(circPill_short);
internal_pillars_1 = STRUCT([internal_pillars_1, third_circPill_secondoRow_1, lastSquarePill_secondRow_1]);
//Aggiungo i raccordi per col secondo piano
var squareJunction_firstRow_1 = T([3])([5.20-0.25])(squareJunction);
var external_Junction_firstRow_1 = STRUCT(REPLICA(3)([squareJunction_firstRow_1, traslation]));
var squareJunction_secondRow_1 = T([1,2,3])([2.75,5.25,5.20-0.25])(squareJunction);

var pillars1 = STRUCT([internal_pillars_1,external_pillars_1,external_Junction_firstRow_1,squareJunction_secondRow_1]);



/****************SECONDO PIANO****************/

//Pilastri interni, prima riga, secondo piano
var squarePill_firstRow_2 = T([3])([5.20])(squarePill_short);
var external_pillars_2 = STRUCT(REPLICA(3)([squarePill_firstRow_2, traslation]));
var lastSquarePill_firstRow_2 = T([1])([11])(squarePill_firstRow_2);
var external_pillars_2 = STRUCT([external_pillars_2, lastSquarePill_firstRow_2]);

//Pilastri esterni, seconda riga, secondo piano
var squarePill_secondRow_2 = T([2,3])([5.25, 5.20])(squarePill_short);
var internal_pillars_2 = STRUCT(REPLICA(5)([squarePill_secondRow_2, traslation]));

//Aggiungo i raccordi per col terzo piano
var squareJunction_firstRow_2 = T([1,3])([5.5,7.70-0.25])(squareJunction);

var pillars2 = STRUCT([external_pillars_2,internal_pillars_2,squareJunction_firstRow_2]);



/****************TERZO PIANO****************/

//Definisco il pilastro rettangolare per l'ultimo piano (più basso)
var squarePill_3 = EXTRUDE([2.30])(CUBOID([0.25,0.25]));
squarePill_3 = T([2])([-0.125])(squarePill_3);
var squarePill_small_3 = EXTRUDE([2.30])(CUBOID([0.125,0.125]));
squarePill_small_3 = T([2])([-0.125])(squarePill_small_3);

//Pilastri esterni, prima riga
var squarePill1_firstRow_3 = T([1,3])([5.5,7.70])(squarePill_3);
var squarePill2_firstRow_3 = T([1])([5.5])(squarePill1_firstRow_3);
var external_pillars_3 = STRUCT([squarePill1_firstRow_3,squarePill2_firstRow_3]);

//Pilastri interni, seconda riga
//pilastri piccoli
var squarePill1_small_secondRow_3 = T([2,3])([5.375,7.70])(squarePill_small_3);
var squarePill2_small_secondRow_3 = T([1])([2.75])(squarePill1_small_secondRow_3);
var squarePills_small_secondRow_3 = STRUCT([squarePill1_small_secondRow_3,squarePill2_small_secondRow_3]);
//pilastri grandi
var squarePill_secondRow_3 = T([1,2,3])([5.5,5.25,7.70])(squarePill_3);
var internal_pillars_3 = STRUCT(REPLICA(3)([squarePill_secondRow_3, traslation]));
internal_pillars_3 = STRUCT([internal_pillars_3, squarePills_small_secondRow_3]);

var pillars3 = STRUCT([external_pillars_3,internal_pillars_3]);


//Struttura dei pilastri
var building = STRUCT([pillars0, pillars1, pillars2, pillars3]);
VIEW(building); 

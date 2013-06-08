//ASSI
var X=0;
var Y=1;
var Z=2;

//COLORI
var nero = [0,0,0];
var neroChiaro = [0.2,0.2,0.2];
var grigioChiaro = [0.85,0.85,0.85];
var azzurroVetro = [0,0.8,1,0.8];
var azzurroVetroContachilometri = [0,0.8,1,0.4];
var rosso = [1,0,0];
var bianco = [1,1,1];
var arancio = [1,0.6,0];
var rossoScuro = [0.8,0,0];
var marrone = [159/255,80/255,19/255];

var verdeAcqua = [0/255,204/255,153/255,0.85];
var verdeErba = [102/255,205/255,0/255];

//MISURE
var groundDimension = 30;

//DOMINI
var domain2D = DOMAIN([[0,groundDimension],[0,groundDimension]])([20,20]);

//DRAW(SKELETON(1)(domain2D));

function Float32Concat(first, second)
{
    var firstLength = first.length;
    var result = new Float32Array(firstLength + second.length);

    result.set(first);
    result.set(second, firstLength);

    return result;
}

function mappingHeights(v){
  var array = new Array();
  array.push(0);
  v = Float32Concat(v, array);
  return v;
}


function getRandomHeights(domain){
  var result;
  mapp = function(v){
    if(v[0]===0 || v[1]===0 || v[0]===groundDimension || v[1]==groundDimension){
       //v[2]=Math.floor((Math.random())+1);
       return v;
    }
    if(v[0]<(groundDimension/4)){
      v[2]=Math.floor((Math.random()*3)+1);
    }

    if(v[0]>=(groundDimension/5) && v[0]<(groundDimension/2.5)){
      v[2]=Math.random()+0.08;
    }

    if(v[0]>=(groundDimension/2.5) && v[1]<(groundDimension/2.5)){
        v[2]=Math.floor((Math.random()*3)+1);
    }

    if(v[1]>(groundDimension/10) && v[1]<(groundDimension/3.75) && v[0]>(groundDimension/2) && v[0]<(groundDimension/1.07)){
        v[2]=0.3;
    } 

    if(v[0]>=(groundDimension/2.5) && v[1]>(groundDimension/(1.5))){
      v[2]=Math.random()+0.08;
    }

    return v;
  }
  result = MAP(mapp)(domain);
  return result;
}

domain2D = MAP(mappingHeights)(domain2D);

var mountains = getRandomHeights(domain2D);


DRAW(COLOR(marrone)(mountains));

var lake = CUBOID([11,4,0.5]);
lake = T([X,Y])([16.5,4])(lake);
lake = COLOR(verdeAcqua)(lake);
DRAW(lake);

var lowland = CUBOID([groundDimension/1.7,groundDimension/2,0.07]);
lowland = T([X,Y])([groundDimension/2.5, groundDimension/2.5])(lowland);
lowland = COLOR(verdeErba)(lowland);
DRAW(lowland);

/*Funzione che accetta come fattori di scala solo valori positivi, maggiori di 1 per ingrandire
e minori di 1 per rimpicciolire. Con valori negativi ribalta la figura sul quadrante opposto*/
function getScaledObject(scaleFactor, obj){
  obj = S([X,Y,Z])([scaleFactor,scaleFactor,scaleFactor])(obj);
  return obj;
}

function CYLINDER(dim){
  function CYLINDER0(intervals){
    var cylinder = DISK(dim[0])(intervals);
    cylinder = EXTRUDE([dim[1]])(cylinder);
    return cylinder;
  }
  return CYLINDER0;
}


function createTree(radius, height, ang_dis){
  var domain = DOMAIN([[0,1],[0,2*PI]])([ang_dis,ang_dis]);
  var profile = BEZIER(S0)([[radius,0,0],[0,0,(2/3)*height]]);
  var mapping = ROTATIONAL_SURFACE(profile);
  var foliage = MAP(mapping)(domain);
  var base = DISK(radius)(ang_dis);
  foliage = STRUCT([foliage,base]);
  var trunk = CYLINDER([(1/4)*radius, (1/3)*height])(36);
  trunk = T([Z])([-(1/3)*height])(trunk);
  tree = STRUCT([COLOR(verdeErba)(foliage),COLOR(marrone)(trunk)]);
  tree = T([Z])([(1/3)*height])(tree);
  return tree;
}

var tree = createTree(3, 10, 20);
tree = getScaledObject(0.05,tree);
//DRAW(tree);

function createForest(mountains, tree){
    var x;
    var y;
    var z;
    mappForest = function(v){
      if(v[0]===0 || v[1]===0 || v[0]===groundDimension || v[1]==groundDimension){
       return v;
      }
      if(v[0]>=(groundDimension/5) && v[0]<(groundDimension/2.5)){
        x = v[0];
        y = v[1];
        z = v[2];
        DRAW(T([X,Y,Z])([x,y,z])(tree));
      }
      // if(v[0]>=(groundDimension/2.5) && v[1]<(groundDimension/5)){
      //   x = v[0];
      //   y = v[1];
      //   z = v[2];
      //   DRAW(T([X,Y,Z])([x,y,z])(tree));
      // }
      if(v[0]>=(groundDimension/2.5) && v[1]>(groundDimension/(1.5))){
        x = v[0];
        y = v[1];
        z = v[2];
        DRAW(T([X,Y,Z])([x,y,z])(tree));
      }
      return v;
    }
  MAP(mappForest)(mountains);
}

createForest(mountains, tree);

function createBuilding(height, width, lenght){
  return CUBOID([lenght,height,width]);
}

function createSettlement(rows, cols){
  var settlement = null;
  var xdistance = 0;
  var zdistance = 0;
  for(r=0;r<rows;r++){
    var settlementRow=null;
    for(c=0;c<cols;c++){
      var lenght = Math.floor((Math.random()*3)+1);
      var width = Math.floor((Math.random()*3)+1);
      var height = Math.floor((Math.random()*4)+1);
      var building = createBuilding(height, width, lenght);
      if(settlementRow===null){
        settlementRow=building;
      }
      else{
        xdistance = xdistance +4;
        building = T([X])([xdistance])(building);
        settlementRow = STRUCT([settlementRow, building]);  
      } 
    }
    xdistance = 0;
    if(settlement===null){
        settlement=settlementRow;
    }
    else{
      zdistance = zdistance + 4;
      settlementRow = T([Z])([zdistance])(settlementRow);
      settlement = STRUCT([settlement, settlementRow]); 
    } 
  }
  return settlement;
}

var settlement1 = createSettlement(7,5);
settlement1 = R([Y,Z])([PI/2])(settlement1);
settlement1 = getScaledObject(0.2,settlement1);
settlement1 = T([X,Y,Z])([14,18.5,0.07])(settlement1);
DRAW(settlement1)

var settlement2 = createSettlement(7,5);
settlement2 = R([Y,Z])([PI/2])(settlement2);
settlement2 = getScaledObject(0.2,settlement2);
settlement2 = T([X,Y,Z])([25,18.5,0.07])(settlement2);
DRAW(settlement2)
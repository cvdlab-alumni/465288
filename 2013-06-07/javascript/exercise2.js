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

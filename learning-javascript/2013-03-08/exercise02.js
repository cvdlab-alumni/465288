var array = []
function pushToArray(n){
	for(var c=1; c<=n; c++){
		var randNum = Math.round(Math.random(100)*100);
		array.push(randNum);
	}
	array = array.filter(function(item){return(item%2===1)});
	array.sort(mySortFunction);
}

function mySortFunction(value1, value2){	//ordina dal più piccolo al più grande
	return value1 - value2;
}
function convertToObj(v,fv){
	debugger;
	var result ='';
	v.forEach(function(item){
		if (item[2]===undefined)
			result+='v '+' '+item[0]+' '+item[1]+' 0 \n';
		else
			result+='v '+' '+item[0]+' '+item[1]+' '+item[2]+'\n';
    });

	fv.forEach(function(item){
		var len = item.length;
		item.forEach(function(item0, index){
			if(index===0){
				result += 'f '+item0+' ';	
			} else if(index===len-1) {
				result += item0+'\n';
			} else {
				result += item0+' ';
			}
		});
    });
	return result;
}

fv = [[5,6,7,8],
[0,5,8],
[0,4,5],
[1,2,4,5],
[2,3,5,6],
[0,8,7], [3,6,7], [1,2,3], [0,1,4]
];
v = [[0,6],
[0,0],
[3,0],
[6,0,4],
[0,3,4],
[3,3],
[6,3],
[6,6],
[3,6]];

convertToObj(v,fv);
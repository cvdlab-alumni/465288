var n = '';
for (var r=1; r<11; r++) {
	for(var c=1; c<11; c++){
		if(c<10){
			n += r*c + ',\t';	
		}else{
			n += r*c;	
		}
	}
	console.log(n);
	n='';
}

console.log('\n');
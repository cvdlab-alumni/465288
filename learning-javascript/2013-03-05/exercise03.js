var n = '';
for (var r=1; r<11; r++) {
	for(var c=1; c<11; c++){
		if(c<10){
			if(c===r){
				n += 1 + ',\t';	
			}else{
				n += 0 + ',\t';	
			}
		}else{
			if(c===r){
				n += 1;	
			}else{
				n += 0;	
			}
		}
			}
	console.log(n);
	n='';
}

alert("Guarda la console");
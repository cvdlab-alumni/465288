function identity(n){
	var s = '';
	for (var r=0; r<n; r++) {
		for(var c=0; c<n; c++){
			if(c===r){
				s += 1 + '\t';	
			}else{
				s += 0 + '\t';	
			}
		}
		console.log(s);
		s='';
	}
}
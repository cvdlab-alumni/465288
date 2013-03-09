function fibonacci(i){
	var c;
	for(c=3; c<=i; c++){
		fibonacci[c]=fibonacci[c-1]+fibonacci[c-2];
	}
	return fibonacci[i];
}

fibonacci[1]=0;
fibonacci[2]=1;
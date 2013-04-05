function draw_arc(r, R, alpha){
	var domain = DOMAIN([[0,alpha], [r,R]])([36,1])
	var mapping = function(v){
		var angle = v[0];
		var radius = v[1];
		return [radius*COS(angle), radius*SIN(angle)];
	}
	return MAP(mapping)(domain);
}
function Point2D(x, y){
	this.x = x;
	this.y = y;
}

var p1 = new Point2D(3,4);
var p2 = new Point2D(5,4);

function Edge(a,b){
	this.a = a;
	this.b = b;
	this.lenght = function(){
		var dx = this.a.x - this.b.x;
		var dy = this.a.y - this.b.y;
		return Math.sqrt(Math.pow(dx,2)+Math.pow(dy,2));
	}
}

edge = new Edge(p1,p2);



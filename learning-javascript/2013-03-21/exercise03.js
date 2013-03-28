function Point2D(x, y){
	this.x = x;
	this.y = y;
}

var point1 = new Point2D(3,4);
var point2 = new Point2D(5,4);
var point3 = new Point2D(4,6);

function Edge(p1,p2){
	this.p1 = p1;
	this.p2 = p2;
	this.lenght = function(){
		var dx = this.p1.x - this.p2.x;
		var dy = this.p1.y - this.p2.y;
		return Math.sqrt(Math.pow(dx,2)+Math.pow(dy,2));
	}
}

edge1 = new Edge(point1,point2);
edge2 = new Edge(point1,point3);
edge3 = new Edge(point2,point3);

function Triangle(e1,e2,e3){
	this.e1 = e1;
	this.e2 = e2;
	this.e3 = e3;
	this.perimeter = function(){
		var l1 = this.e1.lenght();
		var l2 = this.e2.lenght();
		var l3 = this.e3.lenght();
		return l1+l2+l3;
	}
	this.area = function(){
		var l1 = this.e1.lenght();
		var l2 = this.e2.lenght();
		var l3 = this.e3.lenght();
		var p = this.perimeter()/2;
		var area = Math.sqrt(p*(p-l1)*(p-l2)*(p-l3));
		return area;
	}
}

triangle = new Triangle(edge1, edge2, edge3);
function drawArc(alpha,intervalli,r){
  var domain = DOMAIN([[0,alpha]])([intervalli]);
  var circle = function(r){
    return function(v){
      return [r*COS(v[0]),r*SIN(v[0])];
    };
  };
  var mapping = circle(r);
  return MAP(mapping)(domain);
}
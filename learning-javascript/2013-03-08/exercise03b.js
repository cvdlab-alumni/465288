var	array = [];
function capitalizer(){
	var str = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
	array = str.split(' ');
	array = array.map(function(item){
		if(item.indexOf(",")>-1)
			item = item.slice(0, item.indexOf(","));
		if(item.indexOf(".")>-1)
			item = item.slice(0, item.indexOf("."));
		return item;
	});
}
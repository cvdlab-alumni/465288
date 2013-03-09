var data = [
  {id:'01', name:'duffy'},
  {id:'02', name:'michey'},
  {id:'03', name:'donald'},
  {id:'04', name:'goofy'},
  {id:'05', name:'minnie'},
  {id:'06', name:'scrooge'}
];
var key = 'name';
var result = [];
var valori = ['goofy', 'scrooge'];

function select(data, key, valori){
	data.forEach(function(item){
		valori.forEach(function(value){
			if(item[key]===value)
			result.push(item);
		});
	});
}
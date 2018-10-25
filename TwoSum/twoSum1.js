let twoSum = function(x, y) {
	let len=x.length
	while(x.length>1){
		for(i=1;i<x.length;i++){
			if (x[0]+x[i]===y)return [len-x.length,i+len-x.length]
		}
		x.splice(0,1)
	}
	return 0
}
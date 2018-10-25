let twoSum = function (x, y) {
	let i=0
	let complement
	let iC
	for(;i<x.length;i++){
		complement=y-x[i]
		 if( (iC=x.indexOf(complement,i+1)) !=-1){
		 	return[i,iC]
		 }
	}
}
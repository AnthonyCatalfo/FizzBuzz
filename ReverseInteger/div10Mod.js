
let reverse = function(num) {
    let y=1
    if (num<0){
			y=-1
			num=-num
		} 
		let i=0
		let test=0
        let result=0
		let arr=[]
		let digit 
		let exp=1
    while(num>0){
			digit=num % 10
			num =Math.floor(num/10)
			arr.unshift(digit)
		//	console.log(arr) 
		}
    for (;i<arr.length;i++){
			result += arr[i]* Math.pow(10,i)
		//	console.log(result,arr[i],Math.pow(10,i))
		}
         let r = y*result
    if( r > 2147483647 || r < -2147483648)
        return 0
    else 
        return r  
};
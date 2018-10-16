let fizzBuzz=(n)=>{
    let result=[]
    let i=0
	for( i=1;i<n;i++){
		switch(i){
			case i% 15===0 && i:
				result.push('FizzBuzz')
				break;
			case i% 3===0 && i:
				result.push('Fizz')
				break;
			case i% 5===0 && i:
				result.push('Buzz')
				break;
			default:
				result.push(i.toString())
				
		}
	}
}

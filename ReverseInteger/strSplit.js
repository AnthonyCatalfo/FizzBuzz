var reverse = function(x) {
    let y=1
    if (x<0) y=-1 
    let str=x.toString()
    str.split(",")
    let result=[]
    
    for(let i=str.length-1;i>-1;i--){
        result.push(str[i])
    }
        let r = y*parseInt(result.join(""))+0.0
    if( r > 2147483647 || r < -2147483648)
        return 0
    else 
        return r 
        
};
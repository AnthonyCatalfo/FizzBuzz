from fractions import Fraction 

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b): 
    if(b==0):
        return 1000000
    return Fraction(a,b)

def tf(numbers):
    e = [add, sub, mult, div]
    solutions=[]
    results=[]
    for i in e:
        for j in e:
            for k in e:
                    
                    lM=k(j(numbers[0],i(numbers[1],numbers[2])),numbers[3])
                    lL=k(j(i(numbers[0], numbers[1]),numbers[2]),numbers[3])
                    rR=k(numbers[0],j(numbers[1],i(numbers[2],numbers[3])))
                    rM=k(numbers[0],j(i(numbers[1],numbers[2]),numbers[3]))
                    split= k(i(numbers[0], numbers[1]),j(numbers[2], numbers[3]))
                   
                    
                    if(lM==24):
                        lMStr='('+ str(numbers[0])+' '+j.__name__+'('+ str(numbers[1])+' '+i.__name__+' '+      str(numbers[2])+'))'+' '+k.__name__+' '+str(numbers[3])+' lM'
                        solutions.append(lMStr)
                    if(lL==24):
                        lLStr='(('+ str(numbers[0])+' '+i.__name__+' '+str(numbers[1]) +')'+j.__name__+' '+      str(numbers[2])+')'+' '+k.__name__+' '+str(numbers[3])+' lL'
                        solutions.append(lLStr)
                    if(rR==24):
                        rRStr=str(numbers[0])+' '+ k.__name__ +'('+ str(numbers[1])+' '+j.__name__+'('+str(numbers[2])+' '+i.__name__ +' '+str(numbers[3])+'))'+' rR'
                        solutions.append(rRStr) 
                    if(rM==24):
                        rMStr=str(numbers[0])+' '+ k.__name__ +'(('+str(numbers[1])+' '+i.__name__+' '+str(numbers[2])+')'+ j.__name__+' '+str(numbers[3])+')'+' rM'
                        solutions.append(rMStr)
                    if(split==24):
                        splitStr='('+str(numbers[0])+' '+i.__name__+' '+str(numbers[1])+')'+k.__name__+'('+str(numbers[2])+' '+j.__name__+' '+str(numbers[3])+')'+' split'
                        solutions.append(splitStr)
                       
                                 
                    
           
    
    return solutions



def tfh(numbers):
    unique=[]
    
    for i in range(len(numbers)):
        for j in range(len(numbers)): 
            if (j==i):
                continue
            for k in range(len(numbers)):
                if (k==i or k==j):
                    continue
                for l in range(len(numbers)):
                    if (l==i or l==j or l==k):
                        continue
                    unique.append([numbers[i], numbers[j], numbers[k], numbers[l]])
    
    unique.sort()
    te=[]
    for x in range(len(unique)-1):
        if(unique[x]!= unique[x+1]):
            te.append(tf(unique[x]))
        if(x==len(unique)-2):
            te.append(tf(unique[x+1]))    
            
    for elm in te:
        if(elm !=[]):
            for item in elm:
                print(item)
            
tfh([8, 8, 3, 3])
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b): 
    return a / b

def tf(numbers):
    e = [add, sub, mult, div]
    solutions=[]
    results=[]
    for i in e:
        for j in e:
            for k in e:
                    temp= i(j(k(numbers[0], numbers[1]), numbers[2]), numbers[3])
                    if(temp==24):
                        solutions.append([numbers[0], k.__name__, numbers[1],
                            j.__name__, numbers[2],i.__name__, numbers[3]])
                    
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
    for x in range(len(unique)-1):
        if(unique[x]!= unique[x+1]):
            te=tf(unique[x])
            if(te !=[]):
                print (te)


tfh([2, 3, 6, 6])
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b): 
    if(b==0):
        return 1000000
    return a / b

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
                    revS=i(k(numbers[0], numbers[1]),j(numbers[2], numbers[3]))
                    
                    
                    if(lM==24):
                        #solutions.append([numbers,i.__name__,j.__name__,k.__name__,'lM'])
                        solutions.append([k.__name__,'(',j.__name__,'(', numbers[0],i.__name__,'(',numbers[1]
                            , numbers[2],'))',numbers[3],'lM'])
                    if(lL==24):
                        solutions.append([numbers,i.__name__,j.__name__,k.__name__,'lL'])
                        #print(numbers,i,j,k)
                        #solutions.append([i.__name__,k.__name__,numbers[0],numbers[1],
                             #j.__name__,numbers[2], numbers[3],'lL'])
                        
                    if(rR==24):
                        solutions.append([numbers,i.__name__,j.__name__,k.__name__,'rR'])
                        #solutions.append([i.__name__,k.__name__,numbers[0],numbers[1],
                             #j.__name__,numbers[2], numbers[3],'rR'])   
                    if(rM==24):
                        solutions.append([numbers,i.__name__,j.__name__,k.__name__,'rM'])
                        #solutions.append([numbers[0], j.__name__, numbers[1],
                            #k.__name__, numbers[2],i.__name__, numbers[3],'rM'])
                    if(split==24):
                        solutions.append([numbers,i.__name__,j.__name__,k.__name__,'split'])
                        #solutions.append([numbers[0], j.__name__, numbers[1],
                            #i.__name__, numbers[2],k.__name__, numbers[3],'split'])
                    if(revS==24):
                        solutions.append([numbers,i.__name__,j.__name__,k.__name__,'revS'])
                        #solutions.append([numbers[0], i.__name__, numbers[1],
                            #k.__name__, numbers[2],j.__name__, numbers[3],'revS'])
                    
    print(len(solutions))
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
    for x in range(len(unique)-1):
        if(unique[x]!= unique[x+1]):
            te=tf(unique[x])
            if(te !=[]):
                print (te)


tfh([5, 5, 9, 4])



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
                        #solutions.append([numbers,i.__name__,j.__name__,k.__name__,'lM'])
                        lMStr='('+ str(numbers[0])+' '+j.__name__+'('+ str(numbers[1])+' '+i.__name__+' '+      str(numbers[2])+'))'+' '+k.__name__+' '+str(numbers[3])+' lM'
                        solutions.append(lMStr)
                    if(lL==24):
                        #solutions.append([numbers,i.__name__,j.__name__,k.__name__,'lL'])
                        #print(numbers,i,j,k)
                        lLStr='(('+ str(numbers[0])+' '+i.__name__+' '+str(numbers[1]) +')'+j.__name__+' '+      str(numbers[2])+')'+' '+k.__name__+' '+str(numbers[3])+' lL'
                        solutions.append(lLStr)
                    if(rR==24):
                        solutions.append([numbers,i.__name__,j.__name__,k.__name__,'rR'])
                        #solutions.append([i.__name__,k.__name__,numbers[0],numbers[1],
                             #j.__name__,numbers[2], numbers[3],'rR'])   
                    if(rM==24):
                        solutions.append([numbers,i.__name__,j.__name__,k.__name__,'rM'])
                        #solutions.append([numbers[0], j.__name__, numbers[1],
                            #k.__name__, numbers[2],i.__name__, numbers[3],'rM'])
                    if(split==24):
                        solutions.append([numbers,i.__name__,j.__name__,k.__name__,'split'])
                        #solutions.append([numbers[0], j.__name__, numbers[1],
                            #i.__name__, numbers[2],k.__name__, numbers[3],'split'])
                    
                                 
                    
           
    print(len(solutions))
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
    for x in range(len(unique)-1):
        if(unique[x]!= unique[x+1]):
            te=tf(unique[x])
            if(te !=[]):
                for elm in te:
                    print(elm)
                #print (te)


tfh([3, 3, 8, 8])
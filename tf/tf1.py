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
    e = [0, 1, 2, 3]
    unique=[]
    for i in e:
        for j in e:
            for k in e:
                for l in e:  
                    if (i != j and i != k and i != l and j != k and j != l and k != l ):
                        unique.append([numbers[i], numbers[j], numbers[k], numbers[l]])
    unique.sort()
    for x in range(len(unique)-1):
        if(unique[x]!= unique[x+1]):
            te=tf(unique[x])
            if(te !=[]):
                print (te)


tfh([2, 3, 6, 6])
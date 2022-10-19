
rjesenje = {}

def histogram(brojevi,intervali):
    
    for x in range(len(intervali)-1):
        t1=x
        t2=x+1
        for t in brojevi:
           if t>=intervali[t1] and t<intervali[t2]:
            if((intervali[t1],intervali[t2]) in rjesenje):
                rjesenje[(intervali[t1],intervali[t2])] = rjesenje.get((intervali[t1],intervali[t2]))+1
            else:
                rjesenje[(intervali[t1],intervali[t2])] = 1


histogram([1,2,3,2,4,3,5,4,6,1,2,5,3],[0,2,4,7])

print(rjesenje)
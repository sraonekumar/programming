# hello
def rotate(l,r,d = 0):
    if(r > len(l)):
        while(r > len(l)):
            r = r% len(l)
    if r ==0:
        return l
    else:
        if(d == 0):
            temp = list(l[r:])
            temp.extend(l[:r])
            return(temp)
        else:
            temp = list(l[:r])
            temp.extend(l[r:])
            return(temp)
            
        
l = [1,2,3,4,5]
print(l)
print("left rotate:" ,rotate(l,10,0)) # d = -1 -- >right
print("right rotate:",rotate(l,10,-1)) # d = 0 --> left


    
    
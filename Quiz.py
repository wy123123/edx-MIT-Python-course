
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


def primesList(N):
    '''
    N: an integer
    '''
    # Your code here
    l = []
    if N==2:
        return [2]
    else:
        for i in range(2,N+1):
            prime = True
            for d in range (2,i+1):
                if i%d == 0 and i != d:
                    prime = False
                    break
            if prime == True:
                l = l+[i]
    return l
            

def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N/10 == 0:
        if N%10 == 7:
            return 1
        else:
            return 0
    else:
        if N%10 ==7:
            return count7(N/10)+1
        else:
            return count7(N/10)
    

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    l =[]
    for i in aDict.keys():
        count = 0
        for s in aDict.values():
            if aDict[i]==s:
                count += 1
        if count == 1:
            l = l+[i]
    return sorted(l)

def satisfiesF(L):

   count= len(L)
   rec_list=list()

   for i in range(0,count):
     if(f(L[i])==False):
        rec_list.append(L[i])   

   if(rec_list):
     for j in rec_list:
      L.remove(j)



   return len(L)
run_satisfiesF(L, satisfiesF) 

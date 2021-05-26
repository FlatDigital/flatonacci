def flatonacci(signature: list, n: int) -> list:
    if len(signature) == 3 and n > 0:
        pos1, pos2, pos3 = signature[-3], signature[-2], signature[-1]
        count = 0        
        newlist = []
        while count < n:               
            newlist.append(pos1) 
            plus = pos1 + pos2 + pos3            
            pos1 = pos2
            pos2 = pos3
            pos3 = plus            
            count += 1                         
        return newlist
    elif  n == 0:
        return list()
    else:
        return "must be a list of 3 values and n must be a non-negative number"
    pass

#signature = list(input("tell me the signature list"))
#n = int(input("give me a n elements"))

signature = [3,2,1]
n = 11

#return
print(flatonacci(signature, n)) 
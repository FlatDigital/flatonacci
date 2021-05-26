def flatonacci(signature: list, n: int) -> list:
    if len(signature) == 3 and n > 0:
        pos1, pos2, pos3 = signature[-1], signature[-2], signature[-3]
        count = 0        
        while count < n:           
            plus = pos1 + pos2 + pos3            
            pos1 = pos2
            pos2 = pos3
            pos3 = plus
            count += 1  
            print(pos1)
    elif  n == 0:
        return list()
    else:
        return "must be a list of 3 values and n must be a non-negative number"
    pass

#signature = list(input("tell me the signature list"))
#n = int(input("give me a n elements"))

signature = [1,1,1]
n = 8

#return
print(flatonacci(signature, n)) 
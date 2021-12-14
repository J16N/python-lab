from math import sqrt

def get_prop_div(num):
    divisors = [1]
    for i in range(2, int(sqrt(num) + 1)):
        if (num % i == 0):
            divisors.append(i)
            divisors.append(num / i)
    return divisors 

def classify(start, end):
    for i in range(start, end + 1):
        divisors = get_prop_div(i)
        
        if (sum(divisors) > i):
            print("Abundant:", i)
            
        elif (sum(divisors) < i):
            print("Deficient:", i)
            
        else:
            print("Perfect:", i)
            

classify(1, 10000)

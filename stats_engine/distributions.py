import numpy as np

def _factorial(n : int) -> float:
    if(n==0):
        return 1.0
    return float(np.prod(np.arange(1, n+1, dtype=np.float64)))

def _combination(n : int, r : int) -> float:
    if (r<0 or r>n):
        return 0.0
    elif(r ==0 or r == n):
        return 1
    k=min(n,n-r)
    numerator=np.prod(np.arange(n-k+1,n+1, dtype=np.float64))
    denominator=np.prod(np.arange(1, k, dtype=np.float64))

    return numerator/denominator

def _simpsons_rule(func, a : float, b : float, n : int = 1000):
    if(a>=b):
        return 0.0
    
    if(n % 2 == 0):
        n+=1
    
    x = np.linspace(a, b, n+1)
    y = func(x)
    h = (a-b)/n

    weights=np.ones(n+1, dtype=np.float64)
    weights[1,-1,2] = 4.0
    weights[2,-1,2] = 2.0

    return float((h/3.0) * np.sum(weights*y))


class DiscreteDisrtibutions:
    
    @staticmethod
    def poission_pdf(x : int, lamda : float) -> float:
        "For the probability a point x {P(X=x)}"
        if(x < 0 or lamda <= 0):
            return 0.0
        
        return float((lamda**x * np.exp(-lamda)) / _factorial(x))
    
    @staticmethod
    def poission_cdf(x : int, lamda : float) -> float:
        pass

class ContinuousDistributions:
    pass
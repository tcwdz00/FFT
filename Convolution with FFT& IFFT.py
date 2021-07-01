from math import *  
def fast_poly_evaluate(a,b,n):
    '''
    Evaluate polynomial  at nth roots of 1 using divide and conquer alg
    a: polynomial of coefficent form ex. polynomial 1+6*x+4*x^2+2*x^3 represented as a=[1,6,4,2]
    b: using the roots of form e^(ijT/n) for j=0...n-1 if b evaluate to True, otherwise e^(-ijT/n)
    n: an integer that is power of 2
    return the results as a vector of length n 
    '''
    if len(a)==1:
        return [a[0] for _ in range(n)]
    a_even_sample=fast_poly_evaluate(a[::2],b,n//2)
    a_odd_sample=fast_poly_evaluate(a[1::2],b,n//2)
    a_sample=[]
    for j in range(n):
        val=a_even_sample[j%(n//2)]+\
            e**(complex(0,(j if b==True else -j)*2*pi/n))*a_odd_sample[j%(n//2)]
        a_sample.append(val)
    return a_sample

def FFT(a):
    '''
    perform FFT for a vector a
    a: a vector of length power of 2
    '''
    return fast_poly_evaluate(a,1,len(a))

def IFFT(a):
    '''
    perform IFFT for a vector a
    a: a vector of length power of 2
    '''
    return [e/len(a) for e in fast_poly_evaluate(a,0,len(a))]

def poly_multiply(a,b):
    '''
    with FFT and IFFT, perform polynomial multiplication for 
    polynomials a,b of coefficent form in O(nlogn) time.
    equivalent to compute the convolution of vector a and b
    '''
    n=2**ceil(log2(len(a)+len(b)))
    a_sample=fast_poly_evaluate(a,1,n)
    b_sample=fast_poly_evaluate(b,1,n)
    c_sample=[a_sample[i]*b_sample[i] for i in range(n)]
    return [round(e.real) for e in IFFT(c_sample)][:len(a)+len(b)-1]
    

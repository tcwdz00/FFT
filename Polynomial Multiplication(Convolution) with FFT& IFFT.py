from math import *  
def fast_poly_evaluate(a,b,n):
    '''
    evaluate polynomial a for n th roots of unity 
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
    return fast_poly_evaluate(a,1,len(a))

def IFFT(a):
    return [e/len(a) for e in fast_poly_evaluate(a,0,len(a))]

def poly_multiply(a,b):
    n=2**ceil(log2(len(a)+len(b)))
    a_sample=fast_poly_evaluate(a,1,n)
    b_sample=fast_poly_evaluate(b,1,n)
    c_sample=[a_sample[i]*b_sample[i] for i in range(n)]
    return [round(e.real) for e in IFFT(c_sample)][:len(a)+len(b)-1]
    
    

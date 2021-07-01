# FFT
fast fourier transform implemented with python

function description:
  fast_poly_evaluate(a,b,n):
    Evaluate polynomial  at nth roots of 1 using divide and conquer alg
    a: polynomial of coefficent form ex. polynomial 1+6*x+4*x^2+2*x^3 represented as a=[1,6,4,2]
    n: an integer that is power of 2
    return the results as a vector of length n
    
  FFT(a):
    perform FFT for a vector a
    a: a vector of length power of 2
  
  IFFT(a):
    perform IFFT for a vector a
    a: a vector of length power of 2
    
  poly_multiply(a,b):
    with FFT and IFFT, perform polynomial multiplication for polynomials a,b of coefficent form.
    equivalent to compute convolution of vector a and b
    
    
   
    
  

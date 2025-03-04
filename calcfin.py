def fv(pv , i, n):
    fv = pv * (1 + i/100)**n
    return fv

def pmt (pv, i, n):
    pmt = pv * ((((1+i/100)**n)*(i/100)) / (((1+i/100)**n) - 1))
    return pmt
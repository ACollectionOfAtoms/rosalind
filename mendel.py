from __future__ import division
def mendel():
    k = 23 # homozygous dom
    m = 25 # heterozygous
    n = 23 # homozygous recessive

    # after creating punit squares and a probability tree the following equations were created.
    tot = k + m + n

    AAprob =  (k/tot)*(k/(tot-1)) + (k/tot)*(m/tot)+ (k/tot)*(n/tot)
    Aaprob = (m/tot)*(k/tot) + (m/tot)*(m/(tot-1))*(3/4) + (m/tot)*(n/tot)*(1/2)
    aaprob = (n/tot)*(k/tot) + (n/tot)*(m/tot)*(1/2)
    print AAprob + Aaprob + aaprob
mendel()

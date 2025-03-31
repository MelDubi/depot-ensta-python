import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

#Q2.1
tab = [0.82, 0.87, 0.77, 0.96, 0.75, 0.83, 0.87, 0.81]

moy = np.mean(tab)
var = np.var(tab, ddof=1)
ecart_type = np.std(tab, ddof=1)
a = 0.05
a2 = 0.01

# To find the T critical value
#Returns the inverse cumulative distribution function of the student's distribution evaluated
# at the probability values in p using the corresponding degrees of freedom in nu
tn_1 = scipy.stats.t.ppf(1-a/2, df=len(tab))

IC1 = [moy-tn_1*ecart_type/np.sqrt(len(tab)), moy+tn_1*ecart_type/np.sqrt(len(tab))]

print(IC1)

#Q2.2
Z = scipy.stats.norm.ppf(1-a/2)

IC2 = [moy-Z*ecart_type/np.sqrt(len(tab)), moy+Z*ecart_type/np.sqrt(len(tab))]
print(IC2)

#Q3.3
pDupond = 500/1000
pDurand = 250/1000
pDuroc = 50/1000

Z2 = scipy.stats.norm.ppf(1-a2/2)
IC1Dupond = [pDupond-Z*np.sqrt((pDupond-pDupond**2)/1000), pDupond+Z*np.sqrt((pDupond-pDupond**2)/1000)]
print(IC1Dupond)
IC2Dupond = [pDupond-Z2*np.sqrt((pDupond-pDupond**2)/1000), pDupond+Z2*np.sqrt((pDupond-pDupond**2)/1000)]
print(IC2Dupond)
IC1Durand = [pDurand-Z*np.sqrt((pDurand-pDurand**2)/1000), pDurand+Z*np.sqrt((pDurand-pDurand**2)/1000)]
print(IC1Durand)
IC2Durand = [pDurand-Z2*np.sqrt((pDurand-pDurand**2)/1000), pDurand+Z2*np.sqrt((pDurand-pDurand**2)/1000)]
print(IC2Durand)
IC1Duroc = [pDuroc-Z*np.sqrt((pDuroc-pDuroc**2)/1000), pDuroc+Z*np.sqrt((pDuroc-pDuroc**2)/1000)]
print(IC1Duroc)
IC2Duroc = [pDuroc-Z2*np.sqrt((pDuroc-pDuroc**2)/1000), pDuroc+Z2*np.sqrt((pDuroc-pDuroc**2)/1000)]
print(IC2Duroc)

#3.4
pDuval = 170/1000
E=0.01
n = (Z/E)**2*(pDuval-pDuval**2)
print(n)

#4.5
pCasque = 18/50
IC1Casque = [pCasque-Z*np.sqrt((pCasque-pCasque**2)/50), pCasque+Z*np.sqrt((pCasque-pCasque**2)/50)]
print(IC1Casque)

#4.6
pop = 50
propor = 10/50
Estimation_p= propor/pop
print(Estimation_p)


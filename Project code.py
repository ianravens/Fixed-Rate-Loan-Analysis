#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt

def calcPay(P,n,r,l,APR):
    
    # Calculate monthly payment
    num = (P*(1+r)**n)*r
    den = ((1+r)**n)-1
    x = num/den
    
    # Calculate interest paid and total paid
    tot_paid = x * n
    print(f"The monthly payment for a loan of ${P} with a APR of {APR}% is ${x:.2f}.")
    print(f"Total paid: {tot_paid:.2f} Interest paid: {np.round(tot_paid - P,2)}")
    
    # Create bar graph of principle, interest paid and total paid
    data = {'Total paid':tot_paid, 'Interest paid':tot_paid - P, 'Amount borrowed':P}
    courses = list(data.keys())
    values = list(data.values())
    plt.bar(courses, values, color ='red',
        width = 0.4)
    plt.ylabel("Dollars")
    plt.title(f"Breakdown of {l}-year loan with {APR}% APR.")
    plt.show()

#10-year loan
P = 400000
n = 120
r = 0.005455
calcPay(P,n,r,10,6.534)

#30-year loan
P = 400000
n = 360
r = 0.005171
calcPay(P,n,r,30,6.206)

#15
P = 600000
n = 360
r = 0.0022916
calcPay(P,n,r,15,2.25)


# In[ ]:


#Sensitivity Analysis code
tenYrRates = np.array([0.06134,0.06334,0.06534,0.06734,0.06934])
thirtyYrRates = np.array([0.05804,0.06006,0.06206,0.06406,0.06606])

def calcPay(n,APR):
    monthlyPayments = np.array([])
    totIntPaid = np.array([])
    P = 400000
    for i in range(5):
        
        # Convert APR to MPR
        r = APR[i]/12
        
        # Calculate monthly payment and interest paid
        num = (P*(1+r)**n)*r
        den = ((1+r)**n)-1
        x = num/den
        intPaid = x*n - P
        monthlyPayments = np.append(monthlyPayments,x)
        totIntPaid = np.append(totIntPaid,intPaid)
    return monthlyPayments, totIntPaid

calcPay(120,tenYrRates)
calcPay(360,thirtyYrRates)


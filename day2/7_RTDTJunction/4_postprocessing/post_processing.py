import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

TInlet1 = pd.read_csv('TInlet1.csv')
TInlet2 = pd.read_csv('TInlet2.csv')
T_integer_Inlet1 = pd.read_csv('TIntegrationInlet1.csv')
T_integer_Inlet2 = pd.read_csv('TIntegrationInlet2.csv')

# print(T_integer_Inlet1)
# print(T_integer_Inlet1["T"], TInlet1["avg(T)"])
# print(T_integer_Inlet2["T"], TInlet2["avg(T)"])


RTD1 = T_integer_Inlet1["T"]/TInlet1["avg(T)"]
RTD2 = T_integer_Inlet2["T"]/TInlet2["avg(T)"]

plt.plot(RTD1)
plt.plot(RTD2)
# plt.yscale('log')
plt.legend(['RTD1', 'RTD2'])
plt.title('RTD1 and RTD2')
plt.show()
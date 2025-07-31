import pandas as pd
import matplotlib.pyplot as plt
data =  pd.read_csv('pop.csv')
states=data['state']
populations=data['population']
plt.figure(figsize=(8,8))
plt.pie(populations,labels=states,autopct='%1.1f%%',startangle=140)
plt.title("State-wise population in india")
plt.axis('equal')
plt.show()
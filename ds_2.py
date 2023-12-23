import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('tested.csv')
plt.figure(figsize=(10, 6))

sns.kdeplot(df[df['Survived'] == 1]['Age'], fill=True, color='blue', label='Survived', alpha=0.5)
sns.kdeplot(df[df['Survived'] == 0]['Age'], fill=True, color='red', label='Did not survive', alpha=0.5)

plt.title('Shaded Frequency Polygon of Survivors Based on Age')
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend()
plt.show()

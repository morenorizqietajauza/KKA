import pandas as pd
import matplolib.pyplot as plt 
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')

data.info()

data.head()

data.describe()

print("Rata-Rata:", data['nilai'].mean)()
print("Median:", data['nilai'].median)()
print("Modus:", data['nilai'].mode)()

matematika = data[data]['Matpel'] == 'Matematika'
print(matematika)
rata_max_min = data.groupby('Matpel')['Nilai'].agg(['max','min'])

rata = data.groupby('Matpel')['niali'].mean()
rata.plot(kind='bar')
plt.tittle('Rata Rata Nilai Per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata Rata')
plt.show()

sns.boxplot(x='matpel', y='Niali', data=data)
plt.tittle('Distribusi Nilai per Mapel')
plt.show()


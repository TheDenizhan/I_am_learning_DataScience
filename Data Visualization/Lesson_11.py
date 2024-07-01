#SCATTERPLOT MATRİS
import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris")
df=iris.copy()
print("ilk 5",df.head())
print("tip",df.dtypes)
print("şekli",df.shape)
sns.pairplot(df)
plt.show()
sns.pairplot(df,hue="species")
plt.show()
sns.pairplot(df,hue="species",markers=["o","s","D"])
plt.show()
sns.pairplot(df,kind="reg")
plt.show()
sns.pairplot(df,kind="reg",hue="species")
plt.show()
'''
>Oluşturulan scatterplot grafik toz bulutu şeklinde ise ve yapısal bir formu yoksa bu iki değilken arası bir ilişki olmadığı anlamına gelir.
>Oluşturulan grafikte farklı köşelerde kümeleniyorsa bu yapıları ifade eden farklı alt gruplar vardır ve bunların incelenmesi gerekir.
'''
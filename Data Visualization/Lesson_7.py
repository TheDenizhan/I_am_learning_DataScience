#SUTUN GRAFİKLERİ ÇAPRAZLAMALAR
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype
diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
print("İlk 5\n",df.head())
cut_kategorik = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories=cut_kategorik,ordered=True))
print("Cut\n",df.cut.head())
sns.catplot(x="cut",y="price",data=df)
plt.show()
sns.barplot(x="cut",y="price",hue="color",data=df)
plt.show()
print(df.groupby(["cut","color"])["price"].mean())

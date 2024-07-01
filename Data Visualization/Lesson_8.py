#HİSTOGRAM VE YOĞUNLUK
import matplotlib.pyplot as plt
import seaborn as sns
diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
print("ilk 5",df.head())
sns.distplot(df.price,kde=False)
plt.show()
sns.distplot(df.price,bins=10,kde=False)
plt.show()
sns.distplot(df.price) #sns.distplot(df.price,hist=False)
plt.show()
sns.kdeplot(df.price,shade=True)
plt.show()
#HİSTOGRAM VE YOĞUNLUK ÇAPRAZLAMASI
(sns.FacetGrid(df,hue="cut",
               height=5,
               xlim=(0,10000)).map(sns.kdeplot,"price",shade=True).add_legend())
plt.show()
sns.catplot(x="cut",y="price",hue="color",kind="point",data=df)
plt.show()

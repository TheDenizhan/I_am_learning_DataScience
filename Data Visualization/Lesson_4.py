#KATEGORİK DEĞİŞKEN ÖZETLERİ
import seaborn as sns
import matplotlib.pyplot as plt
planets = sns.load_dataset("planets")
df= planets.copy()
print("İlk 5 veri : \n",df.head())
#Sadece Kategorik Değişkenler ve Özetleri
kat_df = df.select_dtypes(include=["object"])
print("Kategorik Değişkenin İlk 5 Verisi : \n",kat_df.head())
#Kategorik Değişkenin Sınıflarına ve Sınıf Sayısına Erişmek
print("Her Bir Kategorik değişkenin sayısı :\n",kat_df["method"].value_counts())
df["method"].value_counts().plot.barh()
plt.show()
df["method"].value_counts().plot.pie()
plt.show()
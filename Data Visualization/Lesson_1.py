#VERİYE İLK BAKIŞ
import seaborn as sns
planets = sns.load_dataset("planets")
print("İlk 5 veri :\n",planets.head())
#Veri Setinin Hikayesi Nedir?
df = planets.copy()
print("İlk 5 veri :\n",df.head())
print("Son 5 veri :\n",df.tail())
#Veri Setinin Yapısal Bilgileri
print("Tablo Hakkında Bilgi :\n",df.info)
print("Tablo Değişkenleri Hakkında Bilgi :\n",df.dtypes)
import pandas as pd
df.method = pd.Categorical(df.method)
print("Tablo Değişkenleri Hakkında Bilgi :\n",df.dtypes)
print("İlk 5 veri :\n",df.head())
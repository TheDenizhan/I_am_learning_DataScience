#VERİ SETİNİN BETİMLENMESİ
import seaborn as sns
planets = sns.load_dataset("planets")
df = planets.copy()
print("İlk 5 veri : \n",df.head())
print("Verinin Şekli : \n",df.shape)
print("Verinin Sütünları : \n",df.columns)
print("Verinin Açıklaması : \n",df.describe().T)
print("Verinin Detaylı Açıklaması : \n",df.describe(include= "all").T)
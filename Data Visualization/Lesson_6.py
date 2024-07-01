'''
Veri Seti Hikayesi
price: dolar cinsinde fiyat (326—18,823)
carat: ağlrllk (0.2—5.01)
cut: kalite (Fair, Good Very Good, Premium, Ideal)
color: renk (from J (worst) to D (best))
clarity: temizliği, berraklığı (I1 (worst), S12, SI1, VS2, VS1, VVS2, VVS1, IF (best))
x: length in mm (0—10.74)
y: width in mm (0—58.9)
z: depth in mm (0—31.8)
G)
depth: toplam derinlik yüzdesi = z/ mean(x, y) = 2 z / (x + y) (43—79)
table: elmasın en noktaslna göre geni$iöi (43—95)
'''
import matplotlib.pyplot as plt
import seaborn as sns
diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
print("İlk 5\n",df.head())
#Veri Setine Hızlı Bakış
print("Hakkında\n",df.info)
print("Açıklama\n",df.describe().T)
print("Cut sütünü\n",df["cut"].value_counts())
print("Color sütünu\n",df["color"].value_counts())
#Ordinal Tanımlama
from pandas.api.types import CategoricalDtype
print("cut ilk 5\n",df.cut.head())
df.cut = df.cut.astype(CategoricalDtype(ordered=True))
print("Cut ilk\n",df.cut.head(1))
cut_kategorik = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories=cut_kategorik,ordered=True))
print("Cut ilk\n",df.cut.head(1))
#SUTUN GRAFİĞİN (BARPLOT) OLUŞTURULMASI
#BARPLOT
df["cut"].value_counts().plot.barh().set_title("Cut Değişkeninin Sınıf Frekansları")
plt.show()
sns.barplot(x="cut",y=df.cut.index,data=df)
plt.show()

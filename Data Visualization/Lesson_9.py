#BOXPLOT
'''
Veri Seti Hikayesi
total_bill: yemeğin toplam fiyatı (bahşiş ve vergi dahil)
tip: bahşiş
sex: ücreti ödeyen kişinin cinsiyeti (O=male, 1=female)
smoker: grupta sigara içen var mı? (O=No, 1=Yes)
day: gün (3=Thur, 4=Fri, 5=sat, 6=Sun)
time: ne zaman? (O=Day, 1=Night)
size: grupta kaç kişi var?
'''
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset("tips")
df= tips.copy()
print("ilk 5",df.head())
print("Açıklama",df.describe().T)
print("Sex",df["sex"].value_counts())
print("smoker",df["smoker"].value_counts())
print("day",df["day"].value_counts())
print("time",df["time"].value_counts())
#KUTU GRAFİĞİ OLUŞTURMA
sns.boxplot(x=df["total_bill"])
plt.show()
sns.boxplot(x=df["total_bill"],orient="v")
plt.show()
#KUTU GRAFİĞİ ÇAPRAZLAMA
#HANGİ GÜNLER DAHA FAZLA KAZANIYORUZ?
sns.boxplot(x="day",y="total_bill",data=df)
plt.show()
#SABAH MI YOKSA AKŞAM MI DAHA ÇOK KAZANIYORUZ?
sns.boxplot(x="time",y="total_bill",data=df)
plt.show()
#KİŞİ SAYISI KAZANÇ
sns.boxplot(x="size",y="total_bill",data=df)
plt.show()
sns.boxplot(x="day",y="total_bill",hue="sex",data=df)
plt.show()
#VİOLİN GRAFİĞİ
sns.catplot(y="total_bill",kind="violin",data=df)
plt.show()
#VİOLİN ÇAPRAZLAMA
sns.catplot(x="day",y="total_bill",kind="violin",data=df)
plt.show()
sns.catplot(x="day",y="total_bill",hue="sex",kind="violin",data=df)
plt.show()
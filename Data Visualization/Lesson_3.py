#EKSİK DEĞERLERİN İNCELENMESİ
import seaborn as sns
planets = sns.load_dataset("planets")
df= planets.copy()
print("İlk 5 veri : \n",df.head())
#HİÇ EKSİK GÖZLEM VARMI?
print("Eksik Gözlemler : \n",df.isnull().values.any())
#HANGİ DEĞİŞKENLERDE KAÇAR TANE VAR?
print("Hangi Değişkenlerde Eksik Veri Var :\n",df.isnull().sum)
#df["değişken_ismi"].fillna(0,inplace = True)
#df["değişken_ismi"].fillna(df.değişken_ismi.mean(),inplace= True)
#df.fillna(df.mean(),inplace = True)
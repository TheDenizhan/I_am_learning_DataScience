#SÜREKLİ DEĞİŞKEN ÖZETLERİ
import seaborn as sns

planets = sns.load_dataset("planets")
df= planets.copy()
print("İlk 5 veri : \n",df.head())
df_num = df.select_dtypes(include=["float64","int64"])
print("İlk 5 veri : \n",df_num.head())
print("İlk 5 veri : \n",df_num.describe().T)
print("İlk 5 veri : \n",df_num["distance"].describe())
print("\nOrtalama :"+str(df_num["distance"].mean()))
print("\nDolu Gözlem Sayısı :"+str(df_num["distance"].count()))
print("\nMaksimum Değer :"+str(df_num["distance"].max()))
print("\nMinimum Değer :"+str(df_num["distance"].min()))
print("\nMedyan :"+str(df_num["distance"].median()))
print("\nStandart Sapma :"+str(df_num["distance"].std()))
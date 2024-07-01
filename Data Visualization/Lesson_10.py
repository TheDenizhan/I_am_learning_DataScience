#KORELASYON GRAFİĞİ
#SCATTERPLOT
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset("tips")
df= tips.copy()
sns.scatterplot(x="total_bill",y="tip",data=df)
plt.show()
#SCATTERPLOT ÇAPRAZLAMA
sns.scatterplot(x="total_bill",y="tip",hue="time",data=df)
plt.show()
sns.scatterplot(x="total_bill",y="tip",hue="time",style="time",data=df)
plt.show()
sns.scatterplot(x="total_bill",y="tip",hue="day",style="time",data=df)
plt.show()
sns.scatterplot(x="total_bill",y="tip",hue="size",size="size",data=df)
plt.show()
#DOĞRUSAL İLİŞKİNİN GÖSTERİLMESİ
sns.lmplot(x="total_bill",y="tip",data=df)
plt.show()
sns.lmplot(x="total_bill",y="tip",hue="smoker",data=df)
plt.show()
sns.lmplot(x="total_bill",y="tip",hue="smoker",col="time",data=df)
plt.show()
sns.lmplot(x="total_bill",y="tip",hue="smoker",col="time",row="sex",data=df)
plt.show()

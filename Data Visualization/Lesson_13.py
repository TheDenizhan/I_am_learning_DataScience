#ÇİZGİ GRAFİĞİ
import matplotlib.pyplot as plt
import seaborn as sns
fmri = sns.load_dataset("fmri")
df = fmri.copy()
print("ilk 5",df.head())
print("Şekil",df.shape)
print("timepoint açıklama",df["timepoint"].describe())
print("signal açıklama",df["signal"].describe())
print("timepoint count",df.groupby("timepoint")["signal"].count())
print("signal count",df.groupby("signal").count())
print("timepoint describe",df.groupby("timepoint")["signal"].describe())
#ÇİZGİ GRAFİĞİN OLUŞTURULMASI
sns.lineplot(x="timepoint",y="signal",data=df)
plt.show()
sns.lineplot(x="timepoint",y="signal",hue="event",data=df)
plt.show()
sns.lineplot(x="timepoint",y="signal",hue="event",style="event",data=df)
plt.show()
sns.lineplot(x="timepoint",
             y="signal",
             hue="event",
             style="event",
             markers=True,
             dashes=True,
             data=df)
plt.show()
sns.lineplot(x="timepoint",
             y="signal",
             hue="region",
             style="event",
             data=df)
plt.show()
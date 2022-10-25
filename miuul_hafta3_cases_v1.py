from typing import Union, Any

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pandas import Series, DataFrame
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader

""" İŞ PROBLEMİ : 
Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak
seviye tabanlı (level based) yeni müşteri tanımları (persona)
oluşturmak ve bu yeni müşteri tanımlarına göre segmentler
oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
şirkete ortalama ne kadar kazandırabileceğini tahmin etmek
istemektedir.
"""
"""
Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır.
*************************************************************************
*************************************************************************
ÖNEMLİ KISIMLAR:

*** Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. ***
Bunun anlamı tablo tekilleştirilmemiştir. 
*** Diğer bir ifade ile belirli demografik özelliklere sahip bir
kullanıcı birden fazla alışveriş yapmış olabilir. ***
*************************************************************************
*************************************************************************
"""

"""
PRICE   – Müşterinin harcama tutarı
SOURCE  – Müşterinin bağlandığı cihaz türü
SEX     – Müşterinin cinsiyeti
COUNTRY – Müşterinin ülkesi
AGE     – Müşterinin yaşı
"""

# ///  GÖREV 1 - SORU 1  //////////////////////////////////////////////////////////////
"""
soru : persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

todos:
1. veri seti okutulacak +
2. describe() +
3. info() +
4. object type dgişkenlerin sınıf sayısını gösteren bir fonk yaz

faced problems:
1. veri seti okuturken path deki "/" leri "\" ile manuel olarak değiştirmek
2. veri setinde değişkenlerin adı BÜYÜK bunlar kod yazarken akıcılığı sağlamak için küçültülmeli
"""
persona = pd.read_csv("C:/Users/Abdulkadir DEMİRCİ/Desktop/2022mvkpython/veri/persona.csv")
df = persona.copy()
df.info()
df.describe().T
df.nunique()
# column isimlerini küçültmek
df.columns = [col.lower() for col in df.columns]
df.columns


# ///  GÖREV 1 - SORU 2  //////////////////////////////////////////////////////////////
"""
soru : Kaç unique SOURCE vardır? Frekansları nedir?

todos: ayrı ayrı bastırılan çıktıları tek bir print içinde göster
faced problems: -
link : https://seaborn.pydata.org/tutorial/color_palettes.html
"""
print(" source değişkeninin eşsiz değer ve miktarları:\n{}\n\n"
      "source değişkeninin unique degerleri: {}\n\n"
      "source degişkeninin unique deger sayısı: {}".format(df["source"].value_counts(),
                                                         df["source"].unique(),
                                                         df["source"].nunique()))
df["source"].value_counts()
df["source"].unique()
df["source"].nunique()

sns.countplot(x=df["source"],data=df,saturation=0.9,palette="YlOrBr")
plt.title("kaynak kullanımı")
plt.show()


# ///  GÖREV 1 - SORU 3  //////////////////////////////////////////////////////////////
"""
soru : Kaç unique PRICE vardır?

todos: -
faced problems: -
"""
df["price"].nunique()
df["price"].unique()
sns.countplot(x=df["price"],data=df,saturation=0.8,palette="magma")
plt.title("fiyat dağılımı")
plt.show()


# ///  GÖREV 1 - SORU 4  //////////////////////////////////////////////////////////////
"""
soru : Hangi PRICE'dan kaçar tane satış gerçekleşmiş? yani unique degerlerin frekansı

todos: -
faced problems: -
"""
df["price"].value_counts()


# ///  GÖREV 1 - SORU 5  //////////////////////////////////////////////////////////////
"""
soru : Hangi ülkeden kaçar tane satış olmuş? yani unique degerlerin frekansı

todos: -
faced problems: -
"""
df["country"].value_counts()
sns.countplot(x=df["country"],saturation=0.5,palette="magma")
plt.title("ülkeler")
plt.show()
# ///  GÖREV 1 - SORU 6  //////////////////////////////////////////////////////////////
"""
soru : Ülkelere göre satışlardan toplam ne kadar kazanılmış?

todos: groupby("country), aggregate according to "price"
faced problems: "sum" ile ["sum"] arasındaki fark önemli, 
hangi toplulaştırma fonk.uyguladıgımızı görmeliyiz
"""
df.groupby("country").agg({"price": ["sum"]})
# df.groupby("country").agg({"price": "sum"})
df.pivot_table("price", "country", aggfunc=["sum"])
df.groupby("country")[["price"]].aggregate(["sum"])
# df.groupby("country")["price"].aggregate(["sum"])

df.groupby("country")[["price"]].aggregate(["sum"]).plot(kind="bar")
plt.show()


# ///  GÖREV 1 - SORU 7  //////////////////////////////////////////////////////////////
"""
soru : SOURCE türlerine göre satış sayıları nedir?

todos: groupby("source), aggregate using "count"
faced problems: 
1. "count" ile ["count"] arasındaki fark önemli, 
hangi toplulaştırma fonk.uyguladıgımızı görmeliyiz
2. pivot_table da df.pivot_table("source","source",aggfunc=["count"]) yazınca 
value error verdi. 
"""
df.groupby("source").agg({"source": ["count"]})
df.groupby("source")[["source"]].aggregate(["count"])
df.pivot_table("age", "source", aggfunc=["count"])

# ///  GÖREV 1 - SORU 8  //////////////////////////////////////////////////////////////
"""
soru : Ülkelere göre PRICE ortalamaları nedir?

todos: groupby("country), aggregate using "mean" over "price"
faced problems: elde edilen sonuçta noktdan sonra sadece 3 basamak görmek istiyorum +
link: https://stackoverflow.com/questions/8885663/how-to-format-a-floating-number-to-fixed-width-in-python/8885688#8885688
"""
pd.options.display.float_format = '{:.3f}'.format

df.groupby("country").agg({"price":["mean"]})
df.groupby("country")[["price"]].aggregate(["mean"])
df.pivot_table("price", "country", aggfunc=["mean"])

df.groupby("country")[["price"]].aggregate(["mean"]).plot()
plt.show()


# ///  GÖREV 1 - SORU 9  //////////////////////////////////////////////////////////////
"""
soru : SOURCE'lara göre PRICE ortalamaları nedir?

todos: groupby("source), aggregate using "mean" over "price"
faced problems: elde edilen sonuçta noktdan sonra sadece 3 basamak görmek istiyorum
"""
df.groupby("source").agg({"price": ["mean"]})
df.groupby("source")[["price"]].aggregate(["mean"])
df.pivot_table("price", "source", aggfunc=["mean"])

# ///  GÖREV 1 - SORU 10 //////////////////////////////////////////////////////////////
"""
soru : COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

todos: groupby(["country","source]), aggregate using "mean" over "price"
faced problems: 
1. elde edilen sonuçta noktdan sonra sadece 3 basamak görmek istiyorum +
2. grafik sadece android olanları çizdiriyor
"""
df.groupby(["country", "source"]).agg({"price": ["mean"]})
df.groupby(["country", "source"]).price.aggregate(["mean"])
# df.groupby(["country","source"])[["price"]].aggregate(["mean"])
df.pivot_table("price", ["country", "source"], aggfunc=["mean"])

df.groupby(["country", "source"]).agg({"price": ["mean"]}).plot()
plt.xticks(rotation=15)
plt.show()


# ///  GÖREV 2 - SORU 1  //////////////////////////////////////////////////////////////
"""
soru : COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

todos: groupby(["country","source","sex","age"]), aggregate using "mean" over "price"
faced problems: elde edilen sonuçta noktdan sonra sadece 3 basamak görmek istiyorum
"""
df.groupby(["country", "source", "sex", "age"]).agg({"price": ["mean"]})
df.groupby(["country", "source", "sex", "age"])[["price"]].aggregate(["mean"])
df.pivot_table(["price"], ["country", "source", "sex", "age"], aggfunc="mean")

df.groupby(["country", "source", "sex", "age"]).agg({"price": ["mean"]}).plot()
plt.xticks(rotation=15)
plt.show()


# ///  GÖREV 3 - SORU 1  //////////////////////////////////////////////////////////////
"""
soru : Önceki sorudaki çıktıyı daha iyi görebilmek için 
sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
Çıktıyı agg_df olarak kaydediniz

todos: 
1. price a göre sort et
2. groupby(["country","source","sex","age"]), aggregate using "mean" over "price"
faced problems: 
1. anlamak
2. yapılan groupby işlemine gerek var mıydı?
evet aynı kırılıma sahip aynı yaştaki gözlemler tek bir deger olarak algılanmalı,
ileride tüm bu kırılım adımlarında customer_label_based adlı degişken oluşturacagız
bu işlem yapılmadan tekilleştirmeye geçilseydi bilgi kaybı yasana bilirdi.
"""
agg_df = df.pivot_table(["price"], ["country", "source", "sex", "age"], aggfunc="mean").\
    sort_values(by="price",ascending=False)
agg_df.head()


# ///  GÖREV 4 - SORU 1  //////////////////////////////////////////////////////////////
"""
soru : Indekste yer alan isimleri değişken ismine çeviriniz.

todos: 
1. index isimlerini yazdır
2. index isimlerini degişkenlere cevir
faced problems: -
"""
agg_df.index
agg_df.reset_index(inplace= True)
agg_df.head()


# ///  GÖREV 5 - SORU 1  //////////////////////////////////////////////////////////////
"""
soru : Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.

todos: 
1. age arlıklarını belirle
2. pd.cut kullan
faced problems: -
"""
# 0-18 / 19-23 / 24-30 / 31-40 / 41 -90 yas aralıklarımız
age_class = [0,19,24,31,41,90]
agg_df["age_cat"] = pd.cut(agg_df["age"],(0,18,23,30,40,90))
agg_df.head()

sns.countplot(x=agg_df["age_cat"], data = agg_df,palette="colorblind")
plt.show()

# ///  GÖREV 6 - SORU 1  //////////////////////////////////////////////////////////////
"""
soru : Yeni seviye tabanlı müşterileri (persona) tanımlayınız.

todos: 
1. Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
2. Yeni eklenecek değişkenin adı: customers_level_based
3. Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek 
customers_level_based değişkenini oluşturmanız gerekmektedir.
4. Dikkat! List comprehension ile customers_level_based değerleri oluşturulduktan 
sonra bu değerlerin tekilleştirilmesi gerekmektedir.
Örneğin birden fazla şu ifadeden olabilir:
 USA_ANDROID_MALE_0_18. Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.

faced problems: -
"""
agg_df["customer_level_based"] = \
    agg_df.apply(lambda row: "%s_%s_%s_%s"%(row["country"].upper(),row["source"].upper(),
                                               row["sex"].upper(),row["age_cat"]),axis=1)
agg_df.head()
# tekilleştirme
agg_df.groupby("customer_level_based").agg({"price":"mean"})
# sadece customer_level_based ve price degişkenini içeren bir df olusturmak istersek
elegance_df=agg_df.groupby("customer_level_based").agg({"price":"mean"}).reset_index()
elegance_df.head()

sns.countplot(x= agg_df["customer_level_based"],data = agg_df,palette="magma")
plt.show()


# ///  GÖREV 7 - SORU 1  //////////////////////////////////////////////////////////////
"""
soru : Yeni müşterileri (personaları) segmentlere ayırınız.

todos: 
1. Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız
(böyle birşey yapılamz gözlemler tekilleştirildi)
2. Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz
3. Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

faced problems: segmentleme işlemi en yüksekten en düşüge göre mi yapacak yoksa tam tersi mi?
(qcut price degişkeni küçükte buyuge sıralayıp en kucuk %0-%25lik parçaya D, %25-%50lik parçaya C,
  %50-%75lik parçaya B, %75-%100 lik parçaya A diye label ekleyecek 
  böyle olsaydı segment sayılarının aynı olmasını beklerdik
faydalı link:
https://stackoverflow.com/questions/59482017/bin-labels-must-be-one-fewer-than-the-number-of-bin-edges-after-passing-pd-qcu
"""
pd.set_option("display.max_columns",None)
agg_df.head()
label=["D","C","B","A"]
agg_df["segment"] = pd.qcut(agg_df["price"],4,duplicates="drop")
agg_df.head()
agg_df["segment"] = pd.qcut(agg_df["price"],4,labels=label,duplicates="drop")
agg_df["segment"].value_counts()
agg_df.groupby("segment")[["price"]].aggregate(["min","max","mean","sum"])

sns.countplot(x=agg_df["segment"],data = agg_df,palette="magma")
plt.show()

# ///  GÖREV 8 - SORU 1  //////////////////////////////////////////////////////////////
"""
soru : Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.

todos: 
1. 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir 
ve ortalama ne kadar gelir kazandırması beklenir?
2. 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir 
ve ortalama ne kadar gelir kazandırması beklenir?

faced problems: -
"""
new_user1 = "TUR_ANDROID_FEMALE_(30, 40]"
new_user2 = "FRA_IOS_FEMALE_(30, 40]"
agg_df[agg_df["customer_level_based"]==new_user1]
agg_df[agg_df["customer_level_based"]==new_user2]

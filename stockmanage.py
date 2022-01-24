from unittest import result
import pandas as pd

pd.set_option('display.max_column',30)
pd.set_option('display.width',1000)

bidu=pd.read_csv("./stock.BIDU.csv",index_col=0)
iq=pd.read_csv("./stock.IQ.csv",index_col=0)

print(bidu.head(5))
print()
print(iq.head(5))

#add prefix 
bidu.columns=["bidu_"+col.lower() for col in bidu.columns]
iq.columns=["iq_"+col.lower() for col in iq.columns]

print(bidu.head(5))
print()
print(iq.head(5))

#Splicing two stocks 
df=pd.concat([bidu,iq],axis=1)
print(df.head(5))

#Filter the desired column 
result=pd.concat([bidu,iq],axis=1)
quotations=result[["bidu_open","bidu_close","iq_open","iq_close"]]
print(quotations.head(5))

#Calculate stock gains 
#Extract opening and closing prices 
quotations=result[["bidu_open","bidu_close","iq_open","iq_close"]].copy()

#Calculate the change percentage of the day 
quotations["bidu_change"]=(quotations["bidu_close"]/quotations["bidu_open"]-1)*100
quotations["iq_change"]=(quotations["iq_close"]/quotations["iq_open"]-1)*100

print(quotations.head(5))
#Whether the two stocks rose and fell together. 
quotations["similarity_flag"]=(quotations["bidu_change"]*quotations["iq_change"]>0)*1
print(quotations.head(5))

#The percentage of signals that both stocks rose and fell at the same time. 

percent=quotations["similarity_flag"].sum()/len(quotations)
print(percent*100)
import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

for i in df["FlightNumber"].index: #Problem - 1
    temp = df["FlightNumber"][i]
    if(pd.isna(temp)):
        df["FlightNumber"][i] = df["FlightNumber"][i-1]+10
df["FlightNumber"].astype('int')

df_temp = df["From_To"].str.split("_",expand=True,) #Problem - 2
df_temp = df_temp.rename(columns={0: "From", 1: "To"})
print(df_temp)

df_capital=df["From_To"].str.capitalize() #Problem - 3
df_temp = df_capital.str.split("_",expand=True,)
df_temp = df_temp.rename(columns={0: "From", 1: "To"})
print(df_temp)

result = pd.concat([df_temp,df], axis=1, sort=False) #Problem - 4
result = result.drop(['From_To'], axis=1)

lst = list(result["RecentDelays"]) #Problem - 5
delays = pd.DataFrame(lst, columns =['Delay_1', 'Delay_2','Delay_3']) 
result = result.drop(['RecentDelays'], axis=1)
result = pd.concat([result,delays], axis=1, sort=False)

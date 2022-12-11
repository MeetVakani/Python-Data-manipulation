#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Data amnipulation with pandas
# sorting data
import pandas as pd
import numpy as np

data_BM=pd.read_csv('C:\study material\Analyticalvidhya(python for datascience)/bigmart_data.csv')

# Drop the null value
data_BM=data_BM.dropna(how='any')

data_BM.head()


# In[5]:


# sort data with sort_value fn

sorted_data=data_BM.sort_values(by='Outlet_Establishment_Year')
# check the sorted data
data_BM[:5]


# In[27]:


# sorting with two values

sorted_data=data_BM.sort_values(by=['Outlet_Establishment_Year', 'Item_Outlet_Sales'],ascending=False ,inplace=True)
data_BM[:5]


# In[28]:


sorted_data=data_BM.sort_values(by=['Item_Outlet_Sales', 'Outlet_Establishment_Year'],ascending=False ,inplace=True)
data_BM[:5]


# In[31]:


data_BM.sort_index(inplace=True)
data_BM.head()


# In[53]:


# Merging the data with pandas
# help  of concat() by creating dummy dataframes
# lets create dummy dataframes

df1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3'],
                  'C':['C0','C1','C2','C3'],
                  'D':['D0','D1','D2','D3']},
                    index=[0,1,2,3])

df2=pd.DataFrame({'A':['A4','A5','A6','A7'],
                  'B':['B4','B5','B6','B7'],
                  'C':['C4','C5','C6','C7'],
                  'D':['D4','D5','D6','D7']},
                    index=[4,5,6,7])

df3=pd.DataFrame({'A':['A8','A9','A10','A11'],
                  'B':['B8','B9','B10','B11'],
                  'C':['C8','C9','C10','C11'],
                  'D':['D8','D9','D10','D11'],
                  'E':['E8','E9','E10','E11']},
                    index=[8,9,10,11])


# In[44]:


# now lets combined them row vise with concat fn 
# with the help of the keys we can know which data is from which dataframe

result=pd.concat([df1,df2,df3], keys=['x','y','z'])
result


# In[45]:


# now to extract df2 which have the label 'y'
result.loc['y']


# In[67]:


# there are 3 types of join. upper one was join='outer' which takes union of dataframes
# Now for join='inner'

result=pd.concat([df1,df2,df3],keys=['x','y','z'], join='inner')
result


# In[55]:


# merging means combining the data with the help of common column in data frame
# outer merge
pd.merge(df1,df3, on=['A','B','C','D'], how='outer')


# In[63]:


#inner merge
pd.merge(df1,df3, on=['A','B','C','D'], how='inner')


# In[64]:


# left merge
pd.merge(df1,df3, on=['A','B','C','D'], how='left')


# In[65]:


# right merge
pd.merge(df1,df3, on=['A','B','C','D'], how='right')


# In[1]:


# main diff of merge and concat : concat for appending datafreame while merge for combine df on the basis of values of common column


# In[3]:


# APPLY function
# used for manipulation in row and column wise, it is faster than applying FOR loop for whole dataset. 
import pandas as pd
import numpy as np

data_BM=pd.read_csv('C:\study material/bigmart_data.csv')

# Drop the null value
data_BM=data_BM.dropna(how='any')

# accesing row wise
data_BM.apply(lambda x: x) 


# In[4]:


# accessing first row by row index
data_BM.apply(lambda x:x[0])


# In[7]:


# accessing first column by column index and axis for telling that we are working with columns now.
data_BM.apply(lambda x:x[0] ,axis=1)


# In[11]:


# accessing first column by name

data_BM.apply(lambda x: x['Item_Identifier'], axis=1)


# In[22]:


# Now we can also use the apply fn for a condition over a data of row and column by clipping
# before clipping
data_BM.iloc[:5,5]  #to access item_MRP column


# In[23]:


# now we only want MRP upto value=200 .hence lets clip

def price_clip(price):
    if(price>200):
        price=200
    return price

# after clipping 
data_BM.iloc[:5,5].apply(lambda x:(price_clip(x)))
# now every value which was greater than 200 is 200.


# In[50]:


# now for another example lets label outlet_location_type column so that we can use num instead of tier1,tier2,tier3.

def label(city):
    if(city=='Tier 1'):
        label=1
    elif(city=='Tier 2'):
        label=2
    else:
        label=3
    return label
#data_BM.iloc[:7,9] this is before data
data_BM.iloc[:7,9].apply(lambda x:(label(x))) #this is after data


# In[51]:


# aggregation
# it gives summeries and knowledge from data
# 3 most important funcions of aggregation:
    #groupby
    #crosstab
    #pivottable


# In[68]:


# groupby:

import pandas as pd
import numpy as np

data_BM=pd.read_csv('C:\study material/bigmart_data.csv')

# Drop the null value
data_BM=data_BM.dropna(how='any')

# groupby function
price_by_item = data_BM.groupby('Item_Type') #grouping by one column
price_by_item.Item_MRP.mean() #finding mean 


# In[71]:


# grouping two columns
multiple_groups=data_BM[:7].groupby(['Item_Type','Item_Fat_Content'])
multiple_groups.first()


# In[72]:


# crosstab
# generate crosstab of size and location type
pd.crosstab(data_BM['Outlet_Size'],data_BM['Outlet_Location_Type']) #compare two columns


# In[74]:


# pivottable
# takes parameter like dataframe ,index which indicates column ,values indicate column we want to aggregate
# uses mean by default
# we can also provide more column in index parameter.
pd.pivot_table(data_BM ,index=['Outlet_Establishment_Year'], values=['Item_Outlet_Sales'])


# In[75]:


# now not only for mean but for np.mean ,np.median ,min,max,np.std in aggfunc.
pd.pivot_table(data_BM ,index=['Outlet_Establishment_Year'] ,values=['Item_Outlet_Sales'] ,aggfunc=[np.mean ,np.median ,min,max,np.std])







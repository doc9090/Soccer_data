#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('BIG FIVE 1995-2019.csv')


# In[3]:


df


# In[4]:


ita_country=df[df["Country"]=="IT"]


# In[5]:


ita_country.head()


# In[6]:


ita_country


# In[7]:


df['Team 1'].iloc[0]


# In[8]:


aston_villa_plays=df[df['Team 1']=='Aston Villa FC ']


# In[9]:


aston_villa_plays


# In[10]:


type(aston_villa_plays['FT Team 1'].iloc[0])


# In[11]:


counter=0
list_of_result=[]

for i in aston_villa_plays['FT Team 1']:
    second_result=aston_villa_plays['FT Team 2'].iloc[counter]
    
    
    if i>second_result:
        list_of_result.append("yes")
        
    else:
        list_of_result.append("no")
        
    
    counter+=1
    
number_elements=0
for element in list_of_result:

    number_elements+=1
    
print(number_elements)


# In[12]:


number_of_victories=0

for victory in list_of_result:
    
    if victory == 'yes':
        number_of_victories+=1
        
    
        
print(number_of_victories)

print('probability of victory'+' '+ str((number_of_victories/number_elements)*100))
        
        


# In[13]:



def adding_column_df(df,list_1,name):
    
    df[str(name)]=list_1
    
    return df


aston_villa_plays=adding_column_df(aston_villa_plays,list_of_result,'result')
    
    

    
    


# In[14]:


aston_villa_plays


# In[15]:


aston_villa_plays.isna().sum()


# In[16]:


type(aston_villa_plays['Date'])


# In[24]:


aston_villa_plays.head(1)


# In[ ]:





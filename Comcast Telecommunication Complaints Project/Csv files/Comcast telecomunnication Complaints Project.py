#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('D:\Data Scientist Master Course\Data sci with python\Project Final\Comcast_telecom_complaints_data.csv')


# In[3]:


df.head()


# In[4]:


print(df.isnull().sum())


# In[5]:


df.describe(include='all')


# In[6]:


# Provide the trend chart for the number of complaints at monthly and daily granularity levels
df['Date_month_year']=df['Date_month_year'].apply(pd.to_datetime)
df=df.set_index('Date_month_year')


# In[7]:


#plotting montly chart
months=df.groupby(pd.Grouper(freq='M')).size().plot()
plt.xlabel('Months')
plt.ylabel('Frequency')
plt.title('Montly Trend Chart')


# # From Above chart the complaints for the month of june 2015 are maximum

# In[8]:


df['Date'].value_counts(dropna=False)[:8]


# In[9]:


#plotting daily chart
df=df.sort_values(by='Date')
plt.figure(figsize=(6,6))
df['Date'].value_counts().plot()
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.title('Daily Trend Chart')


# # Provide a table with the frequency of complaint types.

# In[10]:


df['Customer Complaint'].value_counts(dropna=False)[:9]


# In[11]:


df['Customer Complaint'].value_counts(dropna=False)[:9].plot.bar()


# # Which complaint types are maximum i.e., around internet, network issues, or across any other domains.

# In[12]:


internet_issues1=df[df['Customer Complaint'].str.contains('network')].count()


# In[13]:


internet_issues2=df[df['Customer Complaint'].str.contains('speed')].count()


# In[14]:


internet_issues3=df[df['Customer Complaint'].str.contains('data')].count()


# In[15]:


internet_issues4=df[df['Customer Complaint'].str.contains('internet')].count()


# In[16]:


billing_issues1=df[df['Customer Complaint'].str.contains('bill')].count()


# In[17]:


billing_issues2=df[df['Customer Complaint'].str.contains('billing')].count()


# In[18]:


billing_issues3=df[df['Customer Complaint'].str.contains('charges')].count()


# In[19]:


service_issues1=df[df['Customer Complaint'].str.contains('service')].count()


# In[20]:


service_issues2=df[df['Customer Complaint'].str.contains('customer')].count()


# In[21]:


total_internet_issues=internet_issues1+internet_issues2+internet_issues3+internet_issues4
print(total_internet_issues)


# In[22]:


total_billing_issues=billing_issues1+billing_issues2+billing_issues3
print(total_billing_issues)


# In[23]:


total_service_issues=service_issues1+service_issues2
print(total_service_issues)


# In[24]:


other_issues=2224-(total_internet_issues+total_billing_issues+total_service_issues)
print(other_issues)


# # Create a new categorical variable with value as Open and Closed. Open & Pending is to be categorized as Open and Closed & Solved is to be categorized as Closed

# In[25]:


df.Status.unique()


# In[26]:


df['newStatus']=['Open' if Status=='Open' or Status=='Pending' else 'Closed' for Status in df['Status']]
df=df.drop(['Status'],axis=1)
df


# # Provide state wise status of complaints in a stacked bar chart. Use the categorized variable from 

# In[28]:


Status_complaints =df.groupby(['State','newStatus']).size().unstack()
print(Status_complaints)


# In[29]:


Status_complaints.plot.bar(figsize=(10,10),stacked=True)


# # Which state has the maximum complaints

# In[27]:


df.groupby(['State']).size().sort_values(ascending=False)[:5]


# # insights-maximum complaints are for state of georgia 

# # Which state has the highest percentage of unresolved complaints

# In[31]:


print(df['newStatus'].value_counts())


# In[32]:


unresolved_data= df.groupby(['State','newStatus']).size().unstack().fillna(0).sort_values(by='Open',ascending=False)
unresolved_data['Unresolved_complaints_pr']=unresolved_data['Open']/unresolved_data['Open'].sum()*100
print(unresolved_data)
unresolved_data.plot()


# # Provide the percentage of complaints resolved till date, which were received through the Internet and customer care calls

# In[35]:


resolved_data=df.groupby(['Received Via','newStatus']).size().unstack().fillna(0)
resolved_data['resloved']=resolved_data['Closed']/resolved_data['Closed'].sum()*100
resolved_data['resloved']


# In[36]:


resolved_data.plot(kind='bar',figsize=(8,8))


# # insights - `from above graph we can see there are total 50.61% complaints resolved for customer care call and 49.39% for received via internet

# In[ ]:





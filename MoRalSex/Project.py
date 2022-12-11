#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


st.header("Getting ready")

st.subheader("This data set was provided by sex toys shop Sexy Elephant.")

st.subheader("Sexy Elephant commissioned an oral-sex-focused questionnaire survey on a representative sample (n=1100) of the Czech's online population in the age range 18-65. The survey was conducted by an international market research agency.")

# In[2]:


import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv('oral_sex_eng_translation.csv')


# ## The Dataset itself

# In[4]:


data


# In[5]:


print(data["Age"].mean())


# In[6]:


print(data["Age"].std())


# In[7]:


print(data["Age"].median())


# ## Data description

# In[8]:


data["Age"].describe()


# In[9]:


categories = [col for col in data.columns if data[col].dtype=='O']
categories


# In[10]:


uqique_categories_values={}
for colm in categories:
    uqique_categories_values[colm] = data[colm].unique()

uqique_categories_values


# ## Pretty clean, don’t you think?

# In[11]:


data.isnull().values.any()


# In[12]:


data.isnull().sum().sum()


# ## Let's add some columns!

# In[13]:


data["Difference in age from max"] = max(data["Age"]) - data["Age"]
data


# In[14]:


data["Difference in age from max"].describe()


# In[15]:


data["Difference in age from max"].median()


# ## Plots

# In[16]:


sns.histplot(data['Age'], kde=True, bins=40)
plt.ylabel("Number of people")
plt.show()


# Age is not normally distributed.

# In[17]:


unique = data["Age"].unique()
df12 = sum([data.loc[data.Age == x, 'Age'].count() for x in unique if 18 <= x <= 20])
df23 = sum([data.loc[data.Age == x, 'Age'].count() for x in unique if 20 < x <= 30])
df34 = sum([data.loc[data.Age == x, 'Age'].count() for x in unique if 30 < x <= 40])
df45 = sum([data.loc[data.Age == x, 'Age'].count() for x in unique if 40 < x <= 50])
df56 = sum([data.loc[data.Age == x, 'Age'].count() for x in unique if 50 < x <= 60])
df6 = sum([data.loc[data.Age == x, 'Age'].count() for x in unique if x > 60])
colours = ['red', 'blue', 'green', 'yellow','purple', 'orange']


# In[18]:


fig = px.pie(data, values = [df12, df23, df34, df45, df56, df6], names = ["18-20", "20-30", "30-40", "40-50", "50-60", "60+"], title = "Age in percentage", color = colours)
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.show()


# The biggest number of people, who took the survey, were from age 40 to 50 y.o.

# In[19]:


def OverviewPlots(data, nGraphShown, nGraphPerRow):
    nunique = data.nunique()
    data = data[[col for col in data[2:] if nunique[col] > 1 and nunique[col] < 60]]
    nRow, nCol = data.shape
    columnNames = list(data)
    nGraphRow = (nCol + nGraphPerRow - 1) // nGraphPerRow
    plt.figure(figsize = (4 * nGraphPerRow, 6 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columndata = data.iloc[:, i]
        valueCounts = columndata.value_counts()
        valueCounts.plot.bar()
        plt.ylabel('Number of people')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()


# In[20]:


OverviewPlots(data, 8, 4)


# General information about given dataset.

# In[21]:


plt.figure(figsize=(12,6))
sns.swarmplot(y=data['Age'],x=data['Sex'],hue=data['Do you engage in oral sex?'])
plt.show()


# This graph shows us answers to the survey and with their age and sex. As we see in it, in most cases both sides were engaged in oral sex with mutual agreement. Although, as we can see with men, the other significant part initiated it on their own decision, whereas on the women side it is clear, that mutual agreement is in a leading position and many of them didn't have vaginal sex nor anal sex. Moreover, as the age is getting bigger it becomes more likely that people don't remember being engaged in oral sex or didn't participate in it at all.

# ## Hypothesis

# In general, people mostly do anal sex and for them, it is not important, whether they have eye contact or not (especially for men). Moreover, my assumption is that sex is popular during University life and most people do it in the age form 20-40 years. And women are the most interested part in holding such an event.

# In[22]:


fig = px.pie(data, values = data["Sex"].value_counts(), names = data["Sex"].unique(), title = "Sex comparison")
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.show()


# As we can see from the pie-chart, the most popular sex in this survey is men.

# In[23]:


plot1 = plt.figure(1)
x = data['Age']
plt.grid(axis='x')
plt.xlabel('Age')
plt.ylabel('Number of people')
plt.title('Age variety')
plt.xticks(np.arange(10, 70, 5))

hist_plot = plt.hist(x, bins = 36, ec='black')


# The most popular age to have sex is from 40 to 45 y.o.

# In[24]:


plot1 = plt.figure(4)
x = data['Education']
hist_plot = plt.hist(x, bins=np.arange(5)-0.5, ec='black')
plt.ylabel('Number of people')
plt.title('Education variety')
plt.xticks(size = 8, rotation=0)


# The most popular time to have sex is during Secondary education.

# In[25]:


plot1 = plt.figure(5)
df_men = data.loc[data['Sex'] == 'Male']
x = df_men['Do you engage in oral sex?']

df_women = data.loc[data['Sex'] == 'Female']
y = df_women['Do you engage in oral sex?']

plt.hist(x, bins=np.arange(7)-0.7, rwidth=0.4, color='black', label='men', ec='black')
plt.hist(y, bins=np.arange(7)-0.3, rwidth=0.4, color='pink', label='women', ec='black')

plt.legend(loc='upper right')
plt.title('Do you engage in oral sex?')
plt.ylabel('Number of people')
plt.xticks(size = 8, rotation=90)


# Most of the people wanted sex mutually, both male and female.

# In[26]:


plot1 = plt.figure(6)
data_men = data.loc[data['Sex'] == 'Male']
x = data_men['Kind of sex and eye contact']

data_women = data.loc[data['Sex'] == 'Female']
y = data_women['Kind of sex and eye contact']

plt.hist(x, bins=np.arange(8)-0.7, rwidth=0.4, color='black', label='men', ec='black')
plt.hist(y, bins=np.arange(8)-0.3, rwidth=0.4, color='pink', label='women', ec='black')
plt.legend(loc='upper right')
plt.title('Kind of sex and eye contact')
plt.ylabel('Number of people')
plt.xticks(size = 8, rotation=90)


# It is clear that the most popular sex variant is vaginal sex with straight eye contact.

# ## Conclusion (+ hyphothesis check)

# So, as an overview, my hypothesis was incorrect. Basically, when the mutual agreement occur, it is more likely that both genders will agree to have oral sex. Moreover, eye contact plays a great role in sex, and especially in vaginal sex. The most popular age to have sex is vaginal and the most popular age to hold such an event is 40-45 y.o.

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
import seaborn as sns
import os
arr =os.listdir()


# # importing data

# In[151]:


covid_19_india = pd.read_csv(r"C:\Users\sumanth\Downloads\covid_19_india.csv")
covid_statewise=pd.read_csv(r"C:\Users\sumanth\Downloads\covid_vaccine_statewise.csv")
covid_statewisesetting=pd.read_csv(r"C:\Users\sumanth\Downloads\StatewiseTestingDetails.csv")


# In[152]:


covid_19_india.head()


# In[153]:


covid_statewisesetting.head()


# In[154]:


covid_19_india.dtypes


# In[155]:


covid_statewise.columns


# # converting date columns to datetime types

# In[156]:


covid_19_india['Date']=covid_19_india['Date'].astype('datetime64')
covid_statewise['Updated On']=covid_statewise['Updated On'].astype('datetime64')
covid_statewisesetting['Date']=covid_statewisesetting['Date'].astype('datetime64')


# # deriving new matrices 
# 

# In[157]:


covid_19_india['Year']=covid_19_india['Date'].dt.year
covid_statewise['Year']=covid_statewise['Updated On'].dt.year
covid_statewisesetting['Year']=covid_statewisesetting['Date'].dt.year
covid_19_india['Month']=covid_19_india['Date'].dt.month
covid_statewise['Month']=covid_statewise['Updated On'].dt.month
covid_statewisesetting['Month']=covid_statewisesetting['Date'].dt.month
covid_19_india['Day of Month']=covid_19_india['Date'].dt.day
covid_statewise['Day of Month']=covid_statewise['Updated On'].dt.day
covid_statewisesetting['Day of Month']=covid_statewisesetting['Date'].dt.day


# In[158]:


covid_statewisesetting.head()


# In[159]:


from  IPython.display import display


# In[160]:


All ='All'
def unique_all(array):
    unique = array.unique().tolist()
    unique.sort()
    unique.insert(0,All)
    return unique
    


# In[161]:


dropdown_year = widgets.Dropdown(options = unique_all(covid_19_india.Year))
output_year = widgets.Output()

def dropdown_year_eventhandler(change):
    output_year.clear_output()
    with output_year :
        if(change.new == All):
            display(covid_19_india)
        else :
            display(covid_19_india[covid_19_india.year == change.new])
dropdown_year.observe(dropdown_year_eventhandler,names='value')


# In[162]:


display(dropdown_year)


# In[163]:


display(output_year)


# In[164]:


output = widgets.Output()
plot_output = widgets.Output()
plot_output1 = widgets.Output()

dropdown_year = widgets.Dropdown(options = unique_all(covid_19_india.Year))
dropdown_state = widgets.Dropdown(options = unique_all(covid_19_india['State/UnionTerritory']))
def common_filtering(year,state):
    output.clear_output()
    plot_output.clear_output()
    plot_output1.clear_output()
    if (year == All)&(state == All):
        common_filter = covid_19_india
    elif (year == All):
        common_filter = covid_19_india[covid_19_india['State/UnionTerritory']== state]
    elif (state ==All):
        common_filter = covid_19_india[covid_19_india.Year == year]
        with plot_output1:
            plt.figure(figsize=(10,8))
            sns.barplot(common_filter['Confirmed'],common_filter['State/UnionTerritory'],)
            plt.show()
            
    else :
        common_filter = covid_19_india[(covid_19_india.year == year)&
                                      (covid_19_india['State/UnionTerritory']==state)]
    with output :
        display(common_filter)
    with plot_output:
        sns.countplot(common_filter['Month'])
        plt.show()
    with plot_output :
        valu = list(common_filter['Month'].value_counts())
        labels =list(set(common_filter['Month']))
        
        fig1, ax1 = plt.subplots()
        ax1.pie(valu,labels = labels, autopct = '%1.1f%%',
               shadow =True, starting =90)
        ax1.axis('equal')
        plt.show()
def dropdown_year_eventhandler(change):
    common_filterimg(change.new,dropdown_state.value)
def dropdown_state_eventhandler(change):
    common_filtering(dropdown_year.value,change.new)
dropdown_year.observe(
dropdown_year_eventhandler,names= 'value')
dropdown_state.observe(
dropdown_state_eventhandler,names='value')
    


# In[165]:


item_layout = widgets.Layout(margin='0 0 50px 0')


# In[166]:


input_widgets = widgets.HBox([dropdown_year,dropdown_state])


# In[167]:


tab =widgets.Tab([output,plot_output],layout = item_layout)
tab.set_title(0,'Dataset Exploration')
tab.set_title(1,'Count plot')
tab.set_title(2,'State Wise Analysis')


# In[168]:


dashboard = widgets.VBox([input_widgets, tab])
display(dashboard)


# In[169]:


input_widgets = widgets.HBox([dropdown_year , dropdown_state])


# In[170]:


tab = widgets.Tab([output,plot_output,plot_output1],layout = item_layout)
tab.set_title(0,'Dataset Exploration')
tab.set_title(1,'Count plot')
tab.set_title(2, 'State Wise Analysis')


# In[171]:


dashboard = widgets.VBox([input_widgets,tab])
display(dashboard)


# In[ ]:





# In[ ]:





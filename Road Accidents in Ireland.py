#!/usr/bin/env python
# coding: utf-8

# #  importing Libraries

# In[61]:


# importing Libraries

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
plt.style.use('ggplot')
import numpy as np


# # importing Excel files into each Dataframe

# In[169]:


###1

# Reading Excel File and naming the object called 'county'


county = pd.read_excel("Road Accidents.xlsx", sheet_name='Counties', index_col=None)
county.head()


# In[170]:


###2

# Reading Excel File and naming the object called 'driver'


driver = pd.read_excel("Road Accidents.xlsx", sheet_name='Car Drivers', index_col=None)
driver.head()


# In[171]:


###3

# Reading Excel File and naming the object called 'month'


month = pd.read_excel("Road Accidents.xlsx", sheet_name='Months', index_col=None)
month.head()


# In[172]:


###4

# Reading Excel File and naming the object called 'user'


user= pd.read_excel("Road Accidents.xlsx", sheet_name='Road User', index_col=None)
user.head()


# # Renaming the columns
# 
# We are renaming the columns of various DataFrame objects that presumably hold different worksheets of data related to road fatalities, accidents, drivers, and safety measures like seatbelts.
# 
# Renaming columns is often a necessary step in data cleaning and preparation because it helps avoid potential errors, and improves the readability and understanding of the data and the code.

# In[173]:


##. Need to rename the columns for every object name because I got an error saying there is no attribute.


# for county worksheet
col_name =county.columns[2]
county=county.rename(columns = {col_name:'Fatal Collisions'})


col_name =county.columns[3]
county=county.rename(columns = {col_name:'Injury Collisions'})


col_name =county.columns[4]
county=county.rename(columns = {col_name:'Killed Casualties'})


col_name =county.columns[5]
county=county.rename(columns = {col_name:'Injured Casualties'})


#For Months worksheet

col_name =month.columns[2]
month=month.rename(columns = {col_name:'Road Fatalities'})


#For Road User Worksheet


col_name =user.columns[3]
user=user.rename(columns = {col_name:'Age Group'})

col_name =user.columns[4]
user=user.rename(columns = {col_name:'Killed Casualties'})


#For Driver Worksheet

col_name =driver.columns[1]
driver=driver.rename(columns = {col_name:'Gender'})

col_name =driver.columns[2]
driver=driver.rename(columns = {col_name:'Age Group'})

col_name =driver.columns[3]
driver=driver.rename(columns = {col_name:'All Drivers of Cars Involved in Fatal and Injury Collisions (Number)'})


# ## 1.  Annual Fatalities in Road Accidents in Ireland 

# In[ ]:





# In[68]:


# Creating a dataframe for Number of people killed in Road Accident in Ireland during 2005-2012
Total = county.loc[(county.County.isin(['All Counties'])) , ['Year', 'County', 'Killed Casualties']]
Total


# ### Dealing with duplicates value in this dataframe

# **Duplicate Entries for 2010**
# 
# There are two rows for the year 2010 with different 'Killed Casualties' values (212 and 186).This seems like a data entry mistake
# 
# **Missing Data for 2011**: 
# 
# There is no row for the year 2011. If the dataset is supposed to include yearly data from 2005 to 2012, the absence of data for 2011 may indicate missing data.
# 
# ##### (Source for the real value)  https://en.wikipedia.org/wiki/List_of_road_traffic_accidents_deaths_in_the_Republic_of_Ireland_by_year 
# 
# 

# the correct value for **'Killed Casualties' in 2011 is 186**.
# It seems like a data entry error occurred for the year 2011, mistakenly entered as 2010.

# In[69]:


# Find the index of the row where Year is 2010 and Killed Casualties is 186
index_to_correct = Total[(Total["Year"] == 2010) & (Total["Killed Casualties"] == 186)].index

# Correct the Year to 2011
Total.loc[index_to_correct, "Year"] = 2011

# Verify the correction
print(Total[(Total["Year"] == 2011)])


# In[70]:


# Dispaly the updated dataframe
Total


# In[ ]:


# Creating two graphs on Annual Fatalities in Road Accidents in Ireland (2005-2012)


# In[71]:


# Create a new figure with a specified size (width, height)
plt.figure(figsize=(12, 8))

# Specify the label 'Killed Casualties'
plt.plot(Total["Year"], Total["Killed Casualties"], color='red', label='Killed Casualties') 

# Add a grid with white lines
plt.grid(True, color='white')

# Set the plot background color to light grey
plt.gca().set_facecolor('lightgrey')

# Add axis labels with specified font size, font weight and label padding
plt.xlabel('Year', fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel('Killed Casualties', fontsize=14, fontweight='bold', labelpad=15)

# Add a title with specified font size and font weight
plt.title('Annual Fatalities in Road Accidents in Ireland (2005-2012)', fontsize=16, fontweight='bold')

# Add a legend at the upper left corner with specified font size, without a title
plt.legend(loc="upper left",  prop={'size': 12, 'weight':'bold'}, bbox_to_anchor=(1,1))

# Show the plot
plt.show()


# In[ ]:


# Another way plotting of Annual Fatalities in Road Accidents in Ireland (2005-2012)


# In[72]:


import seaborn as sns
import matplotlib.pyplot as plt

# Create a new figure with a specified size (width, height)
plt.figure(figsize=(12, 8))

# Create a bar chart of 'Killed Casualties' over 'Year' with no error bars, in the color salmon
barplot = sns.barplot(x="Year", y="Killed Casualties", data=Total, color='salmon', ci=None)

# Set the plot style to 'darkgrid' which means the plot will have a grid with dark colored lines
sns.set_style("darkgrid")

# Set the label for the x-axis, the label for the y-axis, and the title of the plot 
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Killed Casualties', fontsize=14, fontweight='bold')
plt.title('Annual Fatalities in Road Accidents in Ireland (2005-2012)', fontsize=16, fontweight='bold')

# Add annotations to each bar
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.0f'), 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     ha = 'center', va = 'center', 
                     xytext = (0, 9), 
                     textcoords = 'offset points')

# Show the plot
plt.show()


# ### Q1. How has the number of 'Killed Casualties' changed over time from 2004 to 2012? 
# 
# #### Are there any significant increases or decreases? Can we identify any year-on-year trends? 
# 
# 
# **ANS:** There is a steady decrease in 'Killed Casualties' over the time period from 2005 to 2012. The number has reduced from **396** in **2005** to **162** in **2012**. This represents a **decrease of more than 50%**. From the given data, it seems that every year the number of 'Killed Casualties' decreases. 
# 
# Currently, we don't have access to the additional data required to investigate further factors. However, should this data become available, we will certainly extend our investigation to gain more comprehensive insights.
# 
# 
# ### Q2 Which year had the highest number of 'Killed Casualties'? 
# 
# #### Which year had the lowest? 
# 
# **ANS:** 
# The year with the highest number of 'Killed Casualties' is **2005, with a total of 396 casualties**. 
# The year with the lowest number is **2012, with a total of 162 casualties**.
# 
# Remember that while this data shows a promising trend, it's crucial to understand that the reasons behind these decreasing numbers can be multifactorial.It could be due to improved road safety measures, better vehicle safety technology, effective traffic law enforcement, and so on. Further investigation and more detailed data would be necessary to ascertain the causes behind this trend.
# 
# 
# 
# 

# In[ ]:





# ## 2.  Identifying Irish Counties with the Highest and Lowest Road Fatalities among Road Users 

# In[73]:


# Display this dataframe
county


# In[74]:


# Making new dataframe that shows only the 'Year', County' and 'Killed Casualities'
allcounty = county.loc[(~ county.County.isin(['All Counties'])) & ( county.Year == year), ['Year', 'County', 'Killed Casualties']]
allcounty


# In[ ]:


# Display the Top 5 counties with the most road deaths


# In[75]:


# Define years
years = range(2005, 2013) # this will include all years from 2005 through 2012

# Initialize an empty dictionary to store the results
top_counties = {}

# Loop over years
for year in years:
    # Filter the data for the specific year
    allcounty = county.loc[(~ county.County.isin(['All Counties'])) & ( county.Year == year), ['Year', 'County', 'Killed Casualties']]
    
    # Merge only year and counties using Panda Series and Np.Array
    a = pd.Series((np.array(allcounty['Killed Casualties'])), index=(allcounty['County']))
    
    # Find the top 3 Irish counties with the most Road Deaths
    top_counties_for_year = a.nlargest(5)

    # Add the result to the dictionary
    top_counties[year] = top_counties_for_year.index.tolist()

# Print the result
for year, counties in top_counties.items():
    print(f"The top 5 counties with the most road deaths in {year} were {', '.join(counties)}.")


# In[ ]:


# Display the 5 counties with the fewest road deaths


# In[76]:


# Initialize an empty dictionary to store the results
lowest_counties = {}

# Loop over years
for year in years:
    # Filter the data for the specific year
    allcounty = county.loc[(~ county.County.isin(['All Counties'])) & ( county.Year == year), ['Year', 'County', 'Killed Casualties']]
    
    # Merge only year and counties using Panda Series and Np.Array
    a = pd.Series((np.array(allcounty['Killed Casualties'])), index=(allcounty['County']))
    
    # Find the top 5 Irish counties with the least Road Deaths
    lowest_counties_for_year = a.nsmallest(5)

    # Add the result to the dictionary
    lowest_counties[year] = lowest_counties_for_year.index.tolist()

# Print the result
for year, counties in lowest_counties.items():
    print(f"The five counties with the least road deaths in {year} were {', '.join(counties)}.")


# In[77]:


# Define years
years = range(2005, 2014) # this will include all years from 2005 through 2013

# Initialize an empty dictionary to store the results
top_counties = {}
lowest_counties = {}

# Loop over years
for year in years:
    # Filter the data for the specific year
    allcounty = county.loc[(~ county.County.isin(['All Counties'])) & ( county.Year == year), ['Year', 'County', 'Killed Casualties']]
    
    # Merge only year and counties using Panda Series and Np.Array
    a = pd.Series((np.array(allcounty['Killed Casualties'])), index=(allcounty['County']))
    
    # Find the top 5 counties with the most Road Deaths
    top_counties_for_year = a.nlargest(5)
    
    # Find the 5 counties with the fewest Road Deaths
    lowest_counties_for_year = a.nsmallest(5)

    # Add the result to the dictionaries
    top_counties[year] = top_counties_for_year
    lowest_counties[year] = lowest_counties_for_year




# In[ ]:


# Plotting the graph for 'The Top 5 counties with the most road deaths'


# In[78]:


import matplotlib.pyplot as plt
import numpy as np

# Create a new figure with a specified size (width, height)
fig, axs = plt.subplots(4, 2, figsize=(15, 20)) 

# Flatten the axes array to easily iterate over it
axs = axs.flatten()

# Define years
years = range(2005, 2013)

# Plotting a bar chart for each year
for i, year in enumerate(years):
    counties = top_counties[year]  # Replace 'least_counties' with 'top_counties'
    bars = axs[i].bar(counties.index, counties.values, color='red', width=0.5)  # Change color to red, make bars narrower
    
    # Display the actual values on top of the bars
    for bar in bars:
        yval = bar.get_height()
        axs[i].text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

    # Add a grid with white lines
    axs[i].grid(True, color='white')

    # Set the plot background color to light grey
    axs[i].set_facecolor('lightgrey')

    
    # Add axis labels with specified font size, font weight and label padding
    axs[i].set_xlabel('County', fontsize=14, fontweight='bold', labelpad=15)
    axs[i].set_ylabel('Road Deaths', fontsize=14, fontweight='bold', labelpad=15)

    # Add a title with specified font size and font weight
    axs[i].set_title(f'Most Road Deaths in {year}', fontsize=16, fontweight='bold')  # Updated title

# Adjust space between subplots
plt.subplots_adjust(hspace=0.5, wspace=0.3)

# Show the plot
plt.show()




# In[ ]:


# Plotting the graph for 'The  5 counties with the most fewest road deaths'


# In[79]:


import matplotlib.pyplot as plt
import numpy as np

# Create a new figure with a specified size (width, height)
fig, axs = plt.subplots(4, 2, figsize=(15, 20)) 

# Flatten the axes array to easily iterate over it
axs = axs.flatten()

# Define years
years = range(2005, 2013)

# Plotting a bar chart for each year
for i, year in enumerate(years):
    counties = lowest_counties[year]

    # Determine the maximum number of counties across all years
    max_counties = max([len(counties) for counties in lowest_counties.values()])
    # Ensure the same number of bars in each plot
    while len(counties) < max_counties:
        # Add an empty county to the current year
        counties = counties.append(pd.Series({f'Empty {len(counties)+1}': 0}))

    bars = axs[i].bar(counties.index, counties.values, color='skyblue', width=0.5)  # Set the width of bars to 0.5
    
    # Display the actual values on top of the bars
    for bar in bars:
        yval = bar.get_height()
        axs[i].text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

    # Add a grid with white lines
    axs[i].grid(True, color='white')

    # Set the plot background color to light grey
    axs[i].set_facecolor('lightgrey')

    # Set y-ticks to integer values
    axs[i].set_yticks(np.arange(0, max(counties.values)+1, 1))

    # Add axis labels with specified font size, font weight and label padding
    axs[i].set_xlabel('County', fontsize=14, fontweight='bold', labelpad=15)
    axs[i].set_ylabel('Road Deaths', fontsize=14, fontweight='bold', labelpad=15)

    # Add a title with specified font size and font weight
    axs[i].set_title(f'Fewest Road Deaths in {year}', fontsize=16, fontweight='bold')  # Updated title

# Adjust space between subplots
plt.subplots_adjust(hspace=0.5, wspace=0.3)

# Show the plot
plt.show()





# ### Q1. Which counties had the highest and lowest casualties?
# 
# **ANS:** From the data you provided, it seems that **Dublin, Cork, and Galway often have the highest numbers of road deaths**, while counties like **Leitrim, Longford, and Carlow frequently have the fewest**. Below are some further considerations based on your questions:
# 
# From 2005 to 2012, **Dublin and Cork consistently had the most road deaths**, while **Leitrim and Longford  often had the fewest**. 
# 
# ### Q2. The comparison with Overall Fatalities? 
# 
# **ANS:** From the data you provided, we can see that the counties with the most road deaths contribute significantly to the overall total. For example, **in 2005, the top 5 counties for road deaths (Dublin, Cork, Meath, Donegal, and Wexford) had a total of 158 deaths**, which is around 40% of the overall total of 396 for that year.
# 
# ### Q3. What are the possible factors might be contributing to the high number of road deaths in these counties?
# 
# **ANS**: 
# 
# Without more detailed information, it's hard to say what factors might be contributing to the high number of road deaths in these counties. Possible factors could include:
# 
# **Population Density**: Dublin, Cork, and Galway are some of the most populated counties in Ireland, which could lead to higher traffic volumes and, potentially, more accidents.
# 
#  **Urban vs Rural**: Urban areas may have more traffic and pedestrians, while rural areas may have more dangerous roads due to higher speed limits, less lighting, or poorer road conditions.
# 
# **Road Infrastructure**: The quality and design of the road infrastructure may also play a role. Counties with poor road infrastructure may have higher rates of road deaths.
# 
# To get a clearer picture, it would be useful to analyze data on traffic volumes, population densities, types of roadways, and other relevant factors in these counties. This would allow you to better understand the specific factors contributing to the high numbers of road deaths.
# 
# 

# In[ ]:





# ##  3, Road User Category and Associated Fatalities

# In[80]:


# Displaying Dataframe
user.head()


# In[81]:


# Displaying all type of 'Road Users'

print(user['Road User'].unique())


# In[82]:


# Using this copied DataFrame for  other data analysis tasks.

user_copy = user.copy()


# In[83]:


# Displaying the new dataframe
user_copy.head()


# In[84]:


# Only selecting the chosen 'Road Users', The Year and 'illed Casualties' 
road_users = ['Pedestrians', 'Pedal cyclists', 'Motor cyclists', 'Car drivers', 'Car passengers']
selected_columns = ['Road User', 'Year' ,'Killed Casualties']

# New datafram showing the updated columns 
usertype = user[user['Road User'].isin(road_users)][selected_columns]




# In[85]:


# Displaying the updated dataframe
usertype


# In[86]:


# Group by 'Road User' and 'Year' and get the sum of 'Killed Casualties'

grouped_usertype = usertype.groupby(['Road User', 'Year'])['Killed Casualties'].sum().reset_index()
print(grouped_usertype)


# In[87]:


# Filter out rows where 'Year' is 'Total'
grouped_usertype = grouped_usertype[grouped_usertype['Year'] != 'Total']

# Create a new figure with a specified size (width, height)
plt.figure(figsize=(10, 6))

# Get the unique 'Road User' values
road_users = grouped_usertype['Road User'].unique()

# Plotting a line for each 'Road User'
for user in road_users:
    user_df = grouped_usertype[grouped_usertype['Road User'] == user]
    plt.plot(user_df['Year'], user_df['Killed Casualties'], marker='o', label=user)

# Add a grid with white lines
plt.grid(True, color='white')

# Set the plot background color to light grey
plt.gca().set_facecolor('lightgrey')

# Add axis labels with specified font size, font weight and label padding
plt.xlabel('Year', fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel('Killed Casualties', fontsize=14, fontweight='bold', labelpad=15)

# Add a title with specified font size and font weight
plt.title('Annual Fatalities by Road User Type (2005-2012)', fontsize=16, fontweight='bold')

# Add a legend at the upper left corner with specified font size, without a title
plt.legend(loc="upper left",  prop={'size': 12, 'weight':'bold'}, bbox_to_anchor=(1,1))

# Show the plot
plt.show()


# In[88]:


# Create a new figure with a specified size (width, height)
fig, axs = plt.subplots(3, 2, figsize=(15, 20)) 

# Flatten the axes array to easily iterate over it
axs = axs.flatten()

# Define color dictionary
color_dict = {
    'Car drivers': 'red',
    'Car passengers': 'blue',
    'Motor cyclists': 'purple',
    'Pedal cyclists': 'grey',
    'Pedestrians': 'yellow'
}

# Plotting a line for each 'Road User'
for i, user in enumerate(road_users):
    user_df = grouped_usertype[grouped_usertype['Road User'] == user]
    axs[i].plot(user_df['Year'], user_df['Killed Casualties'], marker='o', label=user, color=color_dict[user])

    # Add a grid with white lines
    axs[i].grid(True, color='white')

    # Set the plot background color to light grey
    axs[i].set_facecolor('lightgrey')

    # Add axis labels with specified font size, font weight and label padding
    axs[i].set_xlabel('Year', fontsize=14, fontweight='bold', labelpad=15)
    axs[i].set_ylabel('Killed Casualties', fontsize=14, fontweight='bold', labelpad=15)

    # Add a title with specified font size and font weight
    axs[i].set_title('Annual Fatalities Breakdown by ' + user, fontsize=16, fontweight='bold')

# Remove empty subplots
fig.delaxes(axs[5])

# Adjust space between subplots
plt.subplots_adjust(hspace=0.5, wspace=0.3)

# Show the plot
plt.show()


# ### Q1. Who are the most vulnerable road users?
# 
# **ANS**: Looking strictly at the numbers, "**Car drivers**" have the **highest number of killed casualties across the years**, followed by "**Pedestrians", "Car passengers", "Motorcyclists", and "Pedal cyclists**". However, this does not necessarily mean that car drivers are the most vulnerable; it may simply mean that there are more car drivers on the road. To assess vulnerability, we would need additional data such as the total number of each type of road user or the total miles driven/travelled.
# 
# ### Q2. What are the trends in fatalities among different road user types over time?
# 
# **ANS**: From 2005 to 2012, all categories of road users have seen a decrease in the number of fatalities. 
# 
# For "**Car drivers"**, fatalities decreased from 426 in 2005 to 192 in 2012. 
# 
# For "**Car passengers**", fatalities decreased from 227 in 2005 to 75 in 2012. 
# 
# For "**Motorcyclists**", fatalities decreased from 165 in 2005 to 57 in 2012.
# 
# For "**Pedal cyclists**", fatalities decreased from 27 in 2005 to 24 in 2012 (with some fluctuation in between). 
# 
# For "**Pedestrians**", fatalities decreased from 215 in 2005 to 87 in 2012.
# 
# 
# ### Q3. Which road user type saw the biggest decrease in deaths over this period?
# 
# **ANS**: Based on the data provided, none of the road user types saw an increase in deaths over this period. All categories saw a decrease in fatalities from 2005 to 2012.
# 
# ### Q4.  Which road user type saw the biggest increase in deaths over this period?
# 
# **ANS**: Based on the data provided, none of the road user types saw an increase in deaths over this period. All categories saw a decrease in fatalities from 2005 to 2012.
# 
# ###  Q5. What percentage of total road deaths does each road user type constitute?
# 

# In[89]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Your Data
df = pd.DataFrame({
    'Road User': ['Car drivers', 'Car passengers', 'Motor cyclists', 'Pedal cyclists', 'Pedestrians'],
    'Year': ['Total', 'Total', 'Total', 'Total', 'Total'],
    'Killed Casualties': [669, 389, 225, 74, 386]
})

# Create a new figure with specified size (width, height)
fig, ax = plt.subplots(figsize=(10, 10))

# Define your own colors
colors = ['red', 'aqua', 'green', 'yellow', 'orange']

# Explode parameters
explode = [0.1] * len(df) # change to the values you want to highlight, 0.1 is just an example

# Create a pie chart for the specific year
ax.pie(df['Killed Casualties'], labels=df['Road User'], autopct='%1.1f%%', startangle=140, shadow=True, explode=explode, colors=colors)
ax.set_title('Total Road Deaths by User Type from 2005-2012', fontsize=14, weight='bold')

# Show the plot
plt.show()



# **ANS**: This could help identify the groups most at risk.
# 
# Based on the provided results, the answer to the data question "What percentage of total road deaths does each road user type constitute?" is:
# 
# 1. **- Car drivers** constitute **38.4%** of the total road deaths.
# 2. **- Pedestrians** constitute **22.1%** of the total road deaths.
# 3. **- Car passengers** constitute **22.3%** of the total road deaths.
# 4. **-  Motorcyclists** constitute **12.9%** of the total road deaths.
# 5. **-  Pedal cyclists** constitute **4.2%** of the total road deaths.
# 
# These percentages reflect the proportion of total road deaths for each road user type from 2005 to 2012.
# 
# 

# ###  Q6. Are there any correlations between the different road user types?
# 
# #### For instance, does a decrease in deaths among car drivers correlate with an increase in deaths among pedestrians, or vice versa?
# 

# In[90]:


# Convert your data into a DataFrame
data = {
    'Year': [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012] * 5,
    'Road User': ['Car drivers'] * 8 + ['Car passengers'] * 8 + ['Motor cyclists'] * 8 + ['Pedal cyclists'] * 8 + ['Pedestrians'] * 8,
    'Killed Casualties': [426, 435, 328, 327, 321, 237, 195, 192, 227, 234, 182, 143, 117, 138, 90, 75, 165, 87, 98, 87, 75, 51, 54, 57, 27, 27, 42, 39, 21, 15, 27, 24, 215, 210, 239, 144, 120, 132, 141, 87]
}

df = pd.DataFrame(data)

# Pivot the data so each type of road user is a column
pivot_df = df.pivot(index='Year', columns='Road User', values='Killed Casualties')

# Calculate the correlation
corr_df = pivot_df.corr()

# Create a new figure with a specified size
plt.figure(figsize=(10, 10))

# Use seaborn's heatmap function to plot the data with red colormap
sns.heatmap(corr_df, cmap="coolwarm", annot=True, fmt=".2f", linewidths=.5)

# Add a title
plt.title('Heatmap of Road User Type Fatalities Correlation (2005-2012)', fontsize=16, fontweight='bold')

# Show the plot
plt.show()


# **ANS:** Analyzing the data in response to these questions could provide valuable insights into road safety issues and help to guide interventions and policy decisions
# 
# 
# 1. The "**Car drivers**" and "**Car passengers**" correlation is displayed as a **strong positive correlation**, represented by a warm color on the heatmap (**0.93**).
# <br>
# 
# 2. Similarly, "**Car passengers**" and "**Pedestrians**" show a **strong positive correlation (0.87)**, also shown by a warm color.
# <br>
# 
# 3.  "**Motor cyclists**" show **moderate positive correlations with "Car drivers" (0.78)**, "**Car passengers" (0.75), and "Pedestrians" (0.68)**, suggested by a somewhat warm color.
# <br>
# 
# 4.  The correlation between "**Pedal cyclists**" and **other road user types is weaker**, as indicated by the cooler colors. **The strongest correlation "Pedal cyclists" has is with "Pedestrians" (0.53).**
# <br>
# 
# 5.  All road user types have a correlation of 1 with themselves, as expected.
# <br>
# 
# Again, please remember that while these correlations may suggest patterns, they don't prove causation. There could be numerous factors contributing to these observed relationships, including increased overall traffic activity, similar risk factors affecting multiple user types, or even coincidences. Further analysis would be needed to understand the reasons behind these correlations.
# 

# In[ ]:





# ## 4. Annual Casualty Counts by Age Group (2005-2012)
# 

# In[91]:


# Age Group #

user_copy.head()


# In[98]:


# Print unique values for Age Group
print(user_copy['Age Group'].unique())


# In[99]:


# Print unique values for Road User
print(user_copy['Road User'].unique())


# In[101]:


# Print unique values for Gender
print(user_copy['Gender'].unique())


# In[102]:


# Make a new dataframe that only selects 'All road users'
all_road_users_df = user_copy[user_copy['Road User'].str.strip() == 'All road users']
all_road_users_df


# In[103]:


# Update the dataframe that only excludes 'All ages' (Value)
all_road_users_df= all_road_users_df[all_road_users_df['Age Group'].str.strip() != 'All ages']

# Display the updated dataframe
all_road_users_df


# In[104]:


#Display the Unique values for Gender

all_road_users_df['Gender'].unique()


# In[105]:


#Display the Unique values for Age Group

all_road_users_df['Age Group'].unique()


# In[ ]:


# Pivot table


# The code is creating a pivot table that provides the **sum of Killed Casualtie**s for each combination of **Year, Age Group, and Gender**. If there's any combination that doesn't exist in the original data, it fills with 0. After pivoting, it resets the index of the DataFrame to default integers.

# In[119]:


# Creating Pivot table

grouped_df = all_road_users_df.pivot_table(
    values='Killed Casualties', 
    index=['Year', 'Age Group'], 
    columns='Gender', 
    aggfunc=np.sum,
    fill_value=0
).reset_index()


# In[120]:


# Displaying Pivot table
grouped_df


# In[123]:


# Using this copied DataFrame for further performing additional task of  pivot table
grouped_df_copy = grouped_df.copy()


# In[124]:


# Display this pivot table
grouped_df_copy


# In[125]:


# Create a new column 'Killed Casualties' in 'grouped_df_copy' DataFrame, 
# which is the sum of 'Male' and 'Female' columns for each row
grouped_df_copy['Killed Casualties'] = grouped_df_copy['Male'] + grouped_df_copy['Female']


# In[126]:


# Group the 'grouped_df_copy' DataFrame by 'Year' and 'Age Group',
# calculate the sum of 'Killed Casualties' for each group,
# and reset the index of the resulting DataFrame.
grouped_by_year_age = grouped_df_copy.groupby(['Year', 'Age Group'])['Killed Casualties'].sum().reset_index()


# In[127]:


# Set the max rows to be displayed to a high number, e.g., 100
pd.set_option('display.max_rows', 100)

# Now when display the dataframe, it should show all rows
print(grouped_by_year_age)


# In[ ]:


# Creating barplot with two suplots


# This will visualize the number of fatalities per age group over different years. The two subplots separate the data into two time periods for clearer comparison and analysis.

# In[133]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Order Age Groups for better visualization
age_order = ["0 - 5 years", "6 - 9 years", "10 - 14 years", "15 - 17 years", "18 - 20 years",
             "21 - 24 years", "25 - 34 years", "35 - 44 years", "45 - 54 years",
             "55 - 64 years", "65 years and over"]

grouped_by_year_age['Age Group'] = pd.Categorical(grouped_by_year_age['Age Group'], categories=age_order, ordered=True)
grouped_by_year_age = grouped_by_year_age.sort_values(['Year', 'Age Group'])

# Create a color palette
colors = sns.color_palette("hsv", len(age_order))

# Split the data into two subsets
grouped_by_year_age_1 = grouped_by_year_age[grouped_by_year_age['Year'] <= 2008]
grouped_by_year_age_2 = grouped_by_year_age[grouped_by_year_age['Year'] > 2008]

# Create a new figure with a specified size (width, height) and two subplots
fig, axes = plt.subplots(2, 1, figsize=(20, 25))

for subset, ax, title in zip([grouped_by_year_age_1, grouped_by_year_age_2], axes, ['Fatalities per Age Group Over Years (2005-2008)', 'Fatalities per Age Group Over Years (2009-2012)']):
    # Use barplot in seaborn
    sns.barplot(data=subset, x='Year', y='Killed Casualties', hue='Age Group', palette=colors, ax=ax)

    # Add a grid with white lines
    ax.grid(True, color='white')

    # Set the plot background color to light grey
    ax.set_facecolor('lightgrey')

    # Add axis labels with specified font size, font weight and label padding
    ax.set_xlabel('Year', fontsize=14, fontweight='bold', labelpad=15)
    ax.set_ylabel('Fatalities', fontsize=14, fontweight='bold', labelpad=15)

    # Add a title with specified font size and font weight
    ax.set_title(title, fontsize=16, fontweight='bold')

    # Add a legend at the upper left corner with specified font size, without a title
    ax.legend(loc="upper left",  prop={'size': 15, 'weight':'bold'}, bbox_to_anchor=(1,1), title='Age Group', title_fontsize='16')



    # Show numbers on top of bars
    for p in ax.patches:
        ax.annotate('{:.0f}'.format(p.get_height()), (p.get_x()+p.get_width()/2, p.get_height()), 
                 ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=10)

# Adjust the layout to make sure everything fits
fig.tight_layout(pad=5.0)

# Show the plot
plt.show()


# In[ ]:


#Age Group with Highest Fatalities: 
#The age group of '25 - 34 years' consistently had a relatively high number of fatalities in each year. Especially in 2005 and 2006, it recorded the highest fatalities of 77 and 79 respectively.

#Age Group with Lowest Fatalities: 
#The age groups '0 - 5 years' and '6 - 9 years' consistently recorded the lowest fatalities across the years.

#Overall Trend: 
#From an initial glance, there seems to be a general trend of decreasing fatalities over the years for most age groups.

#Elderly Age Group: 
#There is an observable trend that the number of fatalities in the '65 years and over' age group remained quite high throughout these years.

#Youth Age Group: 
#The fatalities for the age groups '15 - 17 years' and '18 - 20 years' decreased noticeably over the years.


# In[ ]:


# Another bar plot for displaying the 'Killed Casualties' by 'Age Group' for each individual year from 2005 to 2012


# In[134]:


# Set the dimensions of the plot
fig, axes = plt.subplots(4, 2, figsize=(20, 30))

# Flatten the array of Axes to make it easier to iterate through
axes = axes.flatten()

# Remove any extra subplots
for i in range(len(grouped_by_year_age["Year"].unique()), len(axes)):
    fig.delaxes(axes[i])

# Iterate through each year and create a separate subplot
for i, (year, data) in enumerate(grouped_by_year_age.groupby("Year")):
    # Use barplot in seaborn
    ax = sns.barplot(ax=axes[i], data=data, y='Age Group', x='Killed Casualties', palette="hsv")
    
    # Add axis labels with specified font size, font weight and label padding
    axes[i].set_xlabel('Fatalities', fontsize=14, fontweight='bold', labelpad=15)
    axes[i].set_ylabel('')
    
    # Add a title with specified font size and font weight
    axes[i].set_title(f'Road Deaths for Year {year}', fontsize=16, fontweight='bold')

    # Display the values on the bar graph
    for p in ax.patches:
        ax.text(p.get_width(), 
                p.get_y() + p.get_height()/2, 
                '{:.0f}'.format(p.get_width()), 
                ha='left', 
                va='center')

# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.4, hspace=0.6)

# Show the plot
plt.show()



# ### Q1. Which age group has the highest number of casualties each year?
# 
# **ANS**:
# 
# * In **2005**, the age group with the highest casualties is **25 - 34 years** with **77 casualties**.
# 
# * In **2006**, again the **25 - 34 years** age group has the **highest number of casualties with 79**. 
# 
# * In **2007**, the **25 - 34 years** age group continues to have the **highest number of casualties with 60**. 
# 
# * In **2008**, the age group with the highest casualties is **25 - 34 years** with **44 casualties**. 
# 
# * In **2009**, again the **25 - 34 years** age group has the **highest number of casualties with 52**. 
# 
# * In **2010**, the **25 - 34 years** age group continues to have the **highest number of casualties with 48**. 
# 
# * In **2011**, the age group with the highest number of casualties changes to **65 years and over** with **37 casualties**. 
# 
# * In **2012**, the **25 - 34 years** age group again has the **highest number of casualties with 35**. 
# 
# 
# * It appears that, most years, the **25 - 34 years** age group had the highest number of casualties. However, in **2011**, the **65 years and over** age group had the highest number of casualties.
# 
# 
# 
# ### Q2.  Which age group has seen the most significant increase or decrease in casualties over the years?
# 
# **ANS**:
# 
# From the given data, it's clear that the **total number of casualties for all age groups has been decreasing over the years** from 2005 to 2012. 
# 
# To find the age group that has seen the most significant decrease, we need to subtract the number of casualties in 2005 from the number in 2012 for each age group:
# 
# - **0 - 5 years**: 2 (2012) - 3 (2005) = -1
# - **6 - 9 years**: 1 (2012) - 1 (2005) = 0
# - **10 - 14 years**: 0 (2012) - 5 (2005) = -5
# - **15 - 17 years**: 7 (2012) - 26 (2005) = -19
# - **18 - 20 years**: 12 (2012) - 55 (2005) = -43
# - **21 - 24 years**: 23 (2012) - 54 (2005) = -31
# - **25 - 34 years**: 35 (2012) - 77 (2005) = -42
# - **35 - 44 years**: 16 (2012) - 45 (2005) = -29
# - **45 - 54 years**: 19 (2012) - 31 (2005) = -12
# - **55 - 64 years**: 11 (2012) - 33 (2005) = -22
# - **65 years and over**: 36 (2012) - 56 (2005) = -20
# 
# From these calculations, the **"18 - 20 years" age group has seen the most significant decrease in road casualties**, with a reduction of 43 between 2005 and 2012.
# 
# For the most significant increase, since all groups have seen a decrease or no change (6-9 years), we can say **no age group has seen a significant increase in casualties** over the years 2005 to 2012. 
# 
# 
# ### Q3.  What is the average number of casualties for each age group over the years?
# 
# #### This will give us an overview of which age group is most vulnerable to fatal accidents over the observed period
# 
# * **0 - 5 years**: The sum of casualties from 2005 to 2012 is 38, so the average is **4.75 casualties per year**.
# * **6 - 9 years**: The sum of casualties from 2005 to 2012 is 17, so the average is **2.125 casualties per year**.
# * **10 - 14 years**: The sum of casualties from 2005 to 2012 is 33, so the average is **4.125 casualties per year**.
# * **15 - 17 years**: The sum of casualties from 2005 to 2012 is 111, so the average is **~13.88 casualties per year**.
# * **18 - 20 years**: The sum of casualties from 2005 to 2012 is 221, so the average is **~27.63 casualties per year**.
# * **21 - 24 years**: The sum of casualties from 2005 to 2012 is 295, so the average is **~36.88 casualties per year**.
# * **25 - 34 years**: The sum of casualties from 2005 to 2012 is 436, so the average is **54.5 casualties per year**.
# * **35 - 44 years**: The sum of casualties from 2005 to 2012 is 264, so the average is **33 casualties per year**.
# * **45 - 54 years**: The sum of casualties from 2005 to 2012 is 168, so the average is **21 casualties per year**.
# * **55 - 64 years**: The sum of casualties from 2005 to 2012 is 171, so the average is **~21.38 casualties per year**.
# * **65 years and over**: The sum of casualties from 2005 to 2012 is 352, so the average is **44 casualties per year**.
# 
# From this, we can see that the age group **25 - 34 years** had the **highest average number of casualties per year** during the period from 2005 to 2012, making it the most vulnerable age group to fatal accidents over this time period.
# 
# 
# 
# ###  Q4. How do the total casualties in each age group compare for the years 2005 and 2012?
# 
# **ANS:** Comparing the first and last year can give a snapshot of the changes in the fatality rate of each age group.
# Here is the comparison of total casualties in each age group for the years 2005 and 2012:
# 
# *  '0 - 5 years': **3 casualties in 2005** and **2 in 2012**.
# * '6 - 9 years': **1 casualty in 2005** and **1 in 2012**.
# * '10 - 14 years': **5 casualties in 2005** and **0 in 2012**.
# * '15 - 17 years': **26 casualties in 2005** and **7 in 2012**.
# * '18 - 20 years': **55 casualties in 2005** and **12 in 2012**.
# * '21 - 24 years': **54 casualties in 2005** and **23 in 2012**.
# * '25 - 34 years': **77 casualties in 2005** and **35 in 2012**.
# * '35 - 44 years': **45 casualties in 2005** and **16 in 2012**.
# * '45 - 54 years': **31 casualties in 2005** and **19 in 2012**.
# * '55 - 64 years': **33 casualties in 2005** and **11 in 2012**.
# * '65 years and over': **56 casualties in 2005** and **36 in 2012**.
# 
# The comparison shows a general **decrease in the number of casualties across all age groups** from 2005 to 2012, with the exception of the '45 - 54 years' group where the numbers slightly decreased.
# 
# 
# ### Q5.  What is the trend for each age group's casualties over the years?
# 
# **ANS**: 
# 
# 1. **0 - 5 years**: The casualties have fluctuated over the years with no clear trend. There's a peak in 2006 and then it generally decreases towards 2012.
# 2. **6 - 9 years**: This group's casualties remain relatively constant over the years, with minor increases and decreases but no clear trend.
# 3. **10 - 14 years**: Casualties in this age group peaked in 2008, and then substantially **decreased towards 2012**, showing an overall downward trend.
# 4. **15 - 17 years**: The data shows a **clear downward trend from 2005 to 2012**.
# 5. **18 - 20 years**: There's a **consistent, significant decrease** in the number of casualties in this age group over the years.
# 6. **21 - 24 years**: This age group also shows a **strong decrease in casualties across the years**.
# 7. **25 - 34 years**: Casualties in this age group peaked in 2006, and then they **steadily decrease towards 2012**, showing a downward trend.
# 8. **35 - 44 years**: This age group shows a **clear decline in casualties from 2005 to 2012**.
# 9. **45 - 54 years**: The number of casualties in this group decreases from 2005 to 2011, then slightly increases in 2012, but the overall trend is downward.
# 10. **55 - 64 years**: There is a **general decrease in the number of casualties in this age group from 2005 to 2012**, showing a downward trend.
# 11. **65 years and over**: Casualties in this age group fluctuate over the years with no clear trend. There's a peak in 2006 and then the numbers vary towards 2012. 
# 
# Remember that while these trends provide valuable information about the changes in casualties over the years, they do not explain why these changes have occurred. To gain insights into the causes, further investigation and analysis would be needed.
# 
# 
# ### Q6. What is the total number of casualties for all age groups for each year?
# 
# **ANS**:
# 
# Based on the data you provided, we can calculate the total number of casualties for each year by adding up the casualties from all age groups for that year. Here's the calculation:
# 
# **2005** total casualties = **386**
#  
# **2006** total casualties = **361**
#  
# **2007** total casualties = **330**
#  
# **2008** total casualties = **273**
#  
# **2009** total casualties = **238**
#  
# **2010** total casualties = **207**
#  
# **2011** total casualties = **186**
#  
# **2012** total casualties = **162**
# 
# So, the total number of casualties for all age groups each year are:
# 
# - **2005: 386**
# - **2006: 361**
# - **2007: 330**
# - **2008: 273**
# - **2009: 238**
# - **2010: 207**
# - **2011: 186**
# - **2012: 162**
# 
# The trend shows a **decrease in total road fatalities from 2005 to 2012**.

# ### Q7. Which age group has the highest total number of road fatalities?
# 

# In[137]:


# Compute total killed casualties for each age group
total_casualties_age_group = grouped_by_year_age.groupby('Age Group')['Killed Casualties'].sum()

# Print the results
print(total_casualties_age_group)


# In[ ]:


#Plot the barchart


# In[138]:


# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Create a color palette
colors = sns.color_palette('hsv', len(total_casualties_age_group))

# Create a new figure with a specified size (width, height)
plt.figure(figsize=(10, 6))

# Create a bar plot for the total casualties per age group with different colors for each age group
bars = plt.bar(total_casualties_age_group.index, total_casualties_age_group.values, color=colors)

# Add a grid with white lines
plt.grid(True, color='white')

# Set the plot background color to light grey
plt.gca().set_facecolor('lightgrey')

# Add axis labels with specified font size, font weight and label padding
plt.xlabel('Age Group', fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel('Killed Casualties', fontsize=14, fontweight='bold', labelpad=15)

# Add a title with specified font size and font weight
plt.title('Total Number of Killed Casualties for Each Age Group (2005-2012)', fontsize=16, fontweight='bold')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Display the number on the graph for each age group
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()



# **ANS**:
# 
# 
# The age group with the highest total number of road fatalities is **25-34 years**, with 436 fatalities.

# In[ ]:





# # 4. Gender Analysis of Car Drivers Involved in Fatal and Injury Collisions

# In[174]:


#Display this Dataframe
driver.head()


# In[175]:


#Displaying unique values for 'Age Groups'
driver['Age Group'].unique()


# In[176]:


#Create a new Dataframe where 'Age Group' == 'All ages'
all_ages_data = driver[driver['Age Group'] == 'All ages']


# In[177]:


#Display this new datafrmae 
all_ages_data


# In[ ]:


# Plotting the barcharts for comparison 


# In[180]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style and font size
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 14})

# Create a color palette
colors = {"Male": "blue", "Female": "pink"}

# Create a new figure with a specified size (width, height)
plt.figure(figsize=(12, 8))

# Create barplot
bplot = sns.barplot(data=all_ages_data, 
                    x='Year', 
                    y='All Drivers of Cars Involved in Fatal and Injury Collisions (Number)', 
                    hue='Gender', 
                    palette=colors, 
                    saturation=0.75)

# Set the plot background color to light grey
plt.gca().set_facecolor('lightgrey')

# Add grid
plt.grid(color='white')

# Set title and labels
plt.title('Gender Analysis of Car Drivers Involved in Fatal and Injury Collisions(2006-2012)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel('Number of Drivers', fontsize=14, fontweight='bold', labelpad=15)

# Add annotations
for p in bplot.patches:
    height = p.get_height()
    bplot.text(p.get_x()+p.get_width()/2.,
            height + 20,
            '{:1.0f}'.format(height),
            ha="center", va='bottom', fontsize=12, color='black')

# Position legend outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1.03, 1), title='Gender', title_fontsize='13')

# Show the plot
plt.show()




# In[181]:


#What is the total number of drivers involved in fatal and injury collisions over these years?
total_drivers = all_ages_data['All Drivers of Cars Involved in Fatal and Injury Collisions (Number)'].sum()
print(f'Total drivers involved in fatal and injury collisions from 2006 to 2012: {total_drivers}')

print('')

#Which year had the highest number of drivers involved in fatal and injury collisions?
max_year = all_ages_data.groupby('Year')['All Drivers of Cars Involved in Fatal and Injury Collisions (Number)'].sum().idxmax()
print(f'The year with the highest number of drivers involved in fatal and injury collisions: {max_year}')

print('')

#How many male and female drivers were involved in fatal and injury collisions each year?
gender_data = all_ages_data.groupby(['Year', 'Gender'])['All Drivers of Cars Involved in Fatal and Injury Collisions (Number)'].sum()
print(gender_data)

print('')


#Which gender had the highest number of drivers involved in fatal and injury collisions over these years?
max_gender = all_ages_data.groupby('Gender')['All Drivers of Cars Involved in Fatal and Injury Collisions (Number)'].sum().idxmax()
print(f'The gender with the highest number of drivers involved in fatal and injury collisions from 2006 to 2012: {max_gender}')

print('')



# ### Q1. What is the year-by-year comparison of male vs. female drivers involved in fatal and injury collisions?
#    - In 2006, there were **3832 accidents involving male drivers** and **2497 accidents involving female drivers**. 
#    - By 2012, these figures were **3768 for male drivers** and **2558 for female drivers**.
# 
# ### Q2. Which gender has seen a more significant increase or decrease in accidents over the years?
#    - **Male drivers saw a decrease of 64 accidents** from 2006 to 2012.
#    - **Female drivers saw an increase of 61 accidents** over the same period.
# 
# ### Q3. What is the average number of accidents for male and female drivers over the years?
# 
# **For male drivers**:
# (3832 + 3580 + 4512 + 4520 + 3789 + 3330 + 3768) / 7 = **~3904.71 accidents per year**
# 
# For **female drivers**:
# (2497 + 2401 + 2963 + 3036 + 2698 + 2427 + 2558) / 7 = **~2654.14 accidents per year**
# 
#    - The average number of accidents involving male drivers from 2006 to 2012 was **3905 accidents per year**.
#    - The average for female drivers was **2654 accidents per year**.
# 
# ### Q4. What is the ratio of male to female drivers involved in fatal and injury collisions each year?
# 
# **2006**: 3832 (male drivers) / 2497 (female drivers) = ~1.53
# 
# **2007**: 3580 / 2401 = ~1.49
# 
# **2008**: 4512 / 2963 = ~1.52 
# 
# **2009**: 4520 / 3036 = ~1.49 
# 
# **2010**: 3789 / 2698 = ~1.40 
# 
# **2011**: 3330 / 2427 = ~1.37
# 
# **2012**: 3768 / 2558 = ~1.47
# 
# 
# 
#    - The ratio of male to female drivers involved in accidents was between **1.37 to 1.53** each year from 2006 to 2012.
#    - This means for every female driver involved in such incidents, there were between 1.37 to 1.53 male drivers involved.

# In[ ]:





# # 5. Monthly Road Fatalities Analysis 

# In[184]:


# Display the dataframe
month.head()


# In[185]:


# Display unique values for 'Month'
month['Month'].unique()


# In[186]:


# Filter out 'All months' and 'Total'
filtered_month_year_data = month[(month['Month'] != 'All months') & (month['Year'] != 'Total')]


# In[187]:


# Display this new dataframe
filtered_month_year_data


# In[ ]:


#Plotting Heatmap


# This heatmap visualizes road fatalities data from the years 2005 to 2012.
# 
# The color of each cell represents the number of road fatalities, with darker shades of red indicating higher numbers.
# 
# 

# In[188]:


# Pivot the data to get a matrix-like DataFrame where each cell represents road fatalities for a given month and year
heatmap_data = filtered_month_year_data.pivot("Month", "Year", "Road Fatalities")

# Sort the months in the correct order
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
heatmap_data = heatmap_data.loc[months_order]

# Create a new figure with a specified size
plt.figure(figsize=(10, 10))

# Use seaborn's heatmap function to plot the data with red colormap
sns.heatmap(heatmap_data, cmap="Reds", annot=True, fmt=".0f", linewidths=.5)

# Add a title
plt.title('Heatmap of Road Fatalities (2005-2012)', fontsize=16, fontweight='bold')

# Show the plot
plt.show()


# In[189]:


# Group data by 'Year' and 'Month' and sum 'Road Fatalities'
grouped_data = filtered_month_year_data.groupby(['Year', 'Month'])['Road Fatalities'].sum().reset_index()

# Sort the data by 'Year' and 'Road Fatalities'
grouped_data_sorted = grouped_data.sort_values(['Year', 'Road Fatalities'], ascending=[True, False])

# Get the month with the maximum fatalities for each year
max_fatalities_each_year = grouped_data_sorted.groupby('Year').first().reset_index()

print(max_fatalities_each_year)


# In[ ]:


#Plotting the barchart for Month with the Highest Fatalities Each Year (2005-2012)


# In[190]:


import matplotlib.pyplot as plt
import seaborn as sns

# Filter out rows with NaN values in the "Road Fatalities" column
filtered_data = max_fatalities_each_year.dropna(subset=["Road Fatalities"])

# Define a color palette for months
month_colors = {
    'January': 'b',
    'February': 'g',
    'March': 'r',
    'April': 'c',
    'May': 'm',
    'June': 'y',
    'July': 'k',
    'August': 'pink',
    'September': 'gray',
    'October': 'purple',
    'November': 'orange',
    'December': 'brown'
}

# Assign the corresponding color for each month in the dataset
filtered_data['color'] = filtered_data['Month'].map(month_colors)

# Set plot style, font size, and figure size
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 14})
plt.figure(figsize=(12, 8))

# Use barplot in seaborn
ax = sns.barplot(
    data=filtered_data,
    x="Year",
    y="Road Fatalities",
    hue="Month",
    palette=month_colors,
    saturation=0.75,
    dodge=False,
)

# Set the plot background color to light grey
plt.gca().set_facecolor('lightgrey')

# Add a white grid
plt.grid(color='white')

# Add axis labels with specified font size, font weight, and label padding
plt.xlabel("Year", fontsize=14, fontweight="bold", labelpad=15)
plt.ylabel("Fatalities", fontsize=14, fontweight="bold", labelpad=15)

# Add a title with specified font size and font weight
plt.title("Month with the Most Road Fatalities (2005-2012)", fontsize=16, fontweight="bold")

# Annotate the non-null values on the chart
for p in ax.patches:
    if not pd.isnull(p.get_height()):
        ax.annotate(
            f"{int(p.get_height())}",  # Format the value as an integer
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
            fontsize=12,
            color='black',
        )

# Position the legend to the right of the chart
plt.legend(
    loc="upper left",
    bbox_to_anchor=(1.03, 1),
    title="Month",
    title_fontsize=12,
)

# Show the plot
plt.show()




# In[191]:


# Group data by 'Year' and 'Month' and sum 'Road Fatalities'
grouped_data = filtered_month_year_data.groupby(['Year', 'Month'])['Road Fatalities'].sum().reset_index()

# Sort the data by 'Year' and 'Road Fatalities'
grouped_data_sorted = grouped_data.sort_values(['Year', 'Road Fatalities'], ascending=[True, True])

# Get the month with the minimum fatalities for each year
min_fatalities_each_year = grouped_data_sorted.groupby('Year').first().reset_index()

print(min_fatalities_each_year)


# In[ ]:


#Plotting the barchart for Month with the lowest Fatalities Each Year (2005-2012)


# In[192]:


import matplotlib.pyplot as plt
import seaborn as sns

# Filter out rows with NaN values in the "Road Fatalities" column
filtered_data = min_fatalities_each_year.dropna(subset=["Road Fatalities"])

# Define a color palette for months
month_colors = {
    'January': 'b',
    'February': 'g',
    'March': 'r',
    'April': 'c',
    'May': 'm',
    'June': 'y',
    'July': 'k',
    'August': 'pink',
    'September': 'gray',
    'October': 'purple',
    'November': 'orange',
    'December': 'brown'
}

# Assign the corresponding color for each month in the dataset
filtered_data['color'] = filtered_data['Month'].map(month_colors)

# Set plot style, font size, and figure size
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 14})
plt.figure(figsize=(12, 8))

# Use barplot in seaborn
ax = sns.barplot(
    data=filtered_data,
    x="Year",
    y="Road Fatalities",
    hue="Month",
    palette=month_colors,
    saturation=0.75,
    dodge=False,
)

# Set the plot background color to light grey
plt.gca().set_facecolor('lightgrey')

# Add a white grid
plt.grid(color='white')

# Add axis labels with specified font size, font weight, and label padding
plt.xlabel("Year", fontsize=14, fontweight="bold", labelpad=15)
plt.ylabel("Fatalities", fontsize=14, fontweight="bold", labelpad=15)

# Add a title with specified font size and font weight
plt.title("Month with the Fewest Road Fatalities (2005-2012)", fontsize=16, fontweight="bold")

# Annotate the non-null values on the chart
for p in ax.patches:
    if not pd.isnull(p.get_height()):
        ax.annotate(
            f"{int(p.get_height())}",  # Format the value as an integer
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
            fontsize=12,
            color='black',
        )

# Position the legend to the right of the chart
plt.legend(
    loc="upper left",
    bbox_to_anchor=(1.03, 1),
    title="Month",
    title_fontsize=12,
)

# Show the plot
plt.show()




# ### Q1. What is the month with the highest number of road fatalities each year?
# 
# 
# **ANS**: The month with the highest number of road fatalities each year:
# 
#    - 2005: **October** with 44 fatalities
#    - 2006: **January** with 40 fatalities
#    - 2007: **December** with 37 fatalities
#    - 2008: **February** with 32 fatalities
#    - 2009: **May** with 28 fatalities
#    - 2010: **October** with 36 fatalities
#    - 2011: **January**  with 21 fatalities
#    - 2012: **June** with 26 fatalities
#    
# ### Q2. What is the month with the lowest number of road fatalities each year?
# 
# 
# **ANS**: The month with the lowest number of road fatalities each year:
# 
#    - 2005: **June** with 22 fatalities
#    - 2006: **August** with 17 fatalities
#    - 2007: **January** with 22 fatalities
#    - 2008: **April** with 19 fatalities
#    - 2009: **February** with 15 fatalities
#    - 2010: **February** with 14 fatalities
#    - 2011: **April**  with 8 fatalities
#    - 2012: **November** with 8 fatalities
#    
#    
# ### Q3. Are there any noticeable trends in road fatalities over the years?
# 
# #### This can provide insights into whether road safety has generally improved or worsened over time
# 
# **ANS:** Generally, there has been a decrease in the number of road fatalities from 2005 to 2012. For instance, the month with the highest number of fatalities in 2005 had 44 deaths, while in 2012 the highest was 26. Also, the month with the lowest number of fatalities in 2005 was 22, and by 2012, it had fallen to 8. 
# 
# Notably, there's no specific pattern concerning which months have the most or least accidents each year. This could suggest that the number of road fatalities is influenced by a variety of factors beyond just the time of year
# 
# 
# 

# ### Q4. Are there seasonal trends in road fatalities?
# 

# In[150]:


#Make a new dataframe 

season = filtered_month_year_data.copy()


# In[151]:


# Define the mapping from months to seasons
seasons_mapping = {
    'January': 'Winter',
    'February': 'Winter',
    'March': 'Spring',
    'April': 'Spring',
    'May': 'Spring',
    'June': 'Summer',
    'July': 'Summer',
    'August': 'Summer',
    'September': 'Fall',
    'October': 'Fall',
    'November': 'Fall',
    'December': 'Winter',
}

# Apply the mapping to the 'Month' column and create a new 'Season' column
season['Season'] = season['Month'].map(seasons_mapping)

print(season)


# In[152]:


seasonal_data = season.groupby('Season')['Road Fatalities'].mean()

print(seasonal_data)


# 
# **ANS:** These average road fatalities suggest that there are slight seasonal variations in road fatalities, with Winter having slightly more fatalities on average compared to other seasons.
# 
# There might be other seasonal factors at play which are not captured in this simple analysis, and the real-life situation can be more complex. 
# 
# For a more thorough analysis, it would be helpful to also consider other factors, such as weather conditions, daylight hours, holiday periods, and traffic volume, among others

# ### Q5. Which months have seen the **most significant increase or decrease in road fatalities over the years**?
# #### This can help identify any months where there has been a **significant change in road safety**.
# 
# **ANS**:
# 
# We will calculate the **change in road fatalities for each month from 2005 to 2012** to identify the months with the most significant increase or decrease. We'll find the change by **subtracting the fatalities in 2005 from the fatalities in 2012**. A positive result will represent an increase in fatalities, while a negative result will represent a decrease. 
# 
# Let's calculate this: 
# 
# - **January**: 10 (2012) - 33 (2005) = -23
# - **February**: 13 (2012) - 37 (2005) = -24
# - **March**: 12 (2012) - 26 (2005) = -14
# - **April**: 16 (2012) - 23 (2005) = -7
# - **May**: 13 (2012) - 41 (2005) = -28
# - **June**: 26 (2012) - 22 (2005) = 4
# - **July**: 15 (2012) - 41 (2005) = -26
# - **August**: 12 (2012) - 24 (2005) = -12
# - **September**: 10 (2012) - 31 (2005) = -21
# - **October**: 15 (2012) - 44 (2005) = -29
# - **November**: 8 (2012) - 34 (2005) = -26
# - **December**: 12 (2012) - 40 (2005) = -28
# 
# From the above calculations, we see that **October has seen the most significant decrease in road fatalities from 2005 to 2012, with a decrease of 29**. Conversely, **June has seen the most significant increase, with an increase of 4**. 
# 
# However, it is important to remember that there can be **various reasons behind these changes**, such as changes in population, changes in the number of vehicles on the road, improvements in vehicle safety, changes in traffic law enforcement, among others. Therefore, **further analysis would be necessary to conclusively determine the reasons behind these changes**.
# 

# ### Q6. Which month has the highest fatalities across all years?

# In[154]:


# On average, has the highest fatalities across all years,
# Group by 'Month' and calculate the mean of 'Road Fatalities'
month_fatalities = filtered_month_year_data.groupby('Month')['Road Fatalities'].mean()

# Get the month with the maximum average number of fatalities
max_month = month_fatalities.idxmax()

# The month with the highest average number of fatalities:
max_month




# **ANS**:  The month with the highest average number of fatalities is **October**

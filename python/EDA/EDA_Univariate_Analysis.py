import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
# path_customer = r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\Data Cleaning\Customer.xlsx"
# Customers_tbl = pd.read_excel(path_customer, sheet_name='Customers')

# # to plot a histogram of age
# age = Customers_tbl['Age']
# plt.hist(age)
# plt.xlabel('Age')
# plt.ylabel('No. of Customers')
# plt.title('Histogram of Age')
# plt.show()

# # # Sample data
# # labels = ['Male', 'Female']
# # sizes = [40, 60]  # Example counts

# # plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# # plt.title('Gender Distribution')
# # plt.show()


# # to plot Gender piechart
# gender_count = Customers_tbl['Gender'].value_counts()
# colors = ["Blue", "Pink", "Yellow"]
# plt.pie(gender_count, labels=gender_count.index,
#         autopct='%1.1f%%', startangle=90, colors=colors)
# plt.title('Gender Distribution Pie chart')
# plt.show()

# # To plot Country bar plot
# country_counts = Customers_tbl['Country'].value_counts(
# ).sort_values(ascending=True)
# plt.barh(country_counts.index, country_counts, color='Green')
# plt.title('Number of customers by country')
# plt.show()

# # To plot City bar plot
# city_counts = Customers_tbl['City'].value_counts(
# ).sort_values(ascending=True)
# plt.barh(city_counts.index, city_counts, color='Green')
# plt.title('Number of customers by City')
# plt.show()

# to plot bar chart of Campaign ID
path_customer = r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\Data Cleaning\Customer.xlsx"
Customers_conversion_tbl = pd.read_excel(
    path_customer, sheet_name="Customer Conversions")

# customer_conversions_counts = Customers_conversion_tbl['Campaign ID'].value_counts(
# ).sort_values(ascending=True)
# print(customer_conversions_counts)
# plt.barh(customer_conversions_counts.index,
#          customer_conversions_counts, color="Gray")
# plt.title('Frequency of each Campaign ID')
# plt.xlabel('Count')
# plt.ylabel('Campaign ID')
# plt.show()

# # to plot Conversions trend over time
# Customers_conversion_tbl['Year'] = Customers_conversion_tbl['Conversion Date'].dt.year
# Customers_conversion_tbl['Month'] = Customers_conversion_tbl['Conversion Date'].dt.month
# Customers_conversion_tbl['Day'] = Customers_conversion_tbl['Conversion Date'].dt.day

# # monthly analysis
# months = Customers_conversion_tbl['Month'].value_counts(
# ).sort_values(ascending=True)
# months.plot(kind='line', marker='o', linestyle='-')
# plt.bar(months.index,
#         months, color="Gray")
# plt.title('Monthly Trends of conversion')
# plt.xlabel('Months')
# plt.ylabel('Number of conversions')
# plt.show()

# # Daily analysis
# days = Customers_conversion_tbl['Day'].value_counts(
# ).sort_values(ascending=True)
# days.plot(kind='line', marker='o', linestyle='-')
# plt.bar(days.index,
#         days, color="Gray")
# plt.title('Daily Trends of conversion')
# plt.xlabel('Days')
# plt.ylabel('Number of conversions')
# plt.show()

# # Yearly analysis
# Years = Customers_conversion_tbl['Year'].value_counts(
# ).sort_values(ascending=True)
# Years.plot(kind='line', marker='o', linestyle='-')
# plt.bar(Years.index,
#         Years, color="Gray")
# plt.title('Yearly Trends of conversion')
# plt.xlabel('Years')
# plt.ylabel('Number of conversions')
# plt.show()

# # to plot revenue Histogram
# revenue = Customers_conversion_tbl['Revenue']
# print(revenue)
# plt.hist(revenue)
# plt.xlabel('Revenue')
# plt.ylabel('No. of Customers')
# plt.title('Histogram of Revenue')
# plt.show()

# Revenue Bivariant analysis - Revenue from each campaign

# Aggregate revenue by campaign ID and ensure it's a Series
revenue_by_campaign1 = Customers_conversion_tbl.groupby('Campaign ID')[
    'Revenue'].sum()

revenue_by_campaign = revenue_by_campaign1.sort_values()
# Print the type to ensure it's a Series
print(type(revenue_by_campaign))

# Create the horizontal bar plot

plt.barh(revenue_by_campaign.index.astype(str),
         revenue_by_campaign.values, color="Black")
plt.xlabel('Revenue')
plt.ylabel('Campaign ID')
plt.title('Revenue from Each Campaign')
plt.show()


# # # to plot pie chart of Channels
# path_campaign = r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\Data Cleaning\Campaigns.xlsx"
# campaign_tbl = pd.read_excel(path_campaign)
# # channel_count = campaign_tbl['Channel'].value_counts()
# # colors = ["red", "gray", "Yellow"]
# # plt.pie(channel_count, labels=channel_count.index,
# #         autopct='%1.1f%%', startangle=90, colors=colors)
# # plt.title('Channel Distribution of Campaigns')
# # plt.show()


# # correlation between clicks and impressions
# path_ImpressionClicks = r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\Data Cleaning\Impressions, Clicks.xlsx"
# ImpressionClicks_tbl = pd.read_excel(path_ImpressionClicks)
# x = ImpressionClicks_tbl['Impressions']
# y = ImpressionClicks_tbl['Clicks']
# plt.scatter(x, y)
# plt.xlabel('Impressions')
# plt.ylabel('Clicks')
# plt.title('Correlation Analysis of Impressions and Clicks')
# plt.show()

path = r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\Data Cleaning\Data For python.xlsx"
df = pd.read_excel(path)


# # scatter plot for budget and impression.
# x = df['Impressions']
# y = df['Budget']
# plt.scatter(x, y)
# plt.xlabel('Impressions')
# plt.ylabel('Budget')
# plt.title('Correlation Analysis of Impressions and Budget')
# plt.show()

# # scatter plot for budget and revenue.
# x = df['Revenue']
# y = df['Budget']
# plt.scatter(x, y)
# plt.xlabel('Revenue')
# plt.ylabel('Budget')
# plt.title('Correlation Analysis of Impressions and Budget')
# plt.show()

# for correlation coefficient matrixx
output_path = r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\EDA\Description_statistics.xlsx"
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    # Select only numeric columns
    df_numeric = df.select_dtypes(include=['number'])

    # Calculate the Pearson correlation matrix
    correlation_matrix = df_numeric.corr()

    # Write the numeric DataFrame to the first sheet
    df_numeric.to_excel(writer, sheet_name='Numeric Data', index=False)

    # Write the correlation matrix to the second sheet
    correlation_matrix.to_excel(writer, sheet_name='Correlation Matrix')

# Print the correlation matrix to confirm it is calculated correctly
print(correlation_matrix)

sns.heatmap(correlation_matrix.round(2), annot=True)
plt.title('Correlation Matrix Heatmap')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()


impbars = df. groupby('Campaign ID')['Impressions'].sum().sort_values()

# Create the horizontal bar plot

plt.barh(impbars.index.astype(str),
         impbars, color="blue")
plt.xlabel('Impression')
plt.ylabel('Campaign ID')
plt.title('Impression from Each Campaign')
plt.show()

Clibars = df. groupby('Campaign ID')['Clicks'].sum().sort_values()

# Create the horizontal bar plot

plt.barh(Clibars.index.astype(str),
         Clibars, color="Yellow")
plt.xlabel('Click')
plt.ylabel('Campaign ID')
plt.title('Clicks from Each Campaign')
plt.show()

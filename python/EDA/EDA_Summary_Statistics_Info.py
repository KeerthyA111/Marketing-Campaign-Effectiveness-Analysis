import pandas as pd
import seaborn as sns


# Display all columns
pd.set_option('display.max_columns', None)
print(2*"\n")

path_customer = r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\Data Cleaning\Customer.xlsx"
Customers_tbl = pd.read_excel(path_customer, sheet_name='Customers')

print('Description Statistics of Customers')
print(Customers_tbl.shape)
print(Customers_tbl.describe(include='all'))
print(2*"\n")

Customers_conversion_tbl = pd.read_excel(
    path_customer, sheet_name="Customer Conversions")
print('Description Statistics Customer Convertions')
print(Customers_tbl.shape)
print(Customers_tbl.describe(include='all'))
print(2*"\n")

Campaign_tbl = pd.read_excel(
    r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\Data Cleaning\Campaigns.xlsx")
print("Description Statictics of Campaign")
print(Campaign_tbl.shape)
print(Campaign_tbl.describe(include='all'))
print(2*"\n")


ImpressionsClick_tbl = pd.read_excel(
    r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\Data Cleaning\Impressions, Clicks.xlsx")

print('Description statistics of Impressions and Clicks')
print(ImpressionsClick_tbl.shape)
print(ImpressionsClick_tbl.describe(include='all'))


# Export descriptive statistics to a new Excel file
Output_path = r"C:\Users\Keerthy Anish\Desktop\Keerthy_Work\Capstone Project\Copy - CDAP Capstone Project Data - Marketing Campaign Effectiveness\EDA\Description_statistics.xlsx"
with pd.ExcelWriter(Output_path, engine='xlsxwriter') as writer:
    Customers_tbl.describe(include='all').to_excel(
        writer, sheet_name='Customers_Desc')
    Customers_conversion_tbl.describe(
        include='all').to_excel(writer, sheet_name='Customer_Conversions_Desc')
    Campaign_tbl.describe(include='all').to_excel(
        writer, sheet_name='Campaigns_Desc')
    ImpressionsClick_tbl.describe(include='all').to_excel(
        writer, sheet_name='Impressions_Clicks_Desc')


# Export info to a new Excel file
# The info() method in pandas doesn't return a DataFrame; it prints directly to the console.
# Therefore, you cannot directly call to_excel on the result of info().
# Instead, you need to capture the output of info() and write it manually to the Excel file.

print('Customers info')
print(Customers_tbl.info())

print(2*'\n')
print('Customer_Conversions info')
print(Customers_conversion_tbl .info())

print(2*'\n')
print('Campaign info')
print(Campaign_tbl.info())

print(2*'\n')
print('Impressions_Click info')
print(ImpressionsClick_tbl.info())

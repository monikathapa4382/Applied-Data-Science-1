# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 23:24:20 2023

@author: Monika
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV 
df = pd.read_csv('C:\\Users\\Monika\\Downloads\\20230816Rolling12MonthsofCashReceiptsBrokenDownbyMonth1.csv')

if 'InvoiceMonth' in df.columns:
    df['InvoiceMonth'] = pd.to_datetime(df['InvoiceMonth'])

# Convert  columns into numeric and remove commas
df['MeatIndustryCash'] = df['MeatIndustryCash'].str.replace(',', '').fillna(0).astype(float)
df['MiscAndMilkIndustryCash'] = df['MiscAndMilkIndustryCash'].str.replace(',', '').fillna(0).astype(float)
df['RadiologicalCash'] = df['RadiologicalCash'].str.replace(',', '').fillna(0).astype(float)
df['GovernmentCash'] = df['GovernmentCash'].str.replace(',', '').fillna(0).astype(float)

# Line Plot

if 'InvoiceMonth' in df.columns:
    df.set_index('InvoiceMonth', inplace=True)

# Create the line plot if there is data to plot

    plt.figure(figsize=(12, 8))
 
    df.plot(kind='line', style='-', figsize=(12, 8))

    # Customize the plot
    plt.xlabel('Invoice Month')
    plt.ylabel('Cash Receipts (USD)')
    plt.title('Line Plot of Cash Receipts by Industry')
  
    plt.legend(title='Industries', loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Bar Plot
    colors = ['red', 'brown', 'yellow', 'blue']
    axis = df.plot(kind='bar', stacked=True, figsize=(12, 8), color=colors)

    # Customthe plot
    axis.set_xlabel('InvoiceMonths')
    axis.set_ylabel('Values')
    axis.set_title('Bar Plot of Cash Receipts Broken')
    plt.grid(True)
    axis.legend(title='Columns', loc='upper left')

    x_labels = df.index.strftime('%Y-%m')
    axis.set_xticklabels(x_labels)

    plt.show()

# Read the data from the CSV 
file_path = 'C:\\Users\\Monika\\Downloads\\monika_dataset.csv'
data = pd.read_csv(file_path)

# Filter the data for specific countries and series
countries = ['India', 'Maldives', 'Sri Lanka']
series = 'EG.ELC.ACCS.UR.ZS'
years = ['2003 [YR2003]', '2004 [YR2004]', '2005 [YR2005]', '2006 [YR2006]', '2007 [YR2007]', '2008 [YR2008]']

filtered_data = data[data['Country Name'].isin(countries) & (data['Series Code'] == series)]
filtered_data = filtered_data.set_index('Country Name')

# Transpose the data for plotting
filtered_data = filtered_data[years].transpose()


# Create a scatter plot
plt.figure(figsize=(10, 6))
for country in countries:
    plt.scatter(filtered_data.index, filtered_data[country], label=country)

plt.xlabel('Years')
plt.ylabel('Consumption of Electricity (%)')
plt.title('World Developement Indicators')
plt.grid(True)
plt.legend()
plt.show()
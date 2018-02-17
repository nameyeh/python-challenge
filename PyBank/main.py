#Instructions 
#------------
#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
#You will be given two sets of revenue data (budget_data_1.csv and  budget_data_2.csv). 
#Each dataset is composed of two columns: Date and Revenue. (Thankfully, your company has rather lax standards 
#for accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:
    ##The total number of months included in the dataset
    ##The total amount of revenue gained over the entire period
    #The average change in revenue between months over the entire period
    #The greatest increase in revenue (date and amount) over the entire period
    #The greatest decrease in revenue (date and amount) over the entire period
#As an example, your analysis should look similar to the one below:
#Financial Analysis
#----------------------------
#Total Months: 25
#Total Revenue: $1241412
#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)
#Your final script should both print the analysis to the terminal 
#and export a text file with the results.
#-----------------------------------------------------------------------------
import numpy as np
import pandas as pd 
#import os
#import csv

file = "C:/Users/nab226/Desktop/NUCHI201801DATA4-Class-Repository-DATA/MWS/Homework/03-Python/Instructions/PyBank/raw_data/budget_data_1.csv"
df = pd.read_csv(file)
#df.head()

#The total number of months included in the dataset
n_months = df.Date.count()
#n_months
print("Financial Analysis - Dataset #1")
print("----------------------------")
print("Total Months: "+str(n_months)) 

#The total amount of revenue gained over the entire period
total_rev = df["Revenue"].sum()
#total_rev
print("Total Revenue: $"+str(total_rev))

#The average change in revenue between months over the entire period
rev = np.array(df["Revenue"])
#rev
n_rev = rev.size
#n_rev

delta_rev = np.diff(rev)
#delta_rev

n_delta_rev = delta_rev.size
#n_delta_rev

avg_delta_rev = (delta_rev.sum())/(n_delta_rev)
avg_delta_rev = np.round(avg_delta_rev,2)
print("Average Revenue Change: $"+str(avg_delta_rev))

#The greatest increase in revenue (date and amount) over the entire period
max_rev = df["Revenue"].max()
#max_rev

min_rev = df["Revenue"].min()
#min_rev

dict_df = pd.Series(df.Revenue.values,index=df.Date).to_dict()
#dict_df

for Date, Revenue in dict_df.items():    
    if Revenue == max_rev:
        print("Greatest Increase in Revenue: "+str(Date)+" ($"+str(Revenue)+")")

for Date, Revenue in dict_df.items():    
    if Revenue == min_rev:
        print("Greatest Decrease in Revenue: "+str(Date)+" ($"+str(Revenue)+")")
print("                                     ")

with open("pybank_output1.txt", "w") as text_file:
   print("Financial Analysis - Dataset #1", file=text_file)
   print("----------------------------", file=text_file)
   print("Total Months: "+str(n_months), file=text_file) 
   print("Total Revenue: $"+str(total_rev), file=text_file)
   print("Average Revenue Change: $"+str(avg_delta_rev), file=text_file)
   for Date, Revenue in dict_df.items():   
       if Revenue == max_rev:
           print("Greatest Increase in Revenue: "+str(Date)+" ($"+str(Revenue)+")", file=text_file)
   for Date, Revenue in dict_df.items():    
       if Revenue == min_rev:
           print("Greatest Decrease in Revenue: "+str(Date)+" ($"+str(Revenue)+")", file=text_file)
 #end of script for dataset #1

#re-run script for dataset #2
#-----------------------------------------------------------------------------
import numpy as np
import pandas as pd 
#import os
#import csv

file = "C:/Users/nab226/Desktop/NUCHI201801DATA4-Class-Repository-DATA/MWS/Homework/03-Python/Instructions/PyBank/raw_data/budget_data_2.csv"
df = pd.read_csv(file)
#df.head()

#The total number of months included in the dataset
n_months = df.Date.count()
#n_months
print("Financial Analysis - Dataset #2")
print("----------------------------")
print("Total Months: "+str(n_months)) 

#The total amount of revenue gained over the entire period
total_rev = df["Revenue"].sum()
#total_rev
print("Total Revenue: $"+str(total_rev))

#The average change in revenue between months over the entire period
rev = np.array(df["Revenue"])
#rev
n_rev = rev.size
#n_rev

delta_rev = np.diff(rev)
#delta_rev

n_delta_rev = delta_rev.size
#n_delta_rev

avg_delta_rev = (delta_rev.sum())/(n_delta_rev)
avg_delta_rev = np.round(avg_delta_rev,2)
print("Average Revenue Change: $"+str(avg_delta_rev))

#The greatest increase in revenue (date and amount) over the entire period
max_rev = df["Revenue"].max()
#max_rev

min_rev = df["Revenue"].min()
#min_rev

dict_df = pd.Series(df.Revenue.values,index=df.Date).to_dict()
#dict_df

for Date, Revenue in dict_df.items():    
    if Revenue == max_rev:
        print("Greatest Increase in Revenue: "+str(Date)+" ($"+str(Revenue)+")")

for Date, Revenue in dict_df.items():    
    if Revenue == min_rev:
        print("Greatest Decrease in Revenue: "+str(Date)+" ($"+str(Revenue)+")")

with open("pybank_output2.txt", "w") as text_file:
   print("Financial Analysis - Dataset #2", file=text_file)
   print("----------------------------", file=text_file)
   print("Total Months: "+str(n_months), file=text_file) 
   print("Total Revenue: $"+str(total_rev), file=text_file)
   print("Average Revenue Change: $"+str(avg_delta_rev), file=text_file)
   for Date, Revenue in dict_df.items():   
       if Revenue == max_rev:
           print("Greatest Increase in Revenue: "+str(Date)+" ($"+str(Revenue)+")", file=text_file)
   for Date, Revenue in dict_df.items():    
       if Revenue == min_rev:
           print("Greatest Decrease in Revenue: "+str(Date)+" ($"+str(Revenue)+")", file=text_file)
 #end of script
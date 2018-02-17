#Instructions 
#In this challenge, you are tasked with helping a small, 
#rural town modernize its vote-counting process.
#You will be given two sets of poll data (election_data_1.csv and 
#election_data_2.csv). Each dataset is composed of three columns: 
#Voter ID, County, and Candidate. Your task is to create a Python 
#script that analyzes the votes and calculates each of the following:

    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:
#Election Results
#-------------------------
#Total Votes: 620100
#-------------------------
#Rogers: 36.0% (223236)
#Gomez: 54.0% (334854)
#Brentwood: 4.0% (24804)
#Higgins: 6.0% (37206)
#-------------------------
#Winner: Gomez
#-------------------------
#Your final script should both print the analysis to the terminal 
#and export a text file with the results.
#-----------------------------------------------------------------------------
import numpy as np
import pandas as pd 
import os
import csv

file = "C:/Users/nab226/Desktop/NUCHI201801DATA4-Class-Repository-DATA/MWS/Homework/03-Python/Instructions/PyPoll/raw_data/election_data_1.csv"
df = pd.read_csv(file)
#df.head()

#The total number of votes cast
n_votes = df["Voter ID"].count()
n_votes

print("#Election Results - Dataset #1")
print("------------------------------------")
print("Total Votes: "+str(n_votes)) 
print("------------------------------------")

cand = df.Candidate.unique()
cand1 = df.loc[(df["Candidate"]== str(cand[0]))]
cand2 = df.loc[(df["Candidate"]== str(cand[1]))]
cand3 = df.loc[(df["Candidate"]== str(cand[2]))]
cand4 = df.loc[(df["Candidate"]== str(cand[3]))]

nm_cand1 = str(cand1.Candidate.values[0])
nm_cand2 = str(cand2.Candidate.values[0])
nm_cand3 = str(cand3.Candidate.values[0])
nm_cand4 = str(cand4.Candidate.values[0])

nm = [nm_cand1,nm_cand2,nm_cand3,nm_cand4]

n_cand1 = np.array(cand1["Voter ID"])
n_cand1 = n_cand1.size

n_cand2 = np.array(cand2["Voter ID"])
n_cand2 = n_cand2.size

n_cand3 = np.array(cand3["Voter ID"])
n_cand3 = n_cand3.size

n_cand4 = np.array(cand4["Voter ID"])
n_cand4 = n_cand4.size

n = [n_cand1, n_cand2, n_cand3, n_cand4] 

cand1_pct = np.round((n_cand1/n_votes)*100,2) 
cand1_pct 

cand2_pct = np.round((n_cand2/n_votes)*100,2) 
cand2_pct 

cand3_pct = np.round((n_cand3/n_votes)*100,2) 
cand3_pct 

cand4_pct = np.round((n_cand4/n_votes)*100,2) 
cand4_pct

pct = [cand1_pct, cand2_pct, cand3_pct, cand4_pct] 

dict_df = dict(zip(nm, zip(pct, n)))

print("Name"+"   "+"(  %"+" , "+"# Votes)")
for i in dict_df:
    print(i, dict_df[i])
print("------------------------------------")
    
max_votes = max(dict_df, key=dict_df.get)
winner = print("Winner: "+str(max_votes))

with open("pypoll_output1.txt", "w") as text_file:  
    print("#Election Results - Dataset #1", file=text_file)
    print("------------------------------------", file=text_file)
    print("Total Votes: "+str(n_votes), file=text_file) 
    print("------------------------------------", file=text_file) 
    print("Name"+"   "+"(  %"+" , "+"# Votes)", file=text_file)
    for i in dict_df:
        print(i, dict_df[i], file=text_file)
    print("------------------------------------", file=text_file)
    print("Winner: "+str(max_votes), file=text_file)
    print("                                    ")
    print("                                    ")
 #end of script for dataset #1

#re-run script for dataset #2
#-----------------------------------------------------------------------------
file = "C:/Users/nab226/Desktop/NUCHI201801DATA4-Class-Repository-DATA/MWS/Homework/03-Python/Instructions/PyPoll/raw_data/election_data_2.csv"
df = pd.read_csv(file)
#df.head()

#The total number of votes cast
n_votes = df["Voter ID"].count()
n_votes

print("#Election Results - Dataset #2")
print("------------------------------------")
print("Total Votes: "+str(n_votes)) 
print("------------------------------------")

cand = df.Candidate.unique()
cand1 = df.loc[(df["Candidate"]== str(cand[0]))]
cand2 = df.loc[(df["Candidate"]== str(cand[1]))]
cand3 = df.loc[(df["Candidate"]== str(cand[2]))]
cand4 = df.loc[(df["Candidate"]== str(cand[3]))]

nm_cand1 = str(cand1.Candidate.values[0])
nm_cand2 = str(cand2.Candidate.values[0])
nm_cand3 = str(cand3.Candidate.values[0])
nm_cand4 = str(cand4.Candidate.values[0])

nm = [nm_cand1,nm_cand2,nm_cand3,nm_cand4]

n_cand1 = np.array(cand1["Voter ID"])
n_cand1 = n_cand1.size

n_cand2 = np.array(cand2["Voter ID"])
n_cand2 = n_cand2.size

n_cand3 = np.array(cand3["Voter ID"])
n_cand3 = n_cand3.size

n_cand4 = np.array(cand4["Voter ID"])
n_cand4 = n_cand4.size

n = [n_cand1, n_cand2, n_cand3, n_cand4] 

cand1_pct = np.round((n_cand1/n_votes)*100,2) 
cand1_pct 

cand2_pct = np.round((n_cand2/n_votes)*100,2) 
cand2_pct 

cand3_pct = np.round((n_cand3/n_votes)*100,2) 
cand3_pct 

cand4_pct = np.round((n_cand4/n_votes)*100,2) 
cand4_pct

pct = [cand1_pct, cand2_pct, cand3_pct, cand4_pct] 

dict_df = dict(zip(nm, zip(pct, n)))

print("Name"+"  "+"( %"+", "+"# Votes)")
for i in dict_df:
    print(i, dict_df[i])
print("------------------------------------")
    
max_votes = max(dict_df, key=dict_df.get)
winner = print("Winner: "+str(max_votes))

with open("pypoll_output2.txt", "w") as text_file:  
    print("#Election Results - Dataset #2", file=text_file)
    print("------------------------------------", file=text_file)
    print("Total Votes: "+str(n_votes), file=text_file) 
    print("------------------------------------", file=text_file) 
    print("Name"+"  "+"( %"+", "+"# Votes)", file=text_file)
    for i in dict_df:
        print(i, dict_df[i], file=text_file)
    print("------------------------------------", file=text_file)
    print("Winner: "+str(max_votes), file=text_file)
    
 #end of script for dataset #2
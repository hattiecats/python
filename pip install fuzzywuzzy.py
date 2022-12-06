# Import packages
import os
import pandas as pd
from fuzzywuzzy import fuzz

# Change directory
os.chdir(r"C:/Users/modul/Documents/Birkbeck Applied Data Science/Python External Projects")
# Import the customers data
filename = "companyL1L2.csv"
customers = pd.read_csv(filename)

# Clean customers lists
a_cleaned = [customer for customer in customers["list_a"] if not(pd.isnull(customer))]
b_cleaned = [customer for customer in customers["list_b"].unique()if not(pd.isnull(customer))]

# Perform fuzzy string matching
tuples_list = [max([(fuzz.token_set_ratio(i,j),j) for j in b_cleaned]) for i in a_cleaned]

# Unpack list of tuples into two lists
similarity_score, fuzzy_match = map(list,zip(*tuples_list))

# Create pandas DataFrame
df = pd.DataFrame({"list_a":a_cleaned, "fuzzy match": fuzzy_match, "similarity score":similarity_score})

# Export to Excel
df.to_csv("C:/Users/modul/Documents/Birkbeck Applied Data Science/Python External Projects/Fuzzy String Matching.csv", header=False, index=False)

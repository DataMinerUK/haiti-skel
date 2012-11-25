from pandas import DataFrame
import pandas as pd
import numpy as np
import os
import sys

def to_cat_list(catstr):
	stripped = (x.strip() for x in catstr.split(","))
	return [x for x in stripped if x]
	
def get_all_categories(cat_series):
	cat_sets = (set(to_cat_list(x)) for x in cat_series)
	return sorted(set.union(*cat_sets))
	
def get_english(cat):
	code, names = cat.split(".")
	if "|" in names:
		names = names.split(" | ")[1]
	return code, names.strip()
	
def get_code(seq):
	return [x.split(".")[0] for x in seq if x]

# Read data from standard input on the command line
sys.stdin = os.fdopen( sys.stdin.fileno(), "rU" )
data = pd.read_csv(sys.stdin)

# Restrict to data in Haiti with categories
data = data[(data.LATITUDE > 18) & (data.LATITUDE < 20) &
	(data.LONGITUDE > -75) & (data.LONGITUDE < -70) &
	data.CATEGORY.notnull()]

# Extract categorizations
all_cats = get_all_categories(data.CATEGORY)

# Add indicator columns for categories
all_codes = get_code(all_cats)
code_index = pd.Index(np.unique(all_codes))
dummy_frame = DataFrame(np.zeros((len(data), len(code_index))), index = data.index, columns = code_index)

for row, cat in zip(data.index, data.CATEGORY):
	codes = get_code(to_cat_list(cat))
	dummy_frame.ix[row, codes] = 1
	
data = data.join(dummy_frame.add_prefix("category_"))

# Write data to standard output
data.to_csv(sys.stdout)

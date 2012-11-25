from pandas import DataFrame
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
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
	
def basic_haiti_map(ax = None, lllat = 17.25, urlat = 20.25, lllon = -75, urlon = -71):
	# Create polar stereographic Basemap instance
	m = Basemap(ax=ax, projection="stere", lon_0=(urlon + lllon)/2, lat_0=(urlat + lllat)/2, 
		llcrnrlat=lllat, urcrnrlat=urlat, llcrnrlon=lllon, urcrnrlon=urlon, 
		resolution="f")
	# Draw coastlines, state and country boundaries, edge of map
	m.drawcoastlines()
	m.drawstates()
	m.drawcountries()
	return m

# Read data from standard input on the command line
sys.stdin = os.fdopen( sys.stdin.fileno(), "rU" )
data = pd.read_csv(sys.stdin)

# Extract categorizations
all_cats = get_all_categories(data.CATEGORY)
english_mapping = dict(get_english(x) for x in all_cats)

# Plot Categorizations
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,10))
fig.subplots_adjust(hspace=0.05, wspace=0.05)

to_plot = ["2a", "1", "3c", "7a"]

lllat=17.25
urlat=20.25
lllon=-75
urlon=-71

for code, ax in zip(to_plot, axes.flat):
	m = basic_haiti_map(ax, lllat=lllat, urlat=urlat, lllon=lllon, urlon=urlon)
	cat_data = data[data["category_%s" % code] == 1]
	
	# Compute map proj coordinates
	x, y = m(cat_data.LONGITUDE, cat_data.LATITUDE)
	
	m.plot(x, y, "k.", alpha=0.5)
	ax.set_title("%s: %s" % (code, english_mapping[code]))

plt.savefig("out/Haiti.pdf")

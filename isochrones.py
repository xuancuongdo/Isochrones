import matplotlib
import matplotlib.pyplot as pyplot

import geopandas

import pandas
import copy


#read file to variable
pop = geopandas.read_file('data/wgtn-2013-pop.geojson')
rds = geopandas.read_file('data/wgtn-roads.shp')
crashes = geopandas.read_file('data/crashes-2017.geojson')

# Make the figure
fig = pyplot.figure(figsize=(10,10))
ax = fig.add_subplot(111)
# Set background colour to grey
ax.set_facecolor('lightgrey')
ax.set_title("General map of assignment materials")

# Plot meshblock populations
pop.plot(ax=ax, column='pop2013', cmap='Blues', alpha=0.8, legend=True)
# Add the roads
rds.plot(ax=ax, linewidth=0.35, color='r')


# Add the crashes
crashes.plot(ax=ax, color='k', markersize=1)

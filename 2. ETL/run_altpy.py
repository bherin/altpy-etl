#!/usr/bin/python

import altpy as ap
import pandas as pd
import numpy as np

#############
# Load data #
#############

#data_inflation = ap.inputdata('csv','../1. Data/inflation.csv',',')
data_inflation = ap.inputdata('xlsx','../1. Data/inflation.xlsx','Sheet2')
#data_immo = ap.inputdata('xlsx','../1. Data/immo_data_light.xlsx','immo_light')
data_immo = ap.inputdata('xlsx','../1. Data/immo_data.xlsx','immo_by_municipality_2010-2019')


################
# Display data #
################

#ap.browse(data_inflation,'2')
#ap.browse(data_immo,'5')

###############
# Select data #
###############

# Inflation data #
##################

# TEST #
#ap.select(data_inflation,'display','n/a','n/a')
#data_inflation2 = ap.select(data_inflation,'rename','Year - 2011','2011')
#ap.select(data_inflation2,'display','n/a','n/a')
#data_inflation2 = ap.select(data_inflation2,'retype','Year - 2012','text')
#ap.select(data_inflation2,'display','n/a','n/a')
#data_inflation2 = ap.select(data_inflation2,'retype','Year - 2012','number')
#ap.select(data_inflation2,'display','n/a','n/a')
#data_inflation2 = ap.select(data_inflation2,'retype','Year - 2012','text')
#data_inflation2 = ap.select(data_inflation2,'keep',['Country','2011','Year - 2012'],'n/a')
#ap.select(data_inflation2,'display','n/a','n/a')
#ap.select(data_inflation,'display','n/a','n/a')

# rename #
data_inflation2 = ap.select(data_inflation, 'rename','Year - 2011','2011')
data_inflation2 = ap.select(data_inflation2,'rename','Year - 2012','2012')
data_inflation2 = ap.select(data_inflation2,'rename','Year - 2013','2013')
data_inflation2 = ap.select(data_inflation2,'rename','Year - 2014','2014')
data_inflation2 = ap.select(data_inflation2,'rename','Year - 2015','2015')
data_inflation2 = ap.select(data_inflation2,'rename','Year - 2016','2016')
data_inflation2 = ap.select(data_inflation2,'rename','Year - 2017','2017')
data_inflation2 = ap.select(data_inflation2,'rename','Year - 2018','2018')
ap.select(data_inflation2,'display','n/a','n/a')
#ap.outputdata(data_inflation2,'csv','../3. Output/inflation2.csv','|')

# transpose #
data_inflation3 = ap.transpose(data_inflation2,['Country'],['2011','2012','2013','2014','2015','2016','2017','2018'])
data_inflation4 = ap.select(data_inflation3,'rename','Name','Year')
data_inflation4 = ap.select(data_inflation4,'rename','Value','Inflation')
ap.browse(data_inflation4,'all')
data_inflation4 = ap.select(data_inflation4,'retype','Year','text')
ap.select(data_inflation4,'display','n/a','n/a')
ap.browse(data_inflation4,'all')

## crosstab #
#data_inflation5 = ap.crosstab(data_inflation4,['Country'],['Year'],['Inflation'],np.mean)
#ap.browse(data_inflation5,'all')
#ap.select(data_inflation5,'display','n/a','n/a')
##ap.outputdata(data_inflation5,'csv','../3. Output/inflation5.csv','|')


# Immo data #
#############

# format #
#ap.select(data_immo,'display','n/a','n/a')
data_immo2 = ap.select(data_immo,'retype','CD_YEAR','text')
data_immo2 = ap.select(data_immo2,'retype','CD_REFNIS','text')
ap.select(data_immo2,'display','n/a','n/a')
data_immo2 = ap.select(data_immo2,'keep',['CD_COUNTRY','CD_YEAR','CD_TYPE_FR','MS_MEAN_PRICE','MS_TOTAL_PRICE','MS_TOTAL_SURFACE'],'n/a')
ap.select(data_immo2,'display','n/a','n/a')
ap.browse(data_immo2,'all')

# join #
data_merge = ap.join(data_immo2,data_inflation4,['CD_COUNTRY','CD_YEAR'],['Country','Year'],'left')
ap.select(data_merge,'display','n/a','n/a')
ap.browse(data_merge,'all')
data_merge = ap.select(data_merge,'keep',['CD_COUNTRY','CD_YEAR','CD_TYPE_FR','MS_MEAN_PRICE','MS_TOTAL_PRICE','MS_TOTAL_SURFACE','Inflation'],'n/a')
ap.select(data_merge,'display','n/a','n/a')

## union #
#dataframe_1 = data_merge
#dataframe_2 = ap.select(data_merge,'keep',['CD_COUNTRY','CD_YEAR'],'n/a')
#dataframe_2['new column'] = dataframe_2['CD_COUNTRY']
#dataframe_3 = ap.union(dataframe_1,dataframe_2)
#ap.select(dataframe_1,'display','n/a','n/a')
#ap.select(dataframe_2,'display','n/a','n/a')
#ap.select(dataframe_3,'display','n/a','n/a')
#ap.browse(dataframe_3,'all')

# sort #
ap.browse(data_immo2,'all')
data_sort = ap.sort(data_immo2,['CD_COUNTRY','CD_YEAR','MS_MEAN_PRICE'],['desc','desc','asc'])
ap.browse(data_sort,'all')

# filter #
data_filter = ap.filter(data_sort,"[CD_COUNTRY] == 'Belgium' and [CD_YEAR] != '2014' and [MS_MEAN_PRICE] > (2 * 125000)",'true')
ap.browse(data_filter,'all')

# formula #
data_calc = ap.formula(data_filter,"[MS_TOTAL_PRICE]/[MS_TOTAL_SURFACE]",'MS_PRICE_PER_SURFACE')
ap.browse(data_calc,'all')
ap.select(data_calc,'display','n/a','n/a')

# comment #
ap.comment('we will now summarize the data')

# summarize #
data_summarize = ap.summarize(data_sort,['CD_COUNTRY','CD_YEAR'],['MS_MEAN_PRICE','MS_TOTAL_PRICE'],['average','sum'])
ap.browse(data_summarize,'all')
ap.select(data_summarize,'display','n/a','n/a')

# drop (select) #
data_drop = ap.select(data_summarize,'drop',['MS_MEAN_PRICE','MS_TOTAL_PRICE'],'n/a')
ap.browse(data_drop,'all')
ap.select(data_drop,'display','n/a','n/a')

#############
# Save data #
#############

#ap.outputdata(data_inflation,'xlsx','../3. Output/inflation.xlsx','Sheet1')
#ap.outputdata(data_inflation,'csv','../3. Output/inflation.csv','|')
#ap.outputdata(data_inflation,'csv','../3. Output/immo_data.csv','|')

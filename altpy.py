#!/usr/bin/python

import pandas as pd
import numpy as np
#import prettypandas
#import datetime

#https://jakevdp.github.io/PythonDataScienceHandbook/03.12-performance-eval-and-query.html

pd.options.mode.chained_assignment = None

#######################
# Library description #
#######################
# This library is a layer above the pandas Library,
# whose purpose is to save data analyst's/scientist's
# time by abstracting further the typical steps
# required in Extract-Transform-Load (ETL) processes.
# It should also help people with less expertise in
# Python implement those ETL processes in an easy
# and intuitive way.


#############
# Functions #
#############

#############
# inputdata #
#############
# Description: load data
# Inputs:
# [string] filetype: either 'xlsx' or 'csv'
# [string] path: file to load link, either absolute or relative
# [string] sheet_or_separator: if xlsx, sheet name to load, if csv separator type (',','|',...)
# Output:
# [dataframe] df_xlsx: returns the xlsx loaded file in a dataframe format
# [dataframe] df_csv: returns the csv loaded file in a dataframe format
# Documentation:

def inputdata(filetype,path,sheet_or_separator):
    print '\n','Input data','\n','----------'

    if filetype == 'xlsx':
        print 'loading file: file type =',filetype,'|path=',path,'|sheet=',sheet_or_separator
        xlsx_file = pd.ExcelFile(path)
        df_xlsx = xlsx_file.parse(sheet_or_separator)
        return df_xlsx

    elif filetype == 'csv':
        print 'loading file: file type =',filetype,'|path=',path,'|separator=',sheet_or_separator
        csv_file = pd.read_csv(path,sep=sheet_or_separator)
        df_csv = csv_file
        return df_csv

    else:
        print('this file format is not available for loading for the moment')


##############
# outputdata #
##############
# Description: save data in new file
# Inputs:
# [dataframe] dataframe: data to save in new file
# [string] filetype: either 'xlsx' or 'csv'
# [string] path: file to save link, either absolute or relative
# [string] sheet_or_separator: if xlsx, sheet name to load, if csv separator type (',','|',...)
# Output:
# [file] saved in specified path, with given name and format
# [print] success/failure message
# Documentation:

def outputdata(dataframe,filetype,path,sheet_or_separator):
    print '\n','Output data','\n','-----------'

    if filetype == 'xlsx':
        print 'save data module, saving file: file type =',filetype,'|path=',path,'|sheet=',sheet_or_separator
        xlsx_writer = pd.ExcelWriter(path,engine='xlsxwriter')
        dataframe.to_excel(xlsx_writer, sheet_name=sheet_or_separator)
        xlsx_writer.save()

    elif filetype == 'csv':
        print 'save data module, saving file: file type =',filetype,'|path=',path,'|separator=',sheet_or_separator
        dataframe.to_csv(path,sep=sheet_or_separator, header=True, index=False, encoding='utf-8')

    else:
        print('this file format is not available for saving for the moment')


##########
# browse #
##########
# Description: display data for review purpose
# Inputs:
# [dataframe] dataframe: dataframe created by other modules and whose data
#                        need to be reviewed
# [string] depth: level of visualization, either a number of rows ('') or 'all'
# Output:
# [print] prints the data from the plugged dataframe
# Documentation:

def browse(dataframe,depth):
    print '\n','Browse','\n','------'

    if depth.isdigit() and int(depth) <= dataframe.shape[0]:
        print 'top',depth,'rows of the dataset'
        print(dataframe.head(n=int(depth)))

    elif depth.isdigit() and int(depth) > dataframe.shape[0]:
        print('the dataset is smaller than number of rows requested')

    elif depth == 'all':
        print(dataframe)
        print 'the dataset has',dataframe.shape[0],'rows'

    else:
        print('this Browse functionality is not available for display for the moment')


##########
# select #
##########
# Description: selects columns for informationaly display, rename, or type change
# Input:
# [dataframe] dataframe: dataframe created by other modules and whose columns
#                        need to be reviewed
# [string] category: 'display' to visualize column's names and types, 'rename'
#                    to rename a column, 'retype' to change a column's data type
#                    'keep' to keep only a subset of columns, 'drop' to drop a
#                    subset of columns
# [string/list] column: the column's name(s) that needs to be renamed (string)
#                       - kept(list) - retyped(string) - dropped(list), 'n/a'
#                       for 'display'
# [string] value: the new allocation, a name for 'rename', a type for 'retype',
#                 'n/a' for 'display', 'n/a' for 'keep', 'n/a' for drop
# Output:
# [dataframe] returns the input dataframe in a new temporary dataframe (except for 'display')
# Documentation:

def select(dataframe,category,column,value):
    print '\n','Select','\n','------'

    if category == 'display':
        print 'list of all columns and respective types available in the dataset'
        print(dataframe.dtypes)

    elif category == 'keep':
        print 'only column(s)',column,'has/have been kept'
        dfo1 = dataframe.copy()
        dfo1 = dfo1[column]
        return dfo1

    elif category == 'drop':
        print 'column(s)',column,'has/have been dropped'
        dfo6 = dataframe.copy()
        dfo6 = dfo6.drop(column,axis=1)
        return dfo6

    elif category == 'rename':
        print 'column [',column,'] has been renamed into [',value,']'
        dfo2 = dataframe.copy()
        dfo2.rename(columns = {column:value}, inplace = True)
        return dfo2

    elif category == 'retype':
        # text (object|string) | number (int64|int) | number (float64|float) | date (datetime64|date)
        print 'column [',column,'] has been converted from [',dataframe[column].dtype,'] to [',value,']'

        if value == 'text':
            dfo3 = dataframe.copy()
            #dfo3[column] = dfo3[column].astype(object)
            dfo3[column] = dfo3[column].astype(str)
            return dfo3

        elif value == 'number':
            dfo4 = dataframe.copy()
            dfo4[column] = pd.to_numeric(dfo4[column], errors='coerce')
            return dfo4

        elif value == 'date':
            dfo5 = dataframe.copy()
            pd.to_datetime(dfo5[column])
            return dfo5

        else:
            print('this data type is not available for data type change')

    else:
        print('this Select functionality is not available for the moment')


#############
# transpose #
#############
# Description: Pivots the orientation of the data so that horizontal fields
#              are moved on the vertical axis
# Input:
# [dataframe] dataframe: dataframe created by other modules and whose data
#                        need to be transposed
# [string-list] key_fields: fields to be kept as key dimension
# [string-list] data_fields: fields to be allocated to the value column
# Output:
# [dataframe] transpose_df: returns the input dataframe in a new temporary dataframe
# Documentation:
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.melt.html

def transpose(dataframe,key_fields,data_fields):
    print '\n','Transpose','\n','---------'
    print 'data have been transposed'

    transpose_df = pd.melt(dataframe, id_vars=key_fields, value_vars=data_fields)
    transpose_df.rename(columns = {'variable':'Name'}, inplace = True)
    transpose_df.rename(columns = {'value':'Value'}, inplace = True)
    return transpose_df


########
# join #
########
# Description: join right dataset to left dataset (master)
# Input:
# [dataframe] dataframe_left: left dataframe (master)
# [dataframe] dataframe_right: right dataframe
# [string-list] keys_left: one or multiple keys to use from left dataframe for join
# [string-list] keys_right: one or multiple keys to use from right dataframe for join
# [string] join_type: either inner, outer, left, right, left_only, right_only
# Output:
# [dataframe] merge_inner: dataframe with intersection of keys from both frames,
#             similar to a SQL inner join; preserve the order of the left keys
# [dataframe] merge_outer: dataframe with union of keys from both frames, similar
#             to a SQL full outer join; sort keys lexicographically
# [dataframe] merge_left: dataframe with only keys from left frame, similar to a
#             SQL left outer join; preserve key order
# [dataframe] merge_right: dataframe with only keys from right frame, similar to
#             a SQL right outer join; preserve key order
# [dataframe] merge_left_only: dataframe with only keys from left frame with no match
# [dataframe] merge_right_only: dataframe with only keys from right frame with no match
# Documentation:
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.merge.html
# https://pandas.pydata.org/pandas-docs/stable/merging.html

def join(dataframe_left,dataframe_right,keys_left,keys_right,join_type):
    print '\n','Join','\n','----'
    print 'datasets have been joined'

    if join_type == 'inner':
        merge_inner = pd.merge(dataframe_left,dataframe_right,how='inner',left_on=keys_left,right_on=keys_right,suffixes=('_LEFT','_RIGHT'))
        return merge_inner
    elif join_type == 'outer':
        merge_outer = pd.merge(dataframe_left,dataframe_right,how='outer',left_on=keys_left,right_on=keys_right,suffixes=('_LEFT','_RIGHT'))
        return merge_outer
    elif join_type == 'left':
        merge_left  = pd.merge(dataframe_left,dataframe_right,how='left',left_on=keys_left,right_on=keys_right,suffixes=('_LEFT','_RIGHT'))
        return merge_left
    elif join_type == 'right':
        merge_right = pd.merge(dataframe_left,dataframe_right,how='right',left_on=keys_left,right_on=keys_right,suffixes=('_LEFT','_RIGHT'))
        return merge_right
    elif join_type == 'left_only':
        merge_left_only = pd.merge(dataframe_left,dataframe_right,how='left',left_on=keys_left,right_on=keys_right,suffixes=('_LEFT','_RIGHT'),indicator=True)
        merge_left_only = merge_left_only[merge_left_only['_merge']=='left_only']
        merge_left_only = merge_left_only.drop(list(dataframe_right)+['_merge'],axis=1)
        return merge_left_only
    elif join_type == 'right_only':
        merge_right_only = pd.merge(dataframe_left,dataframe_right,how='right',left_on=keys_left,right_on=keys_right,suffixes=('_LEFT','_RIGHT'),indicator=True)
        merge_right_only = merge_right_only[merge_right_only['_merge']=='right_only']
        merge_right_only = merge_right_only.drop(list(dataframe_left)+['_merge'],axis=1)
        return merge_right_only

    else:
        print('this join type is not available or is not correct')


#########
# union #
#########
# Description: union 2 dataframes
# Input:
# [dataframe] dataframe_1: first dataframe
# [dataframe] dataframe_2: second dataframe
# Output:
# [dataframe] union_df: returns dataframe_1 union to dataframe_2
# Documentation:
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html

def union(dataframe_1,dataframe_2):
    print '\n','Union','\n','-----'
    print 'datasets have been union'

    union_df = dataframe_1.append(dataframe_2, ignore_index='true')
    return union_df


########
# sort #
########
# Description: sort rows according to one column - either ascending or descending
# Input:
# [dataframe] dataframe: dataframe to apply the sort on
# [string-list] column: column(s) serving as sorting keys
# [string-list] direction: ascending ('asc') or descending ('desc')
# Output:
# [dataframe] sort_df: sorted dataframe
# Documentation:
# http://pandas.pydata.org/pandas-docs/version/0.19.2/generated/pandas.DataFrame.sort.html
# http://pandas.pydata.org/pandas-docs/version/0.19.2/generated/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values

def sort(dataframe, column, direction):
    print '\n','Sort','\n','----'
    print 'dataset has been ordered',direction,'along column',column

    direction= [d.replace('asc', 'True') for d in direction]
    direction = [d.replace('desc', 'False') for d in direction]
    direction_new = [eval(d) for d in direction]
    sort_df = dataframe.sort_values(by=column, ascending=direction_new)
    return sort_df


##########
# filter #
##########

# Description: filter dataset according to given condition(s), with 2 outputs:
#              data meeting the condition(s) (true), and data not meeting it (false)
# Input:
# [dataframe] dataframe: dataframe to apply the filter on
# [string] rules: formula describing the filter rules - !should be typed between
#                 double quotes
# [string] output: specify if we want the true ('true') or the false ('false') output
# Output:
# [dataframe] filter_true: dataframe with rows meeting the rules
# [dataframe] filter_false: dataframe with rows not meeting the rules
# Documentation:
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.query.html

def filter(dataframe,rules,output):
    print '\n','Filter','\n','------'
    print 'filtering rules applied:',rules

    rules_cleaned = rules.replace("[","")
    rules_cleaned = rules_cleaned.replace("]","")

    if output == 'true':
        filter_true = dataframe.query(rules_cleaned)
        return filter_true
    elif output == 'false':
        print('false output is still to be developed')
    else:
        print('this output type or is not correct')


###########
# formula #
###########
# Description: calculate values based on existing columns, and allocate it to
#              existing or new column
# Input:
# [dataframe] dataframe: dataframe to apply the calculation on
# [string] formula: formula describing the calculation rules
# [string] column: column where formula output is allocated, either to existing
#                  or new column
# Output:
# [dataframe] calc_df: dataframe with calculated column
# Documentation:

def formula(dataframe,formula,column):
    print '\n','Formula','\n','-------'
    print 'formula applied:',column,'=',formula

    formula_cleaned = formula.replace("[","calc_df['")
    formula_cleaned = formula_cleaned.replace("]","']")

    calc_df = dataframe
    calc_df[column] = eval(formula_cleaned)
    return calc_df


###########
# comment #
###########

# Description: display comment
# Input:
# [string] text: comment
# Output:
# print text
# Documentation:

def comment(text):
    print '\n','Comment','\n','-------'
    print(text)


############
# crosstab #
############
# Description: Pivots the orientation of the data so that vertical key_fields
#              are moved on the horizontal axis
# Input:
# [dataframe] dataframe: dataframe created by other modules and whose data
#                        need to be pivoted
# [string-list] group_fields: fields to group by
# [string] column_fields: fields to be used as columns
# [string-list] value_fields: column to aggregate
# [string] aggreg_method: np.mean or np.sum
# Output:
# [dataframe] crosstab_df: returns the input dataframe in a new temporary dataframe
# Documentation:
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html
# http://pbpython.com/pandas-pivot-table-explained.html

def crosstab(dataframe,group_fields,column_fields,value_fields,aggreg_method):
    print '\n','Crosstab','\n','--------'
    print 'data have been pivoted'

    crosstab_df = pd.pivot_table(dataframe,index=group_fields,columns=column_fields,values=value_fields,aggfunc=aggreg_method)
    crosstab_df.columns = crosstab_df.columns.droplevel(0)
    crosstab_df = crosstab_df.rename_axis(None, axis=1)
    crosstab_df = crosstab_df.reset_index()
    return crosstab_df


#############
# summarize #
#############

# Description: equivalent of a pivot table in Excel
# Input:
# [dataframe] dataframe: dataframe to apply the summarize on
# [string-list] group_fields: fields to group by
# [string-list] value_fields: fields to summarize
# [string/list] aggreg_methods: the aggregation methods to be used for each
#               columns (text: group by | num: sum, average > more aggregation
#               functionalities to come)
# Output:
# [dataframe] summarize_df: summarized dataframe
# Documentation:
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html
# http://pbpython.com/pandas-pivot-table-explained.html

def summarize(dataframe,group_fields,value_fields,aggreg_methods):
    print '\n','Summarize','\n','---------'
    print value_fields,'have been grouped along the',group_fields,'dimension(s)'

    aggreg_methods_cleaned = []
    for item in aggreg_methods:
        if item == 'average':
            aggreg_methods_cleaned.append(np.mean)
        elif item == 'sum':
            aggreg_methods_cleaned.append(np.sum)
        elif item == 'median':
            aggreg_methods_cleaned.append(np.median)
        else:
            print('error')

    aggreg_methods_final = dict(zip(value_fields, aggreg_methods_cleaned))

    summarize_df = pd.pivot_table(dataframe,index=group_fields,values=value_fields,aggfunc=aggreg_methods_final)
    summarize_df = summarize_df.rename_axis(None, axis=1)
    summarize_df = summarize_df.reset_index()
    return summarize_df

    # add functionality where rename columns





# Program end #

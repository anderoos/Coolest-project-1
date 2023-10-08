# This file holds various functions to clean and sort data for Project 1
# Version: 1
# Indended to be used for Project 1 only
import numpy as np
import pandas as pd
import seaborn as sns

# Author: anderoos
# This script is meant to break up Zillow Data from the continental US into five distinct regions
# West, Midwest, Southwest, Southeast, Northeast
def split_regions(df):
    df['StateName'] = df['StateName'].astype('str')
    # Define categories
    northeast = ['ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA']
    southeast = ['DE', 'MD', 'VA', 'WV', 'NC', 'SC', 'GA', 'FL', 'AL', 'MS', 'LA', 'KY', 'TN']
    midwest = ['OH', 'IN', 'IL', 'MI', 'WI', 'MN', 'IA', 'MO', 'ND', 'SD', 'NE', 'KS']
    west = ['MT', 'ID', 'WY', 'CO', 'NM', 'AZ', 'UT', 'NV', 'CA', 'OR', 'WA', 'AK', 'HI']
    southwest = ['TX', 'OK', 'AR']
    # Filters state codes into separate dataframes
    ne_df = df[df['StateName'].isin(northeast)]
    se_df = df[df['StateName'].isin(southeast)]
    mw_df = df[df['StateName'].isin(midwest)]
    w_df = df[df['StateName'].isin(west)]
    sw_df = df[df['StateName'].isin(southwest)]
    return ne_df, se_df, mw_df, w_df, sw_df


# Author: anderoos
# This script is meant to fill in na or nan values with averages of flanking cells
def fill_zero_with_avg(df):
    new_df = df.copy()     # Create Copy
    for col in df.columns:  # Iterate over columns
        if df[col].dtype == 'object': # If its non-numeric, pass over it
            pass
        else:
            for index, row in df.iterrows(): # for index and row, if the value is na
                if pd.isna(row[col]):
                    indexer = 1
                    # Capture adjacent values
                    while (index + indexer) in df.index and pd.isna(df.at[index + indexer, col]):
                        indexer += 1
                    if (index - 1) in df.index and (index + indexer) in df.index:
                        # Generate average of flanking values
                        new_df.at[index, col] = (df.at[index - 1, col] + df.at[index + indexer, col]) / 2
    return new_df

# Author: anderoos
# Converts all columns to numeric 
def convert_to_numeric(df, start_index = 2):
    for column in df.columns[start_index:]:
        # df[column] = df[column].str.replace(",", "")
        # df[column] = df[column].str.replace(".", "")
        df[column] = pd.to_numeric(df[column])
    return df

# Author: anderoos
# Capture one state
def get_state_data(df, state='NY'):
    df['StateName'] = df['StateName'].astype('str')
    # Filters state codes into separate dataframes
    sub_frame = df[df['StateName'].isin(state)]
    return subframe

# Author: anderoos
# Grab specific dates
# Can only be used after a table has been transposed and properly converted to datetime using pd.to_datetime
# Accepts year as a list and months as a list
def get_specific_dates(df, year, month=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
    filtered_df = df.loc[(df.index.year.isin(year))]
    filtered_df = filtered_df.loc[filtered_df.index.month.isin(month)]
    return filtered_df
    
# Author: anderoos
# Grab specific date ranges
# Can only be used after a table has been transposed and properly converted to datetime using pd.to_datetime
def get_specific_date_range(df, datestart, dateend):
    filtered_df = df[(df.index >= datestart) & (df.index <= dateend)]
    return filtered_df

    
    
# Open the data on Yandex.Music and explore it.

# You'll need `pandas`, so import it.

import pandas as pd

#Read the file `music_project_en.csv` from the `/datasets/` folder and save it in the `df` variable:

df = pd.read_csv('music_project_en.csv')
# csv is comma seperated value
# Print the first 10 table rows:

first_10_rows = df.head(10) # obtaining the first 10 rows from the df table

# Obtaining the general information about the table with one command:

print(df.head(10)) # obtaining general information about the data in df

print(df.columns)

df = df.rename(columns={
    '  userID': 'user_id',
    'Track': 'track',
    'artist': 'artist',
    'genre': 'genre',
    '  City  ': 'city',
    'time': 'time',
    'Day': 'day'
})
# renaming columns

print(df.columns) # checking result: the list of column names

print(df.isna().sum()) # calculating missing values

df['track'] = df['track'].fillna('unknown')
df['artist'] = df['artist'].fillna('unknown')
df['genre'] = df['genre'].fillna('unknown') # looping over column names and replacing missing values with 'unknown'

print(df.isna().sum()) # counting missing values

df = df.drop_duplicates() # removing obvious duplicates

print(df.duplicated)# checking for duplicates
print(df['genre'].unique()) # viewing unique genre names

wrong_genres_list = ['hip', 'hop', 'hip-hop']
correct_genre = 'hiphop'

def replace_wrong_values(wrong_values, correct_value):
    for wrong_value in wrong_values: # looping over misspelled names
        replace_wrong_genres(df, wrong_genres, correct_genre) # removing implicit duplicates

unique_genres = df['genre'].unique()
print(unique_genres)
# checking for implicit duplicates

city_track_counts = df.groupby('city')['track'].sum() # Print the track counts for each city
# Counting up the tracks played in each city

daily_track_counts = df.groupby('day')['track'].sum()
# Calculating tracks played on each of the three days
print(city_track_counts) # Print the track counts for each city
# Counting up the tracks played in each city

day_group = df.groupby('day')
daily_track_counts = day_group['track'].sum()
print(daily_track_counts)
# Calculating tracks played on each of the three days

# <creating the function number_tracks()>
def number_tracks(day,city): # We'll declare a function with two parameters: day=, city=.
    track_list = df.loc[(df['day'] == day) & (df['city'] == city)] # Let the track_list variable store the df rows where   
    # the value in the 'day' column is equal to the day= parameter and, at the same time, 
        # the value in the 'city' column is equal to the city= parameter (apply consecutive filtering 
        # with logical indexing).
    track_list_count = track_list['user_id'].count() # Let the track_list_count variable store the number of 'user_id' column values in track_list
    return track_list_count # (found with the count() method).
# Let the function return a number: the value of track_list_count.

# The function counts tracked played for a certain city and day.
# It first retrieves the rows with the intended day from the table,
# then filters out the rows with the intended city from the result,
# then finds the number of 'user_id' values in the filtered table,
# then returns that number.
# To see what it returns, wrap the function call in print().

number_tracks('Monday', 'Springfield')
# the number of songs played in Springfield on Monday

number_tracks('Monday', 'Shelbyville') # the number of songs played in Shelbyville on Monday

number_tracks('Wednesday', 'Springfield') # the number of songs played in Springfield on 

number_tracks('Wednesday', 'Shelbyville') # the number of songs played in Shelbyville on Wednesday

number_tracks('Friday', 'Springfield') # the number of songs played in Springfield on Friday

number_tracks('Friday', 'Shelbyville') #the number of songs played in Shelbyville on Friday

data = {
    "city": ["Shelbyville", "Springfiled"],
    "monday" : [5614, 15740],
    "wednesday" : [7003, 11056],
    "friday" : [5895, 15945]
}

print(data)

# create the spr_general table from the df rows, 
# where the value in the 'city' column is 'Springfield'
spr_general = df[df[('city')] == 'Springfield']

# create the shel_general from the df rows,
# where the value in the 'city' column is 'Shelbyville'
shel_general = df[df[('city')] == 'Shelbyville']

# 1) Let the genre_df variable store the rows that meet several conditions:
#    - the value in the 'day' column is equal to the value of the day= argument
#    - the value in the 'time' column is greater than the value of the time1= argument
#    - the value in the 'time' column is smaller than the value of the time2= argument
#    Use consecutive filtering with logical indexing.

# 2) Group genre_df by the 'genre' column, take one of its columns, 
#    and use the count() method to find the number of entries for each of 
#    the represented genres; store the resulting Series to the
#    genre_df_count variable

# 3) Sort genre_df_count in descending order of frequency and store the result
#    to the genre_df_sorted variable

# 4) Return a Series object with the first 15 genre_df_sorted value - the 15 most
#    popular genres (on a given day, within a certain timeframe)

# Write your function here
def genre_weekday(df, day, time1, time2):
    
    # consecutive filtering
    # Create the variable genre_df which will store only those df rows where the day is equal to day=
    genre_df = df[df['day'] == day] # write your code here

    # filter again so that genre_df will store only those rows where the time is smaller than time2=
    genre_df = df[(df['day'] == day) & (df['time'] < time2)] # write your code here

    # filter once more so that genre_df will store only rows where the time is greater than time1=
    genre_df = df[(df['day'] == day) & (df['time'] > time1) & (df['time'] < time2)] # write your code here

    # group the filtered DataFrame by the column with the names of genres, take the genre column, and find the number of rows for each genre with the count() method
    genre_df_count = genre.df.groupby('genre')['genre'].count() # write your code here

    # sort the result in descending order (so that the most popular genres come first in the Series object)
    genre_df_sorted = genre_df_count.sort_values(ascending=False) # write your code here

    # we will return the Series object storing the 15 most popular genres on a given day in a given timeframe
    return genre_df_sorted[:15]

number_tracks('Monday', 'Springfield')
# the number of songs played in Springfield on Monday
number_tracks('Monday', 'Shelbyville') # the number of songs played in Shelbyville on Monday
number_tracks('Wednesday', 'Springfield') # the number of songs played in Springfield on Wednesday
number_tracks('Wednesday', 'Shelbyville') # the number of songs played in Shelbyville on Wednesday
number_tracks('Friday', 'Springfield') # the number of songs played in Springfield on Friday
number_tracks('Friday', 'Shelbyville') #the number of songs played in Shelbyville on Friday

# table with results
import pandas as pd
columns = ['City', 'Monday', 'Wednesday', 'Friday']
data = [['Springfield', 16715, 11755, 16890],
        ['Shelbyville', 5982, 0, 6259]]
df_number_tracks = pd.DataFrame(data=data, columns=columns)

spr_general = df[df['city'] == 'Springfield']
print(spr_general.head())
# where the value in the 'city' column is 'Springfield'
# create the spr_general table from the df rows, 
# create the shel_general from the df rows,
# where the value in the 'city' column is 'Shelbyville'
shel_general = df[df['city'] == 'Shelbyville']
print(shel_general.head())


# Write your function here
def genre_weekday(df, day, time1, time2):
    
    # consecutive filtering
    # Create the variable genre_df which will store only those df rows where the day is equal to day=
    genre_df = df[df['day'] == day] # write your code here

    # filter again so that genre_df will store only those rows where the time is smaller than time2=
    genre_df = df[df['time'] < time2] # write your code here

    # filter once more so that genre_df will store only rows where the time is greater than time1=
    genre_df = df[df['time'] > time1] # write your code here

    # group the filtered DataFrame by the column with the names of genres, take the genre column, and find the number of rows for each genre with the count() method
    genre_df_count = df.groupby('genre')['genre'].count() # write your code here

    # sort the result in descending order (so that the most popular genres come first in the Series object)
    genre_df_sorted = genre_df_count.sort_values(ascending=False) # write your code here

    # we will return the Series object storing the 15 most popular genres on a given day in a given timeframe
    return genre_df_sorted[:15]

genre_weekday(shel_general, 'Monday', '07:00', '11:00') # calling the function for Monday morning in Springfield (use spr_general instead of the df table)

genre_weekday(spr_general, 'Monday', '07:00', '11:00')# calling the function for Monday morning in Shelbyville (use shel_general instead of the df table)

genre_weekday(spr_general, 'Friday', '17:00', '23:00')# calling the function for Friday evening in Springfield

genre_weekday(shel_general, 'Friday', '17:00', '23:00')# calling the function for Friday evening in Shelbyville


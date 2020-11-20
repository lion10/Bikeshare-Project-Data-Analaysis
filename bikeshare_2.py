import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print('\nWhat the data of the city you would like to see please! (Chicago,New York City,Washington): ')
        city = input().title()
        if(city not in CITY_DATA.keys()):
            print('\nPlease enter the name of city correctly')                
    print('\nYou entered this {} city'.format(city))    

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'All': 0, 'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6}
    month = ''
    while month not in MONTH_DATA.keys():
        print('\nWhat the data of the month you would like to see [January, February ... , June]!')
        month = input().title()
        if month not in MONTH_DATA.keys():
            print('\nPlease enter the months correctly')
    print('\nYou entered this {} month'.format(month))  
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_LIST = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = ''
    while day not in DAY_LIST:
        print('\nWhat is the day you would like to see please! ')
        day = input().title()
        if day not in DAY_LIST:
            print('\nPlease enter the day correctly')
    print('\nYou entered this {} day'.format(day))
    
    print('-'*40)
    print('\nYou entered city: {}, month: {}, day: {}'.format(city,month,day))
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title() ]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print('\nMost common month between [January, February ... , June] is {}'.format(most_common_month))
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print('\nMost common day is {}'.format(most_common_day))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract hour from the Start Time column to create an hour column
    df['hour'] =pd.to_datetime(df['Start Time']).dt.hour
    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print('\nMost common start hour is {}'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('\nMost commonly used start station {}'.format(most_common_start_station))
        

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('\nMost commonly used end station {}'.format(most_common_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    most_common_combination_start_end_station = df['Start Station'].str.cat(df['End Station']).value_counts().idxmax()
    print('\nMost frequent combination of start station and end station trip {}'.format(most_common_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    minute,secound = divmod(total,60) # Return Integer division and modulo 
    hour,minute =divmod(minute,60)

    print('\nTotal travel time: {}, which is it takes {} hours,{} minutes, {} scounds'.format(total, hour , minute , secound))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean().round(0) # Rounds mean to nearest integer, e.g. 1.95 = 2 and 1.05 = 1 
    mins,secs = divmod(mean_travel_time,60)
    hrs,mins =divmod(mins,60)

    print('\nTotal avarge travel time: {}, which is it takes {} hours,{} minutes, {} scounds'.format(mean_travel_time, hour , minute , secound))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types =  df['User Type'].value_counts()
    print('\nNumber of user types is: {}'.format)
    
    # TO DO: Display counts of gender
    try:
        count_user_types =  df['Gender'].value_counts()
        print('\nNumber of user types is: {}'.format(count_user_types))
    except: 
        print('\nThere is no gender data in this city')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].value_counts().idxmax())
        print('\nEarliest is {}, most recent is {}, most common year is {}'.format(earliest,most_recent,most_common_year))
    except:
        print('\nThere is no Birth Year data in this city')
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_rows_data(df): 
    """ Displays 5 rows of the data.
        args:
            Dataframe df: data frame to display the data 
        Returns:
            None
    """

    start_time = time.time()

    answers = ['Yes','No']
    respons = ''
    count = 0 
    while respons not in answers:
        print('\nDo u like to look at data? [yes, no]')
        respons = input().title()
        if respons == 'Yes':
            print('\n you entered {} '.format(respons))
            print(df.head())
        elif respons not in answers:
            print('\n please enter yes or no')
    
    while respons == 'Yes':
        print('\n would like to show more data')
        count += 5
        respons = input().title()
        if respons == 'Yes':
            print(df[count: count+5])
        elif respons != "yes":
             break

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*80)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
           

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rows_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

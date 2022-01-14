import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True:
        cities= ['chicago','new york city','washington']
        city= input("\n Please input city to analyse? (Chicago, New York city, Washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a valid name of city.")  
    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months= ['All','January','February','March','April','June','May']
        month = input("\n Considering which month? (January, February, March, April, May, June)? Type 'All' for no month filter\n").title()
        if month in months:
            break
        else:
            print("\n Please enter a valid month")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days= ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day = input("\n Which day of the week would you like to consider? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? Type 'All' for no day filter \n").title()         
        if day in days:
            break
        else:
            print("\n Please enter a valid day name") 

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month] 

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]

    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month=='All':
        popular_month= df['month'].mode()[0]
        months= ['January','February','March','April','May','June']
        popuplar_month= months[popular_month-1]
        print("The most Popular month is",popular_month)
        
    # TO DO: display the most common day of week
    if day=='All':
        popular_day= df['day_of_week'].mode()[0]
        print("The most Popular day is",popular_day)


    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    popular_hour=df['Start Hour'].mode()[0]
    print("The popular Start Hour is {}:00 hrs".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station= df['Start Station'].mode()[0]
    print("The most commonly used Start Station is {}".format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station= df['End Station'].mode()[0]
    print("The most commonly used End Station is {}".format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['combine_start_end']=df['Start Station']+" "+"to"+" "+ df['End Station']
    popular_combo= df['combine_start_end'].mode()[0]
    print("The most frequent combination of Start and End Station is {} ".format(popular_combo))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration=df['Trip Duration'].sum()
    minute,second=divmod(total_duration,60)
    hour,minute=divmod(minute,60)
    print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(hour,minute,second))

    # TO DO: display mean travel time
    average_duration=round(df['Trip Duration'].mean())
    m,sec=divmod(average_duration,60)
    if m>60:
        h,m=divmod(m,60)
        print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(h,m,sec))
    else:
        print("The total trip duration: {} minute(s) {} second(s)".format(m,sec))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts= df['User Type'].value_counts()
    print("The user types are:\n",user_counts)

    # TO DO: Display counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        gender_counts= df['Gender'].value_counts()
        print("\nThe counts of each gender are:\n",gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest= int(df['Birth Year'].min())
    print("\nThe oldest user is born of the year",earliest)
    most_recent= int(df['Birth Year'].max())
    print("The youngest user is born of the year",most_recent)
    common_birth_year= int(df['Birth Year'].mode()[0])
    print("Most users are born of the year",common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

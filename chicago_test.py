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
    city = input("Which city would you like to explore ? : ")
    if city.lower() in CITY_DATA:
            break
    else:
        print("The city you have entered is not on the database, please enter relevant city")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("That's great ! Which month would you want to look into? : ").lower()
    while month not in ['all','january','febraury','march','april','may','june']:
        month = input("Enter a relevant month from the following : 'all','january','febraury','march','april','may','june' ")
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter for which day of the week would you like to look at the data for : ")

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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all' :
       
       months = ['january','febraury','march','april','may','june']
       month = months.index(month)+1
       
       df = df[df['month'] == month]
    
    if day != all :
       
       df = df[df['day_of_week'] == day.title()]               

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most Popular Month (1 = January,...,6 = June): {common_month}")

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0] 
    print(f"\nMost Popular Day: {popular_day}")                  

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour()
    
    popular_hour = df['hour'].mode()[0]   
   
    print(f"The most popular hour is: {popular_hour}")   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most popular start station is: {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most popular start station is: {common_end_station}")
   

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'].str.cat(df['End Station'], sep= ' to ')
    combo = df['Start to End'].mode()[0]
       
    print(f"\nThe most frequent combination of trips are from {combo}.")   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print(f"The total travel duration was : {total_time}")

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f"The average time taken was: {mean_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_typ = df['User Type'].value_counts()
    print(f"The total types of users: {user_typ}")
    # TO DO: Display counts of gender
    try:
       genders = df['Gender'].value_counts()
       print(f"\n The types of users by gender are as follows: {genders}")
    except:
       print("There is 'no' gender data for this file")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
            print("There are no birth year details in this file.")
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

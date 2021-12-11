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
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            check = int(input('Choose your city:\n1 or -2 for Chicago.\n2 or -1 for NY city.\n3 or 0 for Washington DC.\n\n'))
            city_list = ['chicago', 'new york city', 'washington']
            city = city_list[check-1]
            break
        except:
            print("\nInvalid input, please make sure you choose from 1|-2 or 2|-1 or 3|0.\n")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            check = int(input('\nChoose the month by number from 1=(January) >>to>> 6=(JUNE).\nAnd 0 for all.\n\n'))
            month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
            month = month_list[check]
            break 
        except:
            print("\nInvalid input, please make sure you choose from 0 to 6.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day of week you want to filter with?\nYou can type all for not filtering.\n\n').lower()
        weekday_name_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saterday',  'sunday']
        if day not in weekday_name_list:
            print('\nTry to spell it right : \n{}\n'.format(weekday_name_list))
        else:
            break
    
#    print('\n{} , {} , {}.\n'.format(city, month, day))

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
    
    if month != 'all':
        month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = month_list.index(month)
        df = df[df['month'] == month]
    
    if day != 'all':
        day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saterday',  'sunday']
        df = df[df['day_of_week'] == day.title()]
        
#    print(df)
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('- Most common month : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('- Most common day of week : {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('- Most common start hour : {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('- Most commonly used start station : {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('- Most commonly used end station : {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    print('- Most frequent combination trip : {}'.format(df['Trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('- Total travel time = {} days '.format(df['Trip Duration'].sum()/(60*60*24)))

    # TO DO: display mean travel time
    print('- Average travel time = {} minutes'.format(df['Trip Duration'].mean()/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('- Counts of user types : \n{}\n'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    try:
        print('- Counts of user gender : \n{}\n'.format(df['Gender'].value_counts()))
    except:
        print("- Counts of user gender : \n  error\n  Washington dataframe has no column called Gender.\n  It's only in Chicago and NY City.\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('- Earlist year : {}\n  Most recent year : {}\n  Most common year : {}'.format(min(df['Birth Year']), max(df['Birth Year']), df['Birth Year'].mode()[0]))
    except:
        print("- Earlist, most recent and common years : \n  error\n  Washington dataframe has no column called Birth Year.\n  It's only in Chicago and NY City.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_raw_data(df):
    """ Asking user if he wants to see raw data. """
    i = 0
# TO DO: convert the user input to lower case using lower() function
    raw = input("Do you want to check for raw data? ('yes' or 'no')\n\n").lower()
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
# TO DO: appropriately subset/slice your dataframe to display next five rows
            print(df[i:i+5])
# TO DO: convert the user input to lower case using lower() function
            raw = input("\nWant to see next five?\n\n").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

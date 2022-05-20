import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': "C:\\Users\\Lenovo\\Downloads\\Telegram Desktop\\chicago.csv",
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    city = input("inter your city : ").lower()
    while city not in cities:
        print("You provided invalid city")
        city = input("inter the city again : ").lower()

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    getting = input("search by month or day or both : ")
    if getting.lower() == "month" or getting.lower() == "both":
        month = input("inter the month : ").lower()
        while month not in months:
            print("You provided invalid month")
            month = input("inter the month again : ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["sat", "sun", "mon", "tues", "fri", "all"]
    if getting.lower() == "day" or getting.lower() == "both":
        day = input("inter the day : ").title().lower()
        while day not in days:
            print("You provided invalid day")
            day = input("inter the day again : ").title().lower()

    print('-' * 40)
    return city, month, day  # error is here  (Local variable 'month' might be referenced before assignment)


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
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month = df["month"].mode()
    print("the most common month is : ", most_month)

    # display the most common day of week
    most_day = df["day_of_week"].value_counts().idxmax()
    print("the most common day of week is : ", most_day)

    # display the most common start hour
    most_hour = df["hour"].value_counts().idxmax()
    print("the most common start hour is : ", most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_ss = df["Start Station"].mode()[0]
    print("most commonly used start station is : ", most_ss)

    # display most commonly used end station
    most_es = df["End Station"].mode()[0]
    print("most commonly used end station is : ", most_es)

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df["Trip Duration"].sum()
    print(total_time)

    # display mean travel time
    count = df["Trip Duration"].count()
    average = total_time / count
    print(average)
    # total_time = df["Trip Duration"].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user = df["User Types"].value_counts()
    print(count_user)

    # Display counts of gender
    if city == "new york city" or city == "washington":
        count_gender = df["Gender"].value_counts()
        print(count_gender)

    # Display earliest, most recent, and most common year of birth
    most_ear = df["Birth Year"].min()
    most_recent = df["Birth Year"].max()
    most_year = df["Birth Year"].mode()[0]
    print("earliest year is : ", most_ear, " most recent year is : ", most_recent, "most common year of birth is : ", most_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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

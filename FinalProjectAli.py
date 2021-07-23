import time
import pandas as pd
import numpy as np

#dictionary for files names 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# dictionary for days index in the system 
DAY_DATA = {  'monday'  : '0',
            'tuesday'   : '1',
            'wednesday' : '2',
            'thursday'  : '3',
            'friday'    : '4',
            'saturday'  : '5',
            'sunday'    : '6'}
#list of days to print the day name by index 
days = [ 'Monday','Tuesday'  ,'Wednesday','Thursday' ,'Friday'   ,'Saturday' ,'Sunday']

MONTH_DATA = {
            'january'   : '1',
            'february'  : '2',
            'march'     : '3',
            'april'     : '4',
            'may'       : '5',
            'june'      : '6'}
moths =['January', 'February', 'March', 'April', 'May', 'June']

# a function that validates user input

def ValidateUserInput(DisplyText,Options):
     while True:
        userInpot = input(DisplyText+" ").lower()
        if userInpot in Options:
            return userInpot
        else:
            print("not valid input,please try again")

def get_filters():
    city="all"
    month="all"
    day="all"
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago","new york city","washington"]
    city =ValidateUserInput("Would you like to see data for Chicago, New York city, or Washington?",cities)

    # Filter options
    options = ["month","day","both","not at all"]
    Filteroption =ValidateUserInput("Would you like to filter the data by month, day, both, or not at all?",options)
    if Filteroption == options[0] or Filteroption == options[2]:#month
    # TO DO: get user input for month (all, january, february, ... , june)
        months = ["january","february","march","april","may","june"]
        month =ValidateUserInput("Which month - January, February, March, April, May, or June?",months)

    if   Filteroption == options[1] or Filteroption == options[2]:#Day
       # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
       days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
       day =ValidateUserInput("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?",days)
    
   
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

    csvData = pd.read_csv(CITY_DATA[city])
    df =pd.DataFrame(csvData)
    
    
    df["DayOfWeek"] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df["Month"] = pd.to_datetime(df['Start Time']).dt.month
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour
  
    if month != "all":
        df = df.loc[df["Month"] ==int(MONTH_DATA[month])]
    if day != "all":
        df = df.loc[df["DayOfWeek"] ==int(DAY_DATA[day])]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    
    print('Most common Start Month:', moths[common_month-1])

    # TO DO: display the most common day of week
    common_day = df['DayOfWeek'].mode()[0]
    print('Most common Start Day:', days[common_day-1])

    # TO DO: display the most common start hour

    
    common_hour = df['Hour'].mode()[0]
    
    print('Most common Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_Start_Station = df['Start Station'].mode()[0]
    print('Most common Start Station:', common_Start_Station)


    # TO DO: display most commonly used end station
    common_End_Station = df['End Station'].mode()[0]
    print('Most common End Station:',    common_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = (df['Start Station']+" and "+df['End Station']).mode()[0]
    print('Most common End Station:', common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration']).sum()
    print('total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration']).mean()
    print('average travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type',user_types )

    # TO DO: Display counts of gender
    if 'Gender' in df.columns.tolist():
        gender = df['Gender'].value_counts()
        print('Gender',gender )
    else :
        print('Gender : No Data To Show' )

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns.tolist() :
        earliest_Birth_Year = df['Birth Year'].min()
        print('Earliest Year Of Birth',earliest_Birth_Year )
        
        recent_Birth_Year = df['Birth Year'].max()
        print('Recent Year Of Birth',recent_Birth_Year )

        Common_Birth_Year = df['Birth Year'].mode()[0]
        print('Common Year Of Birth ',Common_Birth_Year )
    else:
        print ("Birth Year: No Data To Show")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_extra_data(df):
    len_of_df = len(df)
    index = 0
    page_size= 5 
    options = ["yes", "no"] 
    while index <len_of_df : 
        print(df[index:index + page_size])
        user_input =  ValidateUserInput("would you like to see more data ? (yes/no)",options)
        if user_input == "no":
            break 
        index = index +page_size
    print("No More Data To Show")
     
 


def main():
    while True:
        city, month, day = get_filters()
       
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_extra_data(df) 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

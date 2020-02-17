
import time
import pandas as pd


# Autor: Ricky Helfgen Feb. 2020


#Would you like to filter the data by month, day, or not at all?
#(If they chose month) Which month - January, February, March, April, May, or June?
#(If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

# Dictionary of the variables
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

dict_day_number ={0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Saturday", 6 : "Sunday", 20 : "all"}
dict_month_number = { 1: "January", 2 : "Febuary", 3 : "March", 4 : "April", 5:  "May", 6:  "June", 7 : "July", 8 : "August", 9 :  "September", 10:  "Octobr", 11 : "November", 12 : "December", 20 : "all", 0: "none"}
dict_day ={"mo": 0, "tu": 1, "we" : 2, "th" : 3, "fr" : 4, "sa": 5 , "su": 6, "all": 20}
dict_month = {"jan":1, "feb":2, "mar":3, "apr":4, "may":5, "jun":6, "jul":7, "aug":8, "sep":9, "oct":10, "nov":11, "dec":12, "all": 20, "none": 0}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    #change color
    print("\033[2;37;40m Underlined text\033[0;37;40m \n")
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cit = input('Would you like to see data for: \n Chicago ="Chicago" \n New York ="New_York" \n or Washington ="Washington" \n?').lower()
        if cit not in ('chicago','new_york','washington'):
            print('Wrong Input! Please do Input again!')
        else:
            if cit == 'chicago':
                city = 'chicago.csv'
                break
            elif cit == 'new_york':
                city = 'new_york_city.csv'
                break
            elif cit == 'washington':
                city = 'washington.csv'
                break         
    # get user input for month (all, january, february, ... , june)
    while True:
        inter_val = input('Would you like to filter the data by \n a: month \n b: weekday \n c: both \n d: not at all \n (Enter 1,2,3 or 4)\n?')
        if inter_val not in ('a','b','c','d'):
            print('Wrong Input! Please repeat!')
        else:
            if inter_val == 'a':
                month = input('Input requested month: \n (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec) \n?').lower()
                if month not in ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'):
                    print('Wrong Input! Please repeat!')
                else:
                    month = month
                    day = 'none'
                    break
                    print('-'*40)
            elif inter_val == 'b':
                day = input('Input requested day: \n (Mo,Tu,We,Th,Fr,Sa;Su) \n?').lower()
                if day not in ('mo','tu','we','th','fr','sa','su'):
                    print('Wrong Input! Please repeat!')
                else:
                    day = day
                    month = 'none'
                    break
                    print('-'*40)
            elif inter_val == 'c':
                month = input('Input requested month: \n (Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec) \n?').lower()
                if month not in ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'):
                    print('Wrong Input! Please repeat!')
                else:
                    month = month
                    day = input('Input requested day: \n (Mo,Tu,We,Th,Fr,Sa;Su) \n?').lower()
                    if day not in ('mo','tu','we','th','fr','sa','su'):
                        print('Wrong Input! Please repeat!')
                    else:
                        day = day
                        month = month
                        break
                        print('-'*40)
            elif inter_val == 'd':
                #time_int = 'all'
                month = 'all'
                day = 'all'
                break
                print('-'*40)

    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    print('current filter: City:', city, 'Month:',  month.upper(), 'Day:',  day.upper())
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
    #df['Start Time'].str.contains(month)
    
    
    df = pd.read_csv(city, sep=",")
    df['date'] =  pd.to_datetime(df['Start Time'], infer_datetime_format=True)
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['weekday'] = df['date'].dt.weekday
    
    
    #Test if month is out of range
    max_month_int = int(df['month'].max())
    max_month_name = dict_month_number[max_month_int]
    monthtest = int(dict_month[month])

    #if monthtest > max_month_int:
     #   print('Sorry, Month is out of Range!, please take an other Month')
      #  get_filters()
    
    #Now get filter    
    if month == "all":
        return df
    else:
        if month == 'none':
            df = df[df['weekday'] == dict_day[day]]
            return df
        elif day == 'none':
            while True:
                if monthtest > max_month_int:
                    new_month = input('Sorry, Month is out of Range!, please take an other Month \n latest Month is: ' + max_month_name + '\n?').lower()
                    if new_month not in ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'):
                        print('Wrong Input! Please repeat!')
                    else:
                        df = df[df['month'] == dict_month[new_month]]
                        return df
                        break
                else:
                    df = df[df['month'] == dict_month[month]]
                    return df
        else:
            while True:
                if monthtest > max_month_int:
                    new_month = input('Sorry, Month is out of Range!, please take an other Month \n latest Month is: ' + max_month_name + '\n?').lower()
                    if new_month not in ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'):
                        print('Wrong Input! Please repeat!')
                    else:
                        df = df[df['month'] == dict_month[new_month]]
                        df = df[df['weekday'] == dict_day[day]]
                        return df
                        break
                            
                else:
                    df = df[df['month'] == dict_month[month]]
                    df = df[df['weekday'] == dict_day[day]]
                    return df
            
        #print('Sorry, no Data from this Month available! \nFilter: all')
        #return df
    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("\033[1;32;40m \n")
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    n_month_max = df.groupby('month').size().max()
    most_common_month_int = df['month'].mode()[0]
    most_common_month = dict_month_number[most_common_month_int]
    print('The most common month in this Timeperiod was:', most_common_month)
    print('It was count:' ,n_month_max)
    
    # display the most common day of week
    n_weekday_max = df.groupby('day').size().max()
    most_common_weekday_int = df['weekday'].mode()[0]
    most_common_weekday = dict_day_number[most_common_weekday_int]
    print('The most common weekday in this Timeperiod was:', most_common_weekday)
    print('It was count:' ,n_weekday_max)
    #print(most_common_weekday_int)
    # display the most common start hour
    df['hour'] = df['date'].dt.hour
    most_common_starthour_int = df['hour'].mode()[0]
    n_starthour_max = df.groupby('hour').size().max()
    print('The most common starthour in this Timeperiod was: ', most_common_starthour_int, "o'clock")
    print('It was count:', n_starthour_max)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print("\033[1;37;40m \n")
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common Start Station in this Timeperiod was: ', most_common_start_station)
    n_start_station_max = df.groupby('Start Station').size().max()
    print('It was count: ', n_start_station_max)
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common End Station in this Timeperiod was: ', most_common_end_station)
    n_end_station_max = df.groupby('End Station').size().max()
    print('It was count: ', n_end_station_max)
    # display most frequent combination of start station and end station trip
    df['start_end'] = (df["Start Station"] + "_" + df["End Station"])
    most_common_stations = df['start_end'].mode()[0]
    #print(most_common_stations)
    print('The most frequent combination of start und end station trip was: ', most_common_stations)
    n_stations_max = df.groupby('start_end').size().max()
    print('It was count: ', n_stations_max)
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print("\033[1;32;40m \n")
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    sum_duration = df['Trip Duration'].sum()
    print('Total of trip duration: ', sum_duration)
    print('-'*40)
    # display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('Average of trip duration: ', mean_duration)
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("\033[1;37;40m \n")
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df.groupby('User Type')['User Type'].count()
    print('User Types: \n' , count_user_types)
    print('-'*40)
    # Display counts of gender
    try:
        count_gender = df.groupby('Gender')['Gender'].count()
        print('User - Gender: \n' , count_gender)
        print('-'*40)
    except:
        print('Sorry there are no Gender Datas available!')
        print('-'*40)
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = int(df['Birth Year'].min())
        print('The earliest birth: ', earliest_birth)
        most_recent_birth = int(df['Birth Year'].max())
        print('The most recent birth: ', most_recent_birth)
        most_common_birth = int(df['Birth Year'].mode()[0])
        print('The most common birth: ', most_common_birth)
        print('-'*40)
    except:
        print('Sorry, there are no Birth Datas available!')
        print('-'*40)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)

# single data
def ind_trip_data(df):
    y=1
    while y < (len(df)):
        a = y
        for i in range(5):
            print(df.iloc[a,[1,2,3,4,5,6]])
            a +=1
            #print(y)
            #end_data = input("Next single Data? type 'enter' for yes or 'n' for no \n?")
            #if end_data.lower() == 'n':
             #   break
        y += 5
        end_data = input("Next single Data? type 'enter' for yes or 'n' for no \n?")
        if end_data.lower() == 'n':
            break
        
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        nextdata = input('Push Enter to see station statistics')
        if nextdata.lower() == 'n':
            break
        station_stats(df)
        
        nextdata = input('Push Enter to see trip duration statistics')
        if nextdata.lower() == 'n':
            break
        trip_duration_stats(df)
        
        nextdata = input('Push Enter to see user statistics')
        if nextdata.lower() == 'n':
            break
        user_stats(df)
        
        single_data = input('Would you like to see single Data? y/n \n?')
        if single_data.lower() != 'n':
            ind_trip_data(df)
        
        
        restart = input('\nWould you like to restart? Enter y/n.\n?')
        if restart.lower() != 'y':
            print('Have a good time!')
            break


if __name__ == "__main__":
	main()

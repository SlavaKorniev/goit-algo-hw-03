def get_upcoming_birthdays(users):
    from datetime import datetime, timedelta
    
    congratulation_users_date = []
    
    
    date_now_object = datetime.today().date()   #take date today
    year_now = date_now_object.year

    
    for user_birthdays in users:
        user_date = {}       
        # change type date_user to date
        date_user_birthday = datetime.strptime(user_birthdays["birthday"], "%Y.%m.%d").date()
        
        # change year in date_user on curently
        present_date_user_birthday = datetime(year=year_now, month=date_user_birthday.month, day=date_user_birthday.day).date()
            
        weekday_birsday = present_date_user_birthday.weekday()
        
        # congratulations day
        if weekday_birsday == 5:
            present_date_user_congratulations = present_date_user_birthday + timedelta(days=2)
        
        elif weekday_birsday == 6:
            present_date_user_congratulations = present_date_user_birthday + timedelta(days=1)        

        else:
            present_date_user_congratulations = present_date_user_birthday
        
        
         #find difference between users congratulations date and today
        date_user_delta = present_date_user_congratulations - date_now_object        

        if 0<= date_user_delta.days <=7:            
            user_date["name"] = user_birthdays ["name"] #copy names to dictionary
            user_date["congratulation_date"] = present_date_user_congratulations.strftime("%Y.%m.%d") #copy congratulations date
            
            congratulation_users_date.append(user_date)

    return congratulation_users_date




users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:\n", upcoming_birthdays)

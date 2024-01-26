def get_days_from_today(date: str) -> int:
    # format date: str 'YYYY-MM-DD'
    from datetime import datetime
    
    date_now_object = datetime.today()
        
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        date_diference = date_now_object - date_object
        days_from_today = int (date_diference.days)
        
        return days_from_today
    
    except Exception:
        print("Incorect data format. Enter please str 'YYYY-MM-DD'")



print (get_days_from_today("2021-10-09"))


def month_name_to_number(month):
    from datetime import datetime
    month_number = datetime.strptime(month, '%B').month
    return month_number
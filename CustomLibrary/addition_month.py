from datetime import datetime
from dateutil.relativedelta import relativedelta


def add_time(n):
    date_after_month = datetime.today()+ relativedelta(months=n)
    return date_after_month.strftime('%Y-%m-%d')

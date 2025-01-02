import time
from datetime import datetime, timezone, timedelta
import calendar

print("hello")

# default_format = "%Y-%m-%d"
ist_time = datetime.now()
print("LOCAL   time: ", ist_time)
utc_time = datetime.now(timezone.utc)
print("GMT/UTC time: ", utc_time)
current_date = utc_time.replace(tzinfo=timezone.utc)
# print(current_date)
current_month = int(current_date.strftime("%m"))
current_year = int(current_date.strftime("%Y"))
input_year = 2025
input_month = 9
birth_day_ = 8
# days_in_month = calendar.monthrange(current_year, current_month)[1]
days_in_month = calendar.monthrange(input_year, input_month)[1]
print(days_in_month)
sum_ = 0


def get_days_of_searched_conduct_number(days, month, year, conduct_num=7):
    deduced_year = deduce_sum(int(year))
    deduced_month = deduce_sum(int(month))
    result_days = list()
    for i in range(days):
        day = i + 1
        deduced_day = deduce_sum(day)
        sum_ = deduce_sum(int(deduced_day + deduced_month + deduced_year))
        if conduct_num == sum_ and sum_ == 8:
            result_days.append(day)
        elif conduct_num == sum_ and sum_ == 7:
            result_days.append(day)
        elif conduct_num == sum_ and sum_ == 6:
            result_days.append(day)
        elif conduct_num == sum_ and sum_ == 5:
            result_days.append(day)
        elif conduct_num == sum_ and sum_ == 4:
            result_days.append(day)
        elif conduct_num == sum_ and sum_ == 3:
            result_days.append(day)
        elif conduct_num == sum_ and sum_ == 2:
            result_days.append(day)
        elif conduct_num == sum_ and sum_ == 1:
            result_days.append(day)

    print("Days in month no -> %d in year -> %d has conduct number %s : " % (month, year, conduct_num), result_days)
    return result_days


def get_days_of_searched_driver_number(days, month, year, driver_num=8):
    result_days = list()
    for i in range(days):
        day = i + 1
        deduced_day = deduce_sum(day)
        sum_ = deduce_sum(int(deduced_day))
        if driver_num == sum_ and sum_ == 8:
            result_days.append(day)
        elif driver_num == sum_ and sum_ == 7:
            result_days.append(day)
        elif driver_num == sum_ and sum_ == 6:
            result_days.append(day)
        elif driver_num == sum_ and sum_ == 5:
            result_days.append(day)
        elif driver_num == sum_ and sum_ == 4:
            result_days.append(day)
        elif driver_num == sum_ and sum_ == 3:
            result_days.append(day)
        elif driver_num == sum_ and sum_ == 2:
            result_days.append(day)
        elif driver_num == sum_ and sum_ == 1:
            result_days.append(day)

    print("Days in month no -> %d in year -> %d has driver number %s : " % (month, year, driver_num), result_days)
    return result_days


def find_conduct_number_by_birthday(birthday, days, month, year):
    deduced_year = deduce_sum(int(year))
    deduced_month = deduce_sum(int(month))
    for i in range(days):
        day = i + 1
        deduced_day = deduce_sum(day)
        sum__ = deduce_sum(int(deduced_day + deduced_month + deduced_year))
        if int(birthday) == day:
            print("Conduct number of a person who is born on %d no. day of %d no. month in the year %d. " % (birthday,
                                                                                                             month,
                                                                                                             year),
                  sum__)
            return sum__


def find_driver_number_by_birthday(birthday, days, month, year):
    for i in range(days):
        day = i + 1
        deduced_day = deduce_sum(day)
        sum__ = deduce_sum(int(deduced_day))
        if int(birthday) == day:
            print("Driver number of a person who is born on %d no. day of %d no. month in the year %d. " % (birthday,
                                                                                                            month,
                                                                                                            year),
                  sum__)
            return sum__


def deduce_sum(inp_int):
    i = int(inp_int)
    str_i = str(i)
    len_i = len(str_i)
    nums = list()
    sum_ = 0
    for j in range(len_i):
        nums.append(str_i[j])
        sum_ += int(str_i[j])
    len_sum_ = len(str(sum_))
    if len_sum_ == 1:
        return sum_
    else:
        return deduce_sum(sum_)


# print(deduce_sum(1993))

# print(get_days_of_searched_conduct_number(days_in_month, input_month, input_year))
# print(get_days_of_searched_driver_number(days_in_month, input_month, input_year))
print(find_conduct_number_by_birthday(birth_day_, days_in_month, input_month, input_year))
print(find_driver_number_by_birthday(birth_day_, days_in_month, input_month, input_year))

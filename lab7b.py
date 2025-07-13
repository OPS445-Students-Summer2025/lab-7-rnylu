#!/usr/bin/env python3
# Student ID: rlu22
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second


    """These find the quotient and remainder from minute/second values that are 
    60 or over. The quotient returned from divmod are added to the respective hour/minute
    sum and the remainder is set as their respective minute/second sum."""
    
    if sum.second >= 60:
        add_minute, second = divmod(sum.second, 60)
        sum.minute += add_minute
        sum.second = second

    if sum.minute >= 60:
        add_hour, minute = divmod(sum.minute, 60)
        sum.hour += add_hour
        sum.minute = minute

    return sum

def change_time(time, seconds):
    time.second += seconds
    if valid_time(time) != True:
        while time.second >= 60:
            time.second -= 60
            time.minute +=1
        while time.minute >= 60:
            time.minute -= 60
            time.hour += 1

        while time.second < 0: # borrow a minute when seconds < 0
            time.second += 60 
            time.minute -= 1 
            
        while time.minute < 0: # borrow an hour when minutes < 0
            time.minute += 60
            time.hour -= 1

    return None

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

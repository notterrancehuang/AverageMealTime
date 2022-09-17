from my_time import MyTime


def test():
    time_string1 = "10:30 PM"
    time1 = MyTime.parse(time_string1)
    time_string2 = "17:59"
    time2 = MyTime.parse(time_string2)
    print(time1)
    print(time2)

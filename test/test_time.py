from my_time import MyTime


def test():
    time_string1 = "12:30 am"
    time1 = MyTime.parse(time_string1)
    print(time1)

    time_string2 = "8:07 pm"
    time2 = MyTime.parse(time_string2)
    print(time2)

    diff = time1.time_diff(time2)
    print(diff)

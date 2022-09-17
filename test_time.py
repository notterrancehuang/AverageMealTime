from my_time import MyTime


def test():
    time_string1 = "11:59 am"
    time1 = MyTime.convert_to_military(time_string1)
    print(time1)

from my_time import MyTime


def test():
    start_str1 = "9:25"
    end_str1 = "10:30"
    start1 = MyTime.parse(start_str1)
    end1 = MyTime.parse(end_str1)
    diff1 = start1.time_diff(end1)
    print(f"Difference between {str(start1)} and {str(end1)} is {str(diff1)}")

    start_str2 = "09:25"
    end_str2 = "10:20"
    start2 = MyTime.parse(start_str2)
    end2 = MyTime.parse(end_str2)
    diff2 = start2.time_diff(end2)
    print(f"Difference between {str(start2)} and {str(end2)} is {str(diff2)}")

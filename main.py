from my_time import MyTime


def main():
    start_str = "9:25"
    end_str = "10:30"
    start = MyTime.parse(start_str)
    end = MyTime.parse(end_str)
    diff = start.time_diff(end)
    print("Difference between " + str(start) + " and " + str(end))
    print(diff)


if __name__ == "__main__":
    main()

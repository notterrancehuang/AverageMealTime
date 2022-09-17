from my_time import MyTime

class Input:
    @classmethod
    def get_start_time(cls):
        time_string = input("Enter the start time: ")
        time = MyTime.parse(time_string)

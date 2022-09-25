class MyTime:
    """
    A class representing time
    """

    """
    hour: int. hours in military time (24 hours)
    minute: int. the minutes
    return: time object representing the difference between the two times
    """
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    """
    Convert from standard time to military time
    time_string: string with the time and am/pm. 
    return: a new military time time object 
    """
    @classmethod
    def convert_to_military(cls, time_string: str) -> "MyTime":
        time_list = time_string.split(" ")
        hour, minute = time_list[0].split(":")
        if time_list[1].lower() == "pm":
            new_hour = int(hour) + 12
            new_minute = int(minute)
        elif time_list[1].lower() == "am" and hour == "12":
            new_hour = 0
            new_minute = int(minute)
        else:
            new_hour = int(hour)
            new_minute = int(minute)
        return MyTime(new_hour, new_minute)

    """
    Parse a time string and turn into a time object. For example, 05:00
    time_string: a string. 
    return: my_time. a time object
    """
    @classmethod
    def parse(cls, time_string: str) -> "MyTime":
        if MyTime.is_standard_time(time_string):
            return MyTime.convert_to_military(time_string)
        hour_str, minute_str = time_string.split(":")
        hour = int(hour_str)
        minute = int(minute_str)
        return MyTime(hour, minute)

    """
     Check whether the time string is in standard time mode.
     time_string: a string that the user inputs
     return: whether the time is in standard time mode. 
    """
    @classmethod
    def is_standard_time(cls, time_string: str) -> bool:
        time_list = time_string.split(" ")
        return len(time_list) == 2

    """
    Compares the time between this and the end time
    end: the end time of eating the meal
    return: a time object of the difference between the end and start time. 
    """
    def time_diff(self, end: "MyTime") -> "MyTime":
        minute_diff = end.minute - self.minute
        if minute_diff < 0:
            new_minute = 60 + minute_diff
            end.hour -= 1
            new_hour = end.hour - self.hour
        else:
            hour_diff = end.hour - self.hour
            new_minute = minute_diff
            new_hour = hour_diff

        return MyTime(new_hour, new_minute)

    """
    Overriding the toString and giving a string representation of the time 
    object. 
    return: a string representation of the time object. 
    """
    def __str__(self):
        return f"{self.hour:02}" + ":" + f"{self.minute :02}"

class MyTime:
    """
    hour: int. hours in military time (24 hours)
    minute: int. the minutes
    return: time object representing the difference between the two times
    """
    # hours are in military time (24 hours)
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def convert_to_military(cls, time_string: str) -> "MyTime":
        time_list = time_string.split(" ")
        hour, minute = time_list[0].split(":")
        if time_list[1].lower() == "pm":
            new_hour = int(hour) + 12
            new_minute = int(minute)
        else:
            new_hour = int(hour)
            new_minute = int(minute)
        return MyTime(new_hour, new_minute)


    @classmethod
    def parse(cls, time_string: str) -> "MyTime":
        hour_str, minute_str = time_string.split(":")
        hour = int(hour_str)
        minute = int(minute_str)
        return MyTime(hour, minute)

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

    def __str__(self):
        return f"{self.hour:02}" + ":" + f"{self.minute :02}"

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
    def parse(cls, time_string: str) -> "MyTime":
        hour_str, minute_str = time_string.split(":")
        hour = int(hour_str)
        minute = int(minute_str)
        return MyTime(hour, minute)

    def time_diff(self, end: "MyTime") -> "MyTime":
        new_minute = None
        new_hour = None
        minute_diff = end.minute - self.minute
        hour_diff = end.hour - self.hour
        if minute_diff < 0:
            new_minute = 60 + minute_diff
            self.hour -= 1
            new_hour = hour_diff
        else:
            new_minute = minute_diff
            new_hour = hour_diff

        return MyTime(new_hour, new_minute)

    def __str__(self):
        # TODO 0 filling
        return str(self.hour) + ":" + str(self.minute)

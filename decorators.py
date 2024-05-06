def validate_stat_input(func):
    def wrapper(self, *args, **kwargs):
        stat_name, value = args
        while value < 0 or value > 20:
            print("Invalid value. Stat values must be between 0 and 20.")
            value = int(input("Enter the new value for {}: ".format(stat_name)))
        return func(self, stat_name, value)
    return wrapper


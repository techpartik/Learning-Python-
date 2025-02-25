import datetime

class Day:
    def __init__(self, date, day, module):
        self.date = date
        self.day = day
        self.module = module

    def n_d(self):
        # Calculate the day of the year for the given date
        day_of_year = self.date.strftime('%j')
        print(f"Day of the year: {day_of_year}")

# Example usage
# Convert input strings to datetime objects
d1 = datetime.datetime.strptime("20250221", "%Y%m%d")
d2 = datetime.datetime.strptime("20250321", "%Y%m%d")
k = datetime.datetime.now()

# Create an instance of the Day class
ob = Day(d1, d2, k)

# Call the n_d method to print the day of the year
ob.n_d()

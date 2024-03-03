# Author Jennifer Ibanez Cano
# This program will print out the summer months one at a time.

# First I'll create a tuple that stores the months of the year. 

months =("January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
)
# Then I'll create another tuple with just the summer months.
summer = months[4:7]
for months in summer:
    print(months)

# The program will print the months: May, June and July
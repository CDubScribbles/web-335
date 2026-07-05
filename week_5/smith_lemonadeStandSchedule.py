"""
Author: Cliff Smith
Date: July 4, 2026
File Name: smith_lemonadeStandSchedule.py
Description: This program manages a weekly schedule for a lemonade stand.
It uses a list of tasks and a list of days, then loops through the days
to display either the task for that day or a day-off message for weekends.
"""

# Defining a list of tasks related to running a lemonade stand
tasks = ["Buy lemons", "Make lemonade", "Sell lemonade", "Count earnings", "Clean up"]

# Using a for loop to iterate over the list of tasks and print them
print("Weekly Lemonade Stand Tasks:")
for task in tasks:
    print(task)

# Defining a list of days, Sunday through Saturday
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Using a for loop with the range/len pattern to walk through the days list
# A separate counter (task_index) only increases on weekdays, since there
# are 7 days but only 5 tasks - this keeps the two lists lined up correctly
print("\nWeekly Schedule:")
task_index = 0
for i in range(len(days)):
    # Check if the current day is Saturday or Sunday
    if days[i] in ["Saturday", "Sunday"]:
        print(days[i] + ": Day off - go rest!")
    else:
        # For weekdays, print the day and its matching task, then move
        # the task counter forward by one
        print(days[i] + ": " + tasks[task_index])
        task_index = task_index + 1
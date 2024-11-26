import datetime

def generate_first_days():
    year = 2024
    dates = []

    for month in range(1, 13): # 1-12. month
        date = datetime.date(year, month, 1).strftime("%d/%m/%Y") # 1st day of each month in format dd/mm/yyyy
        dates.append(date) # append date to list
    return dates

with open("03_dates.txt", "w") as file:
    for date in generate_first_days():
        file.write(date + "\n") # write to file

with open("03_dates.txt", "r") as file:
    print(file.read()) # print content of file for check


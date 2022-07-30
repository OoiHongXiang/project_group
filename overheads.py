from pathlib import Path
import csv

def overheads():
    file_path = Path.cwd()/"csv_reports"/"overheads-day-45.csv"

    empty_list = []

    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            empty_list.append(line)

    empty_list.pop(0)

    percentage_list = []

    for sublist in empty_list:
        percentage = float(sublist[1])
        percentage_list.append(percentage)

    highest_percentage = max(percentage_list)    
    index = percentage_list.index(highest_percentage)
    highest_category = empty_list[index][0]
    
    return[highest_category, highest_percentage]

print(overheads())
from pathlib import Path 
import csv 
 
def cash_on_hand(): 
    file_path = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv" 
 
    empty_list = [] 
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file: 
        reader = csv.reader(file) 
        for line in reader: 
            empty_list.append(line) 
 
    empty_list.pop(0) 
 
    write_data = [] 
 
    for index, sublist in enumerate(empty_list): 
        current_day = float(sublist[1]) 
        if index == 0: 
            previous_day = 0 
        else: 
            previous_day = float(empty_list[index - 1][1]) 
 
        if current_day < previous_day: 
            day = int(sublist[0]) 
            cash_deficit = previous_day - current_day 
            write_data.append(day) 
            write_data.append(cash_deficit) 
            return(write_data) 
 
print(cash_on_hand())
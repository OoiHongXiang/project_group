from pathlib import Path
import csv

def overheads():
    """
    This function finds the highest overhead category and its value.
    """ 
    
    file_path = Path.cwd()/"csv_reports"/"overheads-day-45.csv"
    # file path to csv file containing overheads data is assigned to file_path variable
    
    empty_list = [] # creates empty list to store data when reading csv file 
    
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    # opens csv file and assigns to file variable
        reader = csv.reader(file)
        for index, line in enumerate(reader):
            if index > 0:
                empty_list.append(line)
        # every line, except the headers (index = 0), in the csv file is appended to the empty list
    
    percentage_list = [] # creates empty list to store the percentages of each category for comparison

    for sublist in empty_list:
        percentage = float(sublist[1])
        percentage_list.append(percentage)
    # percentages of each category is appended to percentage_list

    highest_percentage = max(percentage_list) # finds the highest percentage    
    index = percentage_list.index(highest_percentage) # finds the index of the highest percentage
    highest_category = empty_list[index][0] # finds the category with highest percentage using the index
    
    return[highest_category, highest_percentage]
    # returns category with the highest percentage as a list

print(overheads())
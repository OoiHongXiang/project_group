from pathlib import Path 
import csv 
 
def profit_loss():
    """
    This function highlights the days where there is a net profit deficit and computes the difference in amount. Data is extracted into a list.
    """ 
    
    file_path = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv" 
    # file path to csv file containing net profit data is assigned to file_path variable
    
    empty_list = [] # creates empty list to store data when reading csv file 
    
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file: 
    # opens csv file and assigns to file variable
        reader = csv.reader(file) 
        for index, line in enumerate(reader): 
            if index > 0:
                empty_list.append(line) 
        # every line, except the headers (index = 0), in the csv file is appended to the empty list
 
    data_list = [] # creates empty list to store highlighted days with deficit
 
    for index, sublist in enumerate(empty_list): 
        current_day = float(sublist[4]) # assigns net profit on current day to current_day variable
        if index > 0: 
            previous_day = float(empty_list[index - 1][4]) 
        # every day, except for the first day (index = 0), will have a previous_day variable for comparison (first day does not have a previous day to compare to)
            if current_day < previous_day: 
                day = int(sublist[0]) 
                difference = previous_day - current_day # computes difference in net profit
                data_list.append([day, difference]) 
            # if there is a profit deficit, each day and the difference in amount is appended to data_list as its own individual sublist
    return(data_list) 
    # returns the highlighted days where there is profit deficit and the difference
 
print(profit_loss())
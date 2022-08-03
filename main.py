import api, cash_on_hand, profit_loss, overheads
from pathlib import Path

def main():
    """
    This function imports, coordinates and executes functions from each python file to write a summary report of the business performance in text file.
    """

    file_path = Path.cwd()/"summary_report.txt"
    # file path to .txt file for writing is assigned to file_path variable

    write_list = [] # creates empty list to contain data, in proper format, to be written
    
    rate = api.api() # assigns currency exchange rate from api() to rate variable
    write_list.append(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{rate}")
    # appends string, in proper format, to write_list

    highest_overhead = overheads.overheads() 
    # assigns list from overheads(), containing highest category and its percentage, to highest_overhead variable
    write_list.append(f"\n[HIGHEST OVERHEADS] {highest_overhead[0]}: {highest_overhead[1]}")
    # appends highest category and its amount to write_list

    cash_deficit = cash_on_hand.cash_on_hand()
    # assigns list from cash_on_hand(), containing highlighted days with cash deficit, to cash_deficit variable
    if cash_deficit == []:
        write_list.append(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    # if there are no highlighted days, string stating a daily cash surplus is appended to write_list
    else:
        for sublist in cash_deficit:    
            write_list.append(f"\n[CASH DEFICIT] DAY: {sublist[0]}, AMOUNT: SGD{sublist[1] * rate}")
    # if there are highlighted days, each day and difference (converted to SGD using rate) is appended to write_list

    profit_deficit = profit_loss.profit_loss()
    # assigns list from profit_loss(), containing highlighted days with profit deficit, to profit_deficit variable
    if profit_deficit == []:
        write_list.append(f"\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    # if there are no highlighted days, string stating a daily profit surplus is appended to write_list
    else:
        for sublist in profit_deficit:    
            write_list.append(f"\n[PROFIT DEFICIT] DAY: {sublist[0]}, AMOUNT: SGD{sublist[1] * rate}")
    # if there are highlighted days, each day and difference (converted to SGD using rate) is appended to write_list

    print(write_list) # prints list containing the texts to be written

    with file_path.open(mode="w") as file:
    # opens summary_report.txt file for writing and assigns to file variable
        file.writelines(write_list)
        # contents of write_list is written to summary_report.txt

print(main())
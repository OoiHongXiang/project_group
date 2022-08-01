import api, cash_on_hand, profit_loss, overheads 
from pathlib import Path 
 
def main(): 
    rate = api.api() 
    highest_overhead = overheads.overheads() 
    cash_deficit = cash_on_hand.cash_on_hand() 
    profit_deficit = profit_loss.profit_loss() 
 
    file_path = Path.cwd()/"summary_report.txt" 
    write_list = [ 
        f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{rate}", 
        f"\n[HIGHEST OVERHEADS] {highest_overhead[0]}: {highest_overhead[1]}", 
        f"\n[CASH DEFICIT] DAY: {cash_deficit[0]}, AMOUNT: SGD{cash_deficit[1] * rate}", 
        f"\n[PROFIT DEFICIT] DAY: {profit_deficit[0]}, AMOUNT: SGD{profit_deficit[1] * rate}", 
        f"\n[PROFIT DEFICIT] DAY: {profit_deficit[2]}, AMOUNT: SGD{profit_deficit[3] * rate}", 
        f"\n[PROFIT DEFICIT] DAY: {profit_deficit[4]}, AMOUNT: SGD{profit_deficit[5] * rate}", 
        ] 
 
    with file_path.open(mode="w") as file: 
        file.writelines(write_list) 
 
print(main())

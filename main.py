import api, cash_on_hand, profit_loss, overheads
from pathlib import Path

def main():
    file_path = Path.cwd()/"summary_report.txt"
    write_list = []
    
    rate = api.api()
    write_list.append(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{rate}")
    
    highest_overhead = overheads.overheads()
    write_list.append(f"\n[HIGHEST OVERHEADS] {highest_overhead[0]}: {highest_overhead[1]}")
    
    cash_deficit = cash_on_hand.cash_on_hand()
    if cash_deficit == []:
        write_list.append(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    else:
        for sublist in cash_deficit:    
            write_list.append(f"\n[CASH DEFICIT] DAY: {sublist[0]}, AMOUNT: SGD{sublist[1] * rate}")
    
    profit_deficit = profit_loss.profit_loss()
    if profit_deficit == []:
        write_list.append(f"\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    else:
        for sublist in profit_deficit:    
            write_list.append(f"\n[PROFIT DEFICIT] DAY: {sublist[0]}, AMOUNT: SGD{sublist[1] * rate}")

    with file_path.open(mode="w") as file:
        file.writelines(write_list)
    
    print(write_list)

print(main())
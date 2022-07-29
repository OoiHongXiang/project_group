from pathlib import Path
import api, overheads

def main():
    rate = api.api()

    file_path = Path.cwd()/"summary_report.txt"
    with file_path.open(mode="w", encoding="UTF-8", newline="") as file:
        file.writeline(rate)

print(main())
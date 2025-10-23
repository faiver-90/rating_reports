import datetime
from pathlib import Path

from script.io import save_csv_files


def build_final_table(rows, report_headers):
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    save_csv_files(Path(f'reports/{now}/report.csv'),rows, headers=report_headers)

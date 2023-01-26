import yaml
import csv

all_records = []
with open('DATA/city-of-chicago-salaries.csv') as chi_in:
    headers = next(chi_in)  # consume header row
    # print(f"headers: {headers}")
    rdr = csv.reader(chi_in)
    for i, (name, position, dept, salary) in enumerate(rdr):
        all_records.append(
            {
                'name': name.title(),
                'position': position,
                'department': dept,
                'salary': float(salary.lstrip('$'))
            }
        )

with open('chicago_employees.yml', 'w') as chi_out:
    yaml.dump(all_records, chi_out)
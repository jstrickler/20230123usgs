import lxml.etree as et
import csv

root = et.Element('employees')

# Name,Position Title,Department,Employee Annual Salary

with open('DATA/city-of-chicago-salaries.csv') as chi_in:
    headers = next(chi_in)  # consume header row    
    # print(f"headers: {headers}")
    rdr = csv.reader(chi_in)
    for i, (name, position, dept, salary) in enumerate(rdr):
        employee = et.SubElement(root, 'employee', department=dept)
        pos_title = et.SubElement(employee, 'position')
        pos_title.text = position
        et.SubElement(employee, 'salary').text = salary.lstrip('$')
        if i == 30:
            break

print(et.tostring(root, pretty_print=True, xml_declaration=True).decode())

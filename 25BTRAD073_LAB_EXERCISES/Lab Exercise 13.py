import csv
import os

INPUT_FILE = "employees.csv"
OUTPUT_FILE = "payroll_summary.csv"

sample_employees = [
    ["EmpID", "Name", "Department", "BasicSalary", "Bonus"],
    ["E101", "Rohan Verma", "Engineering", "60000", "5000"],
    ["E102", "Priya Nair", "Marketing", "45000", "3000"],
    ["E103", "Amit Patel", "HR", "40000", "2000"],
    ["E104", "Sneha Rao", "Engineering", "75000", "8000"],
    ["E105", "Invalid User", "Sales", "-5000", "1000"]
]

with open(INPUT_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sample_employees)


def process_payroll():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: '{INPUT_FILE}' not found.")
        return

    processed_records = []
    total_company_gross = 0.0
    total_company_net = 0.0

    with open(INPUT_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            emp_id = row["EmpID"]
            name = row["Name"]
            dept = row["Department"]

            try:
                basic = float(row["BasicSalary"])
                bonus = float(row["Bonus"])
                if basic <= 0 or bonus < 0:
                    raise ValueError("Negative or zero base salary")
            except ValueError as e:
                print(f"Skipping invalid record for {emp_id} ({name}): {e}")
                continue

            hra = basic * 0.20
            gross_salary = basic + hra + bonus

            pf_deduction = basic * 0.12
            tax_deduction = gross_salary * 0.10
            total_deductions = pf_deduction + tax_deduction

            net_salary = gross_salary - total_deductions

            assert round(net_salary + total_deductions, 2) == round(gross_salary, 2), (
                "Math mismatch!"
            )

            total_company_gross += gross_salary
            total_company_net += net_salary

            processed_records.append({
                "EmpID": emp_id,
                "Name": name,
                "Department": dept,
                "GrossSalary": round(gross_salary, 2),
                "Deductions": round(total_deductions, 2),
                "NetSalary": round(net_salary, 2)
            })

    fieldnames = [
        "EmpID", "Name", "Department", "GrossSalary", "Deductions", "NetSalary"
    ]
    with open(OUTPUT_FILE, "w", newline="") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_records)

    print("\n--- Monthly Payroll Summary ---")
    print(
        f"{'ID':<6} {'Name':<15} {'Dept':<12} {'Gross':>10} "
        f"{'Deductions':>12} {'Net Pay':>10}"
    )
    print("-" * 70)
    for emp in processed_records:
        print(
            f"{emp['EmpID']:<6} {emp['Name']:<15} {emp['Department']:<12} "
            f"{emp['GrossSalary']:>10.2f} {emp['Deductions']:>12.2f} "
            f"{emp['NetSalary']:>10.2f}"
        )

    print("-" * 70)
    print(f"Total Valid Employees Processed : {len(processed_records)}")
    print(f"Total Company Gross Expense : ₹{total_company_gross:,.2f}")
    print(f"Total Net Disbursed to Staff : ₹{total_company_net:,.2f}")
    print(
        f"Total Tax & PF Withheld : ₹{(total_company_gross - total_company_net):,.2f}"
    )
    print(f"\nDetailed report saved to '{OUTPUT_FILE}'.")


process_payroll()

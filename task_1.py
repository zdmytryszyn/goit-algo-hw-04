def total_salary(path: str) -> tuple | str:
    try:
        with open(path, "r", encoding="utf-8") as salary_file:
            employee_list = [
                line.strip().split(",") for line in salary_file.readlines()
            ]
            total_wage = sum(float(employee[1]) for employee in employee_list)
            average_salary = total_wage / len(employee_list)
            return total_wage, average_salary
    except FileNotFoundError:
        return f"No such file: '{path}', provide a valid path to file"
    except IOError:
        return f"File '{path}' may be corrupted, cannot be opened"

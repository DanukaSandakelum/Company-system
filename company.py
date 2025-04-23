class Person:
    def __init__(self, name, nic, age):
        self.name = name
        self.nic = nic
        self.age = age


class Student(Person):
    def __init__(self, name, nic, age, gpa1, gpa2, gpa3, gpa4):
        super().__init__(name, nic, age)
        self.gpa1 = gpa1
        self.gpa2 = gpa2
        self.gpa3 = gpa3
        self.gpa4 = gpa4
        self.final_gpa = 0.0

    def calculate_gpa(self):
        self.final_gpa = (self.gpa1 + self.gpa2 + self.gpa3 + self.gpa4) / 4
        return self.final_gpa

    def final_result(self):
        if self.final_gpa > 3.70:
            return "First Class"
        elif self.final_gpa > 3.30:
            return "Second Class (Upper)"
        elif self.final_gpa > 3.00:
            return "Second Class (Lower)"
        else:
            return "Pass"


class StaffMember(Person):
    COLA = 7800.00  # Cost of Living Allowance

    def __init__(self, name, nic, age, basic_salary, loan_installment):
        super().__init__(name, nic, age)
        self.basic_salary = basic_salary
        self.loan_installment = loan_installment

    def get_salary(self):
        raise NotImplementedError("Subclasses must implement this method")


class AcademicStaff(StaffMember):
    ACADEMIC_ALLOWANCE = 25  # in percent

    def __init__(self, name, nic, age, basic_salary, loan_installment):
        super().__init__(name, nic, age, basic_salary, loan_installment)

    def get_salary(self):
        allowance = (self.basic_salary * self.ACADEMIC_ALLOWANCE) / 100
        return self.basic_salary + self.COLA + allowance - self.loan_installment


class NonAcademicStaff(StaffMember):
    def __init__(self, name, nic, age, basic_salary, loan_installment, overtime_hours):
        super().__init__(name, nic, age, basic_salary, loan_installment)
        self.overtime_hours = overtime_hours

    def overtime_amount(self):
        return (self.basic_salary / (20 * 8)) * self.overtime_hours

    def get_salary(self):
        return self.basic_salary + self.COLA + self.overtime_amount() - self.loan_installment


# Handling logic
def handle_student():
    print("\nEnter Student Details:")
    name = input("Name: ")
    nic = input("NIC: ")
    age = int(input("Age: "))
    gpas = [float(input(f"GPA {i+1}: ")) for i in range(4)]

    student = Student(name, nic, age, *gpas)
    student.calculate_gpa()
    print(f"\nFinal GPA: {student.final_gpa:.2f}")
    print("Result:", student.final_result())


def handle_staff():
    staff_type = input("\nStaff Type (1. Academic / 2. Non-Academic): ").strip()
    name = input("Name: ")
    nic = input("NIC: ")
    age = int(input("Age: "))
    basic_salary = float(input("Basic Salary: "))
    loan_installment = float(input("Loan Installment: "))

    if staff_type == "1":
        staff = AcademicStaff(name, nic, age, basic_salary, loan_installment)
    elif staff_type == "2":
        overtime = float(input("Overtime Hours: "))
        staff = NonAcademicStaff(name, nic, age, basic_salary, loan_installment, overtime)
    else:
        print("Invalid staff type!")
        return

    print(f"\nSalary: {staff.get_salary():.2f}")


def main():
    while True:
        print("\n===== Main Menu =====")
        print("1. Student Operations")
        print("2. Staff Operations")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            handle_student()
        elif choice == "2":
            handle_staff()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

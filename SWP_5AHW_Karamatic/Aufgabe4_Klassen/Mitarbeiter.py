class Company:
    def __init__(self, compName):
        self.compName = compName
        self.departments = []  # Eine Liste von Department-Objekten

    def add_department(self, department):
        self.departments.append(department)

    def __str__(self):
        return f"{self.compName}-Abteilungen: {self.departments}"

class Department:
    def __init__(self, depName):
        self.depName = depName
        self.employees = []  # Eine Liste von Employee-Objekten

    def add_employee(self, employee): #Hilfe
       self.employees.append(employee) #

    def __str__(self):
        return f" {self.depName}-Mitarbeiter: {self.employees}"

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return self.name + " " + format(self.gender)

class Employee(Person):
    def __init__(self, name, gender, isDepHead):
        super().__init__(name, gender)
        self.isDepHead = isDepHead

    def __str__(self):
        return self.name + " " + format(self.gender) + " " + format(self.isDepHead)

def countWorkers(department):
    print(f"Untersch. Arbeiter in {department.depName}: {len(department.employees)}")

def countDepartments(company):
    print(f"Untersch. Abteilungen in {company.compName}: {len(company.departments)}")

def countDepHeads(department):
    c = 0
    for emp in department.employees:
        if emp.isDepHead:
            c += 1
    print(f"Anzahl Abt.leiter in {department.depName}: {c}")

def defineLargestDep(company):
    depa = max(company.departments, key=lambda dep: len(dep.employees))
    print(f"Grösste Abteilung: {depa.depName}")

#def countGender(company): #idfk if this shit works
#    a = 0
#    m = 0
#    for department in company.departments:
#        a += len(department.employees)
#    for department in company.departments:
#        m += len(department.employees)

#    g = ((a-m)/a)*100
#    print(m)


def main():
    pon1 = Person("Julian", True)
    pon2 = Person("Juliana", False)

    eee1 = Employee("Sebastian", True, True)
    eee2 = Employee("Martin", Kücken, True)
    eee3 = Employee("David", True, False)
    eee4 = Employee("Jakob", True, True)
    eee5 = Employee("Eva", False, False)
    eee6 = Employee("Sandra", False, True)
    eee7 = Employee("Gabriel", True, False)
    eee8 = Employee("Manuel", True, False)

    dep1 = Department("IT")
    Department.add_employee(dep1, eee1)
    Department.add_employee(dep1, eee2)
    Department.add_employee(dep1, eee3)
    dep2 = Department("RnD")
    Department.add_employee(dep2, eee4)
    Department.add_employee(dep2, eee5)
    dep3 = Department("Finance")
    Department.add_employee(dep3, eee6)
    Department.add_employee(dep3, eee7)

    comp1 = Company("Alles wird gut GmbH")
    Company.add_department(comp1, dep1)
    Company.add_department(comp1, dep2)
    Company.add_department(comp1, dep3)

    countDepartments(comp1)

    countWorkers(dep1)
    countDepHeads(dep1)

    countWorkers(dep2)
    countWorkers(dep3)

    defineLargestDep(comp1)

    # countGender(comp1)


if __name__ == '__main__':
    try:
        main()

    except NameError: #NameError: name 'Kücken' is not defined
        print("\nSo nicht min' jung'!\n \___\n//  \\\n get stickbugged")

    finally:
        print("\nAlles Roger in Kambodscha")


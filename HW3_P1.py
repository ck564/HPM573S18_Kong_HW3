# HW 3 Problem 1

class Patient:
    """base class"""
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError ("This is an abstract method and needs to be implemented in derived classes.")

class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.expected_cost = ED_cost

    def discharge(self):
        print("Discharged:", self.name, ", ED")

class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.expected_cost = hospitalized_cost

    def discharge(self):
        print("Discharged:", self.name, ", Hospitalized")


class Hospital:
    def __init__(self):
        self.patients = []
        self.costs = 0

    def admit(self, Patient):
        self.patients.append(Patient)

    def discharge_all(self):
        for Patient in self.patients:
            Patient.discharge()
            self.costs += Patient.expected_cost

    def get_total_cost(self):
        return self.costs

# Hospital patient costs
ED_cost = 1000
hospitalized_cost = 2000

# Patients
P1 = EmergencyPatient("Sally")
P2 = EmergencyPatient("John")
P3 = EmergencyPatient("Wayne")
P4 = HospitalizedPatient("Claire")
P5 = HospitalizedPatient("Everleigh")

# Admitting patients
Hospital1 = Hospital()

Hospital1.admit(P1)
Hospital1.admit(P2)
Hospital1.admit(P3)
Hospital1.admit(P4)
Hospital1.admit(P5)

# Discharging patients
Hospital1.discharge_all()

# Calculating total cost
print("Total operating cost: $", Hospital1.get_total_cost())




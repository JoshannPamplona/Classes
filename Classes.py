class Doctor:
    def __init__(self, id, name, specialization, working_time, qualification, room_number):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def display_info(self):
        print(f"Doctor ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Working Time: {self.working_time}")
        print(f"Qualification: {self.qualification}")
        print(f"Room Number: {self.room_number}")
        print("=" * 30)

class Facility:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Facility Name: {self.name}")
        print("=" * 30)

class Laboratory:
    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def display_info(self):
        print(f"Laboratory Name: {self.lab_name}")
        print(f"Cost: ${self.cost}")
        print("=" * 30)

class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def display_info(self):
        print(f"Patient ID: {self.pid}")
        print(f"Name: {self.name}")
        print(f"Disease: {self.disease}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print("=" * 30)

class HospitalManagementSystem:
    def __init__(self):
        self.doctors = []
        self.facilities = []
        self.laboratories = []
        self.patients = []

    def display_menu(self):
        print("Alberta Hospital (AH) Management System")
        print("1 - Manage Doctors")
        print("2 - Manage Facilities")
        print("3 - Manage Laboratories")
        print("4 - Manage Patients")
        print("0 - Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.manage_doctors()
            elif choice == '2':
                self.manage_facilities()
            elif choice == '3':
                self.manage_laboratories()
            elif choice == '4':
                self.manage_patients()
            elif choice == '0':
                print("Exiting Alberta Hospital (AH) Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def manage_doctors(self):
        while True:
            print("\nManage Doctors:")
            print("1 - Display Doctors")
            print("2 - Add Doctor")
            print("3 - Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_doctors()
            elif choice == '2':
                self.add_doctor()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def display_doctors(self):
        print("\nDoctors List:")
        for doctor in self.doctors:
            doctor.display_info()

    def add_doctor(self):
        id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")
        working_time = input("Enter Working Time: ")
        qualification = input("Enter Qualification: ")
        room_number = input("Enter Room Number: ")

        new_doctor = Doctor(id, name, specialization, working_time, qualification, room_number)
        self.doctors.append(new_doctor)
        print("Doctor added successfully!")

    def manage_facilities(self):
        while True:
            print("\nManage Facilities:")
            print("1 - Display Facilities")
            print("2 - Add Facility")
            print("3 - Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_facilities()
            elif choice == '2':
                self.add_facility()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def display_facilities(self):
        print("\nFacilities List:")
        for facility in self.facilities:
            facility.display_info()

    def add_facility(self):
        name = input("Enter Facility Name: ")
        new_facility = Facility(name)
        self.facilities.append(new_facility)
        print("Facility added successfully!")

    def manage_laboratories(self):
        while True:
            print("\nManage Laboratories:")
            print("1 - Display Laboratories")
            print("2 - Add Laboratory")
            print("3 - Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_laboratories()
            elif choice == '2':
                self.add_laboratory()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def display_laboratories(self):
        print("\nLaboratories List:")
        for lab in self.laboratories:
            lab.display_info()

    def add_laboratory(self):
        lab_name = input("Enter Laboratory Name: ")
        cost = input("Enter Cost: ")
        new_lab = Laboratory(lab_name, cost)
        self.laboratories.append(new_lab)
        print("Laboratory added successfully!")

    def manage_patients(self):
        while True:
            print("\nManage Patients:")
            print("1 - Display Patients")
            print("2 - Add Patient")
            print("3 - Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_patients()
            elif choice == '2':
                self.add_patient()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def display_patients(self):
        print("\nPatients List:")
        for patient in self.patients:
            patient.display_info()

    def add_patient(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter Disease: ")
        gender = input("Enter Gender: ")
        age = input("Enter Age: ")

        new_patient = Patient(pid, name, disease, gender, age)
        self.patients.append(new_patient)
        print("Patient added successfully!")

# Create an instance of the HospitalManagementSystem
ahms = HospitalManagementSystem()

# Populate initial data (you can add more here if needed)
ahms.doctors.append(Doctor("101", "Dr. Smith", "Cardiologist", "9 AM - 5 PM", "MD, PhD", "204"))
ahms.facilities.append(Facility("Emergency Room"))
ahms.laboratories.append(Laboratory("Lab A", "$100"))
ahms.patients.append(Patient("P001", "John Doe", "Fever", "Male", "30"))

# Run the Hospital Management System
ahms.run()

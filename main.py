from datetime import datetime as DateTime

class Person:
    '''class represents Person'''
    # Constructor to initialize the attributes for the class Person
    def __init__(self, firstname='', lastname='', date_of_birth=DateTime.now(), address='', phone_number=''):
        self.firstname = firstname  # public
        self.lastname = lastname   # public
        self._date_of_birth = date_of_birth  # protected
        self.__address = address   # private
        self.phone_number = phone_number  # public


    def age(self):
        '''calcualtes the age of the person'''
        pass


    def full_name(self):
        '''Return the full name of the person'''
        pass


    # A function allowing the change of the first name
    def set_firstname(self, firstname):
        self.firstname = firstname

    # A function to get the first name
    def get_firstname(self):
        return self.firstname

    # A function allowing the change of the last name
    def set_lastname(self, lastname):
        self.lastname = lastname

    # A function to get the last name
    def get_lastname(self):
        return self.lastname

    # A function allowing the change of the date_of_birth
    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    # A function to get the date_of_birth
    def get_date_of_birth(self):
        return self._date_of_birth

    # A function allowing the change of the address
    def set_address(self, address):
        self.__address = address

    # A function to get the address
    def get_address(self):
        return self.__address

    # A function allowing the change of the phone_number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    # A function to get the phone number
    def get_phone_number(self):
        return self.phone_number



class Employee(Person):
    '''clss represents Employee , inherits from Person'''
    # Constructor to initialize the attributes for the class Employee
    def __init__(self, firstname='', lastname='', date_of_birth=DateTime.now(), address='', phone_number='',
                 employee_id=0, date_hired=DateTime.now(), position='', department='', salary=0.0):

        # call the parent class
        super().__init__(firstname, lastname, date_of_birth, address, phone_number)

        # Constructor to initialize the attributes for the class Employee
        self.__employee_id = employee_id #Private
        self._date_hired = date_hired#Protected
        self.position = position# Public
        self._department = department# Protected
        self.__salary = salary# Private

    def years_of_service(self):
        '''output  the number of years working'''
        pass

    def annual_review(self):
        '''analyze employee performnace.'''
        pass



    #setter getter:
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def set_date_hired(self, date_hired):
        self._date_hired = date_hired

    def get_date_hired(self):
        return self._date_hired

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_department(self, department):
        self._department = department

    def get_department(self):
        return self._department

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary



class Doctor(Employee):
    '''clss represents Doctor , inherits from Employee'''

    def __init__(self, firstname='', lastname='', date_of_birth=DateTime.now(), address='', phone_number='',
                 employee_id=0, date_hired=DateTime.now(), position='', department='', salary=0.0, specialization='', year_of_experience=0, certification=None, clinic_room='', patient_list=None):
        # call the parent class
        super().__init__(firstname, lastname, date_of_birth, address, phone_number, employee_id, date_hired, position, department, salary)

        if certification is None:
            certification = []  # create list of certificate of class doctor

        if patient_list is None:
            patient_list = []  # create list of patient_list of class doctor

        self.patient_list = patient_list  # public
        self.lastname = lastname  # public
        self._address = address  # protected
        self.__employee_id = employee_id  # private
        self.position = position  # public
        self._specialization = specialization  # protected
        self._year_of_experience = year_of_experience  # protected
        self.certification = certification  # Public
        self._clinic_room = clinic_room  # protected

    def diagnose(self, patient):
        '''updates patient's current condition.'''
        pass

    def add_certification(self, certification):
        '''Add a new certification'''
        pass

    def assign_patient(self, patient):
        '''Assigning a new patient'''
        pass
    #setter getter

    def get_specialization(self):
        return self._specialization

    def set_specialization(self, specialization):
        self._specialization = specialization

    def get_year_of_experience(self):
        return self._year_of_experience

    def set_year_of_experience(self, years):
        self._year_of_experience = years

    def get_clinic_room(self):
        return self._clinic_room

    def set_clinic_room(self, room):
        self._clinic_room = room

    def get_address(self):
        return self._address

    def set_address(self, addr):
        self._address = addr


class Nurse(Employee):
    '''class represents Nurse, inherits from Employee'''

    def __init__(self, firstname='', lastname='', date_of_birth=DateTime.now(), address='', phone_number='',
                 employee_id=0, date_hired=DateTime.now(), position='', department='', salary=0.0, nurse_id=0,
                 shift='', qualification=None, assigned_patients=None):

        # calling parent
        super().__init__(firstname, lastname, date_of_birth, address, phone_number, employee_id, date_hired, position, department, salary)

        if qualification is None:
            qualification = []  # create list of qualification for the nurse

        if assigned_patients is None:
            assigned_patients = []  # create list of assigned_patients for the nurse

        self.nurse_id = nurse_id
        self._qualification = qualification
        self.__assigned_patients = assigned_patients
        self.shift = shift

    def manage_medication(self, patient, medication):
        '''manage  medication to a patient.'''
        pass

    def assign_shift(self, start_time, end_time):
        '''Assign a work shift'''
        pass


    #setter getter
    def get_qualification(self):
        return self._qualification

    def set_qualification(self, qualification):
        if qualification is None:
            qualification = []
        self._qualification = qualification

    def get_assigned_patients(self):
        return self.__assigned_patients

    def set_assigned_patients(self, patients):
        if patients is None:
            patients = []
        self.__assigned_patients = patients

    def get_shift(self):
        return self.shift

    def set_shift(self, shift):
        self.shift = shift

    def get_nurse_id(self):
        return self.nurse_id

    def set_nurse_id(self, nurse_id):
        self.nurse_id = nurse_id


class Patient(Person):
    '''clss represents Patient , inherits from Person'''

    def __init__(self, firstname='', lastname='', date_of_birth=DateTime.now(), address='', phone_number='',
                 patient_id='', date_admitted=DateTime.now(), medical_history=None, current_condition='',
                 assigned_doctor=None,patient_name=''):
        super().__init__(firstname, lastname, date_of_birth, address, phone_number)

        if medical_history is None:
            medical_history = []    # create list of Medical_history of class Patient

        self.__patient_id = patient_id
        self._date_admitted = date_admitted
        self._medical_history = medical_history
        self.current_condition = current_condition
        self._assigned_doctor = assigned_doctor
        self.patient_name=patient_name

    def admit(self, date):
        '''Admit the patient'''
        pass

    def discharge(self, date):
        '''Discharge the patient'''
        pass

    def update_medical_history(self, entry):
        '''update medical history.'''
        pass



#setter getter
    def get_patient_id(self):
        return self.__patient_id

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def get_date_admitted(self):
        return self._date_admitted

    def set_date_admitted(self, date_admitted):
        self._date_admitted = date_admitted

    def get_medical_history(self):
        return self._medical_history

    def set_medical_history(self, medical_history):
        if medical_history is None:
            medical_history = []
        self._medical_history = medical_history

    def get_current_condition(self):
        return self.current_condition

    def set_current_condition(self, current_condition):
        self.current_condition = current_condition

    def get_assigned_doctor(self):
        return self._assigned_doctor

    def set_assigned_doctor(self, doctor):
        self._assigned_doctor = doctor

    def get_patient_name(self):
        return self.patient_name

    def set_patient_name(self, patient_name):
        self.patient_name = patient_name


from enum  import Enum #using Enum module for the class ServiceTypes: i used it since it is useful for allowing us to define values from a finite list of choices


class ServiceType(Enum):
    '''class that represents servicetype'''
    # Initializing members of enum
    DOCTOR_CONSULTATION = 1
    NURSING_SERVICES = 2
    HOSPITAL_CHARGES = 3
    PHARMACY = 4
    ROOM_CHARGES = 5


class InsuranceCoverage(Enum):
    '''class that represents InsuranceCoverage'''
    # Initializing members of enum for insurance
    NONE = 0.0
    HALF = 0.5
    FULL = 1.0


class Service:
    '''class that represents service'''
    # constructor
    def __init__(self):
        # using the ServiceType enum values to define the prices : Note  that i  used dictionary since it is more convienant
        self.prices = { ServiceType.DOCTOR_CONSULTATION: 150, ServiceType.NURSING_SERVICES: 120, ServiceType.HOSPITAL_CHARGES: 320, ServiceType.PHARMACY: 415, ServiceType.ROOM_CHARGES: 160 }

    def calculate_final_amount(self, total_amount, insurance_coverage):
        '''calculation for total_amount after insurance_coverage '''
        discount = total_amount * insurance_coverage.value
        return total_amount - discount

    def add_service(self, service_type, price):
        '''Add a new service type.'''
        pass

    def remove_service(self, service_type):
        '''Remove service type'''
        pass

    def update_service_price(self, service_type, new_price):
        '''Update the price of service.'''
        pass


person1 = Person("Omar", "Alameemi", DateTime(2003, 11, 16), "Abu  Dhabi Almushrif.", "+971555060075")

# Create Employee object
employee1 = Employee("Fatima", "Alfalasi", DateTime(1970, 6, 16), "Albateen.", "+050818944", 1233123, DateTime(2020, 6, 1), "Nurse", "General", 50000.0)

# Create Doctor object
doctor1 = Doctor("Mohamed", "Alameemi", DateTime(1981, 6, 16), "Albateen ", "+78489393", 123445, DateTime(2015, 6, 1), "Doctor", "heart", 100000.0, "heart", 10, ["heart Certificate"], "Room 101")

# Create Nurse object
nurse1 = Nurse("Khaled", "Almazrouie", DateTime(200, 10, 8), "Alain", "+235643123", 857373, DateTime(2018, 1, 1), "Nurse", "General", 60000.0, 201, "Morning", ["Nursing Certificate"])

# Create Patient object
patient1 = Patient("Musabbah", "alhumari", DateTime(2000, 4, 4), "Dubai", "+87245914", "AE7489274", DateTime(2023, 5, 1), ["Previous illness"], "Fever", doctor1, "Musabbah alhumari")

# Service and ServiceType
service_obj = Service()
total_amount = service_obj.prices[ServiceType.DOCTOR_CONSULTATION] + service_obj.prices[ServiceType.PHARMACY] #calculation of total cost for  doctor and pharamcy

amount_after_discount = service_obj.calculate_final_amount(total_amount, InsuranceCoverage.HALF) # final amount_after_discount: here we  are calling the function calculate_final_amount to apply the discount  rate with respect to the  insurance_coverage

# Display Receipt
print(f"Receipt Details for Patient: {patient1.get_patient_name()}") #calling patient 1 by using getter()
print("====================================")
print(f"Service: {ServiceType.DOCTOR_CONSULTATION.name}\tPrice: {service_obj.prices[ServiceType.DOCTOR_CONSULTATION]}")
print(f"Service: {ServiceType.PHARMACY.name}\tPrice: {service_obj.prices[ServiceType.PHARMACY]}")
print("------------------------------------")
print(f"Total Amount: {total_amount}")
print(f"Insurance Coverage: {InsuranceCoverage.HALF.name} ({InsuranceCoverage.HALF.value*100}%)")
print(f"Final Amount after Discount: {amount_after_discount}")
print("====================================")














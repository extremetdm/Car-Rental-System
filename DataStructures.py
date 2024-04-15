from datetime import datetime

class Staff:

    _staffList = {}
    _loginAttempts = 0

    def __init__(self, id:str, name:str, role:str, password:str, registration_date:datetime):
        self.id = id
        self.name = name
        if role in ['Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff']:
            self.role = role
        else:
            self.role = 'N/A'
        self.password = password
        self.registration_date = registration_date

        __class__._staffList[id] = self

    @classmethod
    # Returns the user info if credentials are correct.
    # If StaffID doesn't exist, returns 0
    # If password is incorrect, returns the attempt count.
    def login(cls,username:str, password:str):
        if username in cls._staffList:
            staff = cls._staffList[username]
            if password == staff.password:
                return staff
            else:
                cls._loginAttempts += 1
                return cls._loginAttempts
        else:
            return 0

class Customer:

    _CustomerList = {}

    # Auto incrementing CustomerID
    _NewCustomerID = 100001

    def __init__(self, name:str, nric:str, passport_number:str, license_no:str, address:str, phone:str, registration_date:datetime,id=None):
        # Generates CustomerID if no CustomerID given
        if id == None:
            self.id = f'C{__class__._NewCustomerID}'
        else:
            self.id = id
        self.name = name
        self.nric = passport_number
        self.license_no = license_no
        self.address = address
        self.phone = phone
        self.registration_date = registration_date

        __class__._CustomerList[id] = self

        # Increments CustomerID until next empty CustomerId
        while f'C{__class__._NewCustomerID}' in __class__._CustomerList:
            __class__._NewCustomerID += 1

class Car:

    _CarList = {}

    def __init__(self, registration_no, manufacturer, model, manufacture_year, capacity, last_service_date, insurance_policy_number, insurance_expiry, road_tax_expiry, rental_rate = 250, availability = 'Available'):
        self.registration_no = registration_no
        self.manufacturer = manufacturer
        self.model = model
        self.manufacture_year = manufacture_year
        self.capacity = capacity
        self.last_service_date = last_service_date
        self.insurance_policy_number = insurance_policy_number
        self.insurance_expiry = insurance_expiry
        self.road_tax_expiry = road_tax_expiry
        self.rental_rate = rental_rate
        if availability in ['Available','Reserved','Rented','Under Service','Disposed']:
            self.availability = availability
        else:
            self.availability = 'Available'

        __class__._CarList[id] = self

class Rental:
    
    _RentalList = []
    
    def __init__(self, car:Car, customer:Customer, rental_date:datetime, return_date:datetime):
        self.car = car
        self.customer = customer
        self.rental_date = rental_date
        self.return_date = return_date

        self.rental_period = (return_date - rental_date).days
        self.rental_fee = car.rental_rate * self.rental_period

        __class__._RentalList.append(self)

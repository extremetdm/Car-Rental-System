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
    def login(cls,username:str, password:str):
    # Returns the user info if credentials are correct.
    # If StaffID doesn't exist, returns 0
    # If password is incorrect, returns the attempt count.
        if username in cls._staffList:
            staff = cls._staffList[username]
            if password == staff.password:
                return staff
            else:
                cls._loginAttempts += 1
                return cls._loginAttempts
        else:
            return 0

    @classmethod
    def readRecord(cls):
        with open('StaffRecord.txt','r') as f:
            for staffinfo in f.readlines():
                staffinfo = staffinfo.rstrip()
                if staffinfo != '':
                    staffinfo = staffinfo.split('|')
                    staffinfo[-1] = datetime.strptime(staffinfo[-1],'%Y-%m-%d')
                    cls(*staffinfo)

    @classmethod
    def updateRecord(cls):
        with open('StaffRecord.txt','w') as f:
            for staff in cls._staffList.values():
                f.write(f"{staff.id}|{staff.name}|{staff.role}|{staff.password}|{staff.registration_date.strftime('%Y-%m-%d')}\n")

    @classmethod
    def getStaff(cls,id):
        return cls._staffList[id]

class Customer:

    _customerList = {}

    # Auto incrementing CustomerID
    _newCustomerID = 100001

    def __init__(self, name:str, nric:str, passport_number:str, license_no:str, address:str, phone:str, registration_date:datetime,id=None):
        # Generates CustomerID if no CustomerID given
        if id == None:
            self.id = f'C{__class__._newCustomerID}'
        else:
            self.id = id
        self.name = name
        self.nric = nric
        self.passport_number = passport_number
        self.license_no = license_no
        self.address = address
        self.phone = phone
        self.registration_date = registration_date

        __class__._customerList[id] = self

        # Increments CustomerID until next empty CustomerId
        while f'C{__class__._newCustomerID}' in __class__._customerList:
            __class__._newCustomerID += 1

    @classmethod
    def readRecord(cls):
        with open('CustomerRecord.txt','r') as f:
            for customerinfo in f.readlines():
                customerinfo = customerinfo.rstrip()
                if customerinfo != '':
                    customerinfo = customerinfo.split('|')
                    customerinfo[-2] = datetime.strptime(customerinfo[-2],'%Y-%m-%d')
                    cls(*customerinfo)

    @classmethod
    def updateRecord(cls):
        with open('CustomerRecord.txt','w') as f:
            for customer in cls._customerList.values():
                f.write(f"{customer.name}|{customer.nric}|{customer.passport_number}|{customer.license_no}|{customer.address}|{customer.phone}|{customer.registration_date.strftime('%Y-%m-%d')}|{customer.id}\n")

    @classmethod
    def getCustomer(cls,id):
        return cls._customerList[id]

class Car:

    _carList = {}

    def __init__(self, registration_no:str, manufacturer:str, model:str, manufacture_year:int, capacity:int, last_service_date:datetime, insurance_policy_number:str, insurance_expiry:datetime, road_tax_expiry:datetime, rental_rate = 250, availability = 'Available'):
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

        __class__._carList[registration_no] = self

    @classmethod
    def readRecord(cls):
        with open('CarRecord.txt','r') as f:
            for carinfo in f.readlines():
                carinfo = carinfo.rstrip()
                if carinfo != '':
                    carinfo = carinfo.split('|')
                    carinfo[3:6] = int(carinfo[3]), int(carinfo[4]), datetime.strptime(carinfo[5],'%Y-%m-%d')
                    carinfo[7:9] = datetime.strptime(carinfo[7],'%Y-%m-%d'), datetime.strptime(carinfo[8],'%Y-%m-%d')
                    cls(*carinfo)

    @classmethod
    def updateRecord(cls):
        with open('CarRecord.txt','w') as f:
            for car in cls._carList.values():
                f.write(f"{car.registration_no}|{car.manufacturer}|{car.model}|{car.manufacture_year}|{car.capacity}|{car.last_service_date.strftime('%Y-%m-%d')}|{car.insurance_policy_number}|{car.insurance_expiry.strftime('%Y-%m-%d')}|{car.road_tax_expiry.strftime('%Y-%m-%d')}|{car.rental_rate}|{car.availability}\n")

    @classmethod
    def getCar(cls,registration_no):
        return cls._carList[registration_no]

class Rental:
    
    _rentalList = []
    
    def __init__(self, car:Car, customer:Customer, rental_date:datetime, return_date:datetime):
        self.car = car
        self.customer = customer
        self.rental_date = rental_date
        self.return_date = return_date

        self.rental_period = (return_date - rental_date).days
        self.rental_fee = car.rental_rate * self.rental_period

        __class__._rentalList.append(self)

    @classmethod
    def readRecord(cls):
        with open('RentalRecord.txt','r') as f:
            for rentalinfo in f.readlines():
                rentalinfo = rentalinfo.rstrip()
                if rentalinfo != '':
                    rentalinfo = rentalinfo.split('|')
                    rentalinfo = Car.getCar(rentalinfo[0]), Customer.getCustomer(rentalinfo[1]), datetime.strptime(rentalinfo[2],'%Y-%m-%d'), datetime.strptime(rentalinfo[3],'%Y-%m-%d')
                    cls(*rentalinfo)

    @classmethod
    def updateRecord(cls):
        with open('RentalRecord.txt','w') as f:
            for rental in cls._rentalList:
                f.write(f"{rental.car.registration_no}|{rental.customer.id}|{rental.rental_date.strftime('%Y-%m-%d')}|{rental.return_date.strftime('%Y-%m-%d')}\n")
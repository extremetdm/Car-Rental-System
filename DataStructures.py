from datetime import datetime

class Staff:

    _staffList:dict[str:object] = {}

    def __init__(self, id:str, name:str, role:str, password:str, registration_date:datetime,attempts:int=0):
        self.id = id
        self.name = name
        if role in ['Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff']:
            self.role = role
        else:
            self.role = 'N/A'
        self.password = password
        self.registration_date = registration_date

        __class__._staffList[self.id] = self

        self.attempts = attempts

    @classmethod
    def readRecord(cls):
        with open('StaffRecord.txt','r') as f:
            for staffinfo in f.readlines():
                staffinfo = staffinfo.rstrip()
                if staffinfo != '':
                    staffinfo = staffinfo.split('|')
                    staffinfo[-2:] = datetime.strptime(staffinfo[-2],'%Y-%m-%d'), int(staffinfo[-1]) 
                    cls(*staffinfo)

    @classmethod
    def updateRecord(cls):
        with open('StaffRecord.txt','w') as f:
            for staff in cls._staffList.values():
                f.write(f"{staff.id}|{staff.name}|{staff.role}|{staff.password}|{staff.registration_date.strftime('%Y-%m-%d')}|{staff.attempts}\n")

    @classmethod
    def getStaff(cls,id:str) -> object | None:
        if id in cls._staffList:
            return cls._staffList[id]
        else:
            return None
    
    @classmethod
    def staffInRecord(cls,id:str) -> bool:
        if id in cls._staffList:
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return f"|{self.id:^20}|{self.name:^20}|{self.role:^30}|{self.registration_date.strftime('%Y-%m-%d'):^20}|"
    
    @classmethod
    def getStaffList(cls) -> list[object]:
        return cls._staffList.values()


class Customer:

    _customerList:dict[str:object] = {}

    # Auto incrementing CustomerID
    _newCustomerID = 100001

    def __init__(self, name:str, nric:str, passport_number:str, license_no:str, address:str, phone:str, registration_date:datetime,id:str|None=None):
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

        __class__._customerList[self.id] = self

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
    def getCustomer(cls,id:str) -> object|None:
        if id in cls._customerList:
            return cls._customerList[id]
        else:
            return None
    
    @classmethod
    def customerInRecord(cls,id:str) -> bool:
        if id in cls._customerList:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"|{self.id:^20}|{self.name:^20}|{self.nric:^20}|{self.passport_number:^20}|{self.license_no:^20}|{self.address:^50}|{self.phone:^20}|{self.registration_date.strftime('%Y-%m-%d'):^20}|"
    
    @classmethod
    def getCustomerList(cls) -> list[object]:
        return cls._customerList.values()

class Car:

    _carList:dict[str:object] = {}

    def __init__(self, registration_no:str, manufacturer:str, model:str, manufacture_year:int, capacity:int, last_service_date:datetime, insurance_policy_number:str, insurance_expiry:datetime, road_tax_expiry:datetime, rental_rate:int = 250, availability:str = 'Available'):
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

        __class__._carList[self.registration_no] = self

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
    def getCar(cls,registration_no:str) -> object|None:
        if registration_no in cls._carList:
            return cls._carList[registration_no]
        else:
            return None
        
    @classmethod
    def carInRecord(cls,registration_no:str) -> bool:
        if registration_no in cls._carList:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.registration_no:^20}|{self.manufacturer:^20}|{self.model:^20}|{self.manufacture_year:^20}|{self.capacity:^20}|{self.last_service_date.strftime('%Y-%m-%d'):^20}|{self.insurance_policy_number:^20}|{self.insurance_expiry.strftime('%Y-%m-%d'):^20}|{self.road_tax_expiry.strftime('%Y-%m-%d'):^20}|{self.rental_rate:^20}|{self.availability:^20}"

    @classmethod
    def getCarList(cls) -> list[object]:
        return cls._carList.values()

class Rental:
    
    rentalList:list[object] = []
    
    def __init__(self, car:Car, customer:Customer, rental_date:datetime, return_date:datetime):
        self.car = car
        self.customer = customer
        self.rental_date = rental_date
        self.return_date = return_date

        self.rental_period = (return_date - rental_date).days
        self.rental_fee = float(car.rental_rate) * int(self.rental_period)

        __class__.rentalList.append(self)

    @classmethod
    def readRecord(cls):
        with open('RentalRecord.txt','r') as  f:
            for rentalinfo in f.readlines():
                rentalinfo = rentalinfo.rstrip()
                if rentalinfo != '':
                    rentalinfo = rentalinfo.split('|')
                    rentalinfo = Car.getCar(rentalinfo[0]), Customer.getCustomer(rentalinfo[1]), datetime.strptime(rentalinfo[2],'%Y-%m-%d'), datetime.strptime(rentalinfo[3],'%Y-%m-%d')
                    cls(*rentalinfo)

    @classmethod
    def updateRecord(cls):
        with open('RentalRecord.txt','w') as f:
            for rental in cls.rentalList:
                f.write(f"{rental.car.registration_no}|{rental.customer.id}|{rental.rental_date.strftime('%Y-%m-%d')}|{rental.return_date.strftime('%Y-%m-%d')}\n")

    def __repr__(self) -> str:
        return f"{self.car.registration_no:^20}|{self.customer.id:^20}|{self.rental_date.strftime('%Y-%m-%d'):^20}|{self.return_date.strftime('%Y-%m-%d'):^20}"
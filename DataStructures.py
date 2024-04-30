from datetime import datetime

class Staff:

    # Variable to store all staff records
    _staffList:dict[str:object] = {}

    # For adding new staff info into the records
    def __init__(self, id:str, name:str, role:str, password:str, registration_date:datetime,attempts:int=0):

        # Assigning values to all attributes
        self.id = id
        self.name = name
        self.role = role # 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'
        self.password = password
        self.registration_date = registration_date
        self.attempts = attempts

        # Adding staff info to the records
        __class__._staffList[self.id] = self        
    
    # For displaying staff info
    def __repr__(self) -> str:
        return f"|{self.id:^20}|{self.name:^20}|{self.role:^30}|{self.registration_date.strftime('%Y-%m-%d'):^20}|"
    
    # For deleting a staff record
    def delete(self):
        del __class__._staffList[self.id]

    # For querying staff from the records
    @classmethod
    def getStaff(cls,id:str) -> object | None:
        if id in cls._staffList:
            return cls._staffList[id]
        else:
            return None
    
    # Returns a list of all staff and their infos
    @classmethod
    def getStaffList(cls) -> list[object]:
        return cls._staffList.values()
    
    # For checking if a staff is registered in the records
    @classmethod
    def staffInRecord(cls,id:str) -> bool:
        return id in cls._staffList

    # For reading staff records stored in a text file
    @classmethod
    def readRecord(cls):
        with open('StaffRecord.txt','r') as f:
            for staffinfo in f.readlines():
                staffinfo = staffinfo.strip()
                if staffinfo != '':
                    staffinfo = staffinfo.split('|')
                    staffinfo[-2:] = datetime.strptime(staffinfo[-2],'%Y-%m-%d'), int(staffinfo[-1]) 
                    cls(*staffinfo)

    # For storing staff records in a text file
    @classmethod
    def updateRecord(cls):
        with open('StaffRecord.txt','w') as f:
            for staff in cls._staffList.values():
                f.write(f"{staff.id}|{staff.name}|{staff.role}|{staff.password}|{staff.registration_date.strftime('%Y-%m-%d')}|{staff.attempts}\n")

class Customer:

    # Variable to store all customer records
    _customerList:dict[str:object] = {}

    # Auto incrementing CustomerID
    _newCustomerID = 100001

    # For adding new customer info into the records
    def __init__(self, name:str, nric:str, passport_number:str, license_no:str, address:str, phone:str, registration_date:datetime,id:str|None=None):
        
        # Assigning values to all attributes

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

        # Adding customer info to the records
        __class__._customerList[self.id] = self

        # Increments CustomerID until next free CustomerID
        while f'C{__class__._newCustomerID}' in __class__._customerList:
            __class__._newCustomerID += 1

    # For displaying customer info
    def __repr__(self) -> str:
        return f"|{self.id:^20}|{self.name:^20}|{self.nric:^20}|{self.passport_number:^20}|{self.license_no:^20}|{self.address:^50}|{self.phone:^20}|{self.registration_date.strftime('%Y-%m-%d'):^20}|"
    
    # For deleting a customer record
    def delete(self):

        # Ensuring new customer is registered under the first free CustomerID
        if (numericId := int(self.id[1:])) < __class__._newCustomerID:
            __class__._newCustomerID = numericId

        del __class__._customerList[self.id]

    # For querying customer from the records
    @classmethod
    def getCustomer(cls,id:str) -> object|None:
        if id in cls._customerList:
            return cls._customerList[id]
        else:
            return None

    # Returns a list of all customer and their infos
    @classmethod
    def getCustomerList(cls) -> list[object]:
        return cls._customerList.values()  

    # For checking if a customer is registered in the records
    @classmethod
    def customerInRecord(cls,id:str) -> bool:
        return id in cls._customerList

    # For reading customer records stored in a text file
    @classmethod
    def readRecord(cls):
        with open('CustomerRecord.txt','r') as f:
            for customerinfo in f.readlines():
                customerinfo = customerinfo.strip()
                if customerinfo != '':
                    customerinfo = customerinfo.split('|')
                    customerinfo[-2] = datetime.strptime(customerinfo[-2],'%Y-%m-%d')
                    cls(*customerinfo)

    # For storing customer records in a text file
    @classmethod
    def updateRecord(cls):
        with open('CustomerRecord.txt','w') as f:
            for customer in cls._customerList.values():
                f.write(f"{customer.name}|{customer.nric}|{customer.passport_number}|{customer.license_no}|{customer.address}|{customer.phone}|{customer.registration_date.strftime('%Y-%m-%d')}|{customer.id}\n")

class Car:

    # Variable to store all car records
    _carList:dict[str:object] = {}

    # Variable to store the default renting rates of cars (based on car capacity)
    _carDefaultRentalRate:dict[int:float] = {}

    # For adding new car info into the records
    def __init__(self, registration_no:str, manufacturer:str, model:str, manufacture_year:int, capacity:int, last_service_date:datetime, insurance_policy_number:str, insurance_expiry:datetime, road_tax_expiry:datetime, specificRentalRate:float|None = None, availability:str = 'Available'):
        
        # Assigning values to all attributes
        self.registration_no = registration_no
        self.manufacturer = manufacturer
        self.model = model
        self.manufacture_year = manufacture_year
        self.capacity = capacity # 2, 4, 5, 6, 7, 8, 9
        self.last_service_date = last_service_date
        self.insurance_policy_number = insurance_policy_number
        self.insurance_expiry = insurance_expiry
        self.road_tax_expiry = road_tax_expiry
        self._specificRentalRate = specificRentalRate
        self.availability = availability # 'Available','Reserved','Rented','Under Service','Disposed'

        # Adding customer info to the records
        __class__._carList[self.registration_no] = self

    # For setting a car-specific rental rate
    def setSpecificRentalRate(self,rentalRate:float|None):
        self._specificRentalRate = rentalRate

    # Returns the car's rental rate
    def getRentalRate(self) -> float:
        if self._specificRentalRate == None:
            return __class__._carDefaultRentalRate[self.capacity]
        else:
            return self._specificRentalRate
        
    # For displaying car info
    def __repr__(self) -> str:
        return f"|{self.registration_no:^20}|{self.manufacturer:^15}|{self.model:^15}|{self.manufacture_year:^20}|{self.capacity:^20}|{self.last_service_date.strftime('%Y-%m-%d'):^20}|{self.insurance_policy_number:^20}|{self.insurance_expiry.strftime('%Y-%m-%d'):^20}|{self.road_tax_expiry.strftime('%Y-%m-%d'):^20}|{self.getRentalRate():^20.2f}|{self.availability:^15}|"

    # For deleting a car record
    def delete(self):
        del __class__._carList[self.registration_no]

    # For querying car from the records
    @classmethod
    def getCar(cls,registration_no:str) -> object|None:
        if registration_no in cls._carList:
            return cls._carList[registration_no]
        else:
            return None
            
    # Returns a list of all car and their infos
    @classmethod
    def getCarList(cls) -> list[object]:
        return cls._carList.values()
    
    # For checking if a car is registered in the records
    @classmethod
    def carInRecord(cls,registration_no:str) -> bool:
        return registration_no in cls._carList

    # For updating the default car renting rates
    @classmethod
    def updateDefaultRentalRate(cls,capacity:int,rentalRate:float):
        cls._carDefaultRentalRate[capacity] = rentalRate

    # For reading car records stored in a text file
    @classmethod
    def readRecord(cls):
        with open('CarRecord.txt','r') as f:
            record = f.readlines()
            __class__._carDefaultRentalRate = {capacity:float(rentalRate) for capacity, rentalRate in zip((2, 4, 5, 6, 7, 8, 9),record[0].strip().split('|'))}
            for carinfo in record[1:]:
                carinfo = carinfo.strip()
                if carinfo != '':
                    carinfo = carinfo.split('|')
                    carinfo[3:6] = int(carinfo[3]), int(carinfo[4]), datetime.strptime(carinfo[5],'%Y-%m-%d')
                    carinfo[7:10] = datetime.strptime(carinfo[7],'%Y-%m-%d'), datetime.strptime(carinfo[8],'%Y-%m-%d'), None if carinfo[9] == 'None' else float(carinfo[9])
                    cls(*carinfo)

    # For storing car records in a text file
    @classmethod
    def updateRecord(cls):
        with open('CarRecord.txt','w') as f:
            f.write('|'.join(map(lambda x:f'{x:.2f}',cls._carDefaultRentalRate.values()))+'\n')
            for car in cls._carList.values():
                f.write(f"{car.registration_no}|{car.manufacturer}|{car.model}|{car.manufacture_year}|{car.capacity}|{car.last_service_date.strftime('%Y-%m-%d')}|{car.insurance_policy_number}|{car.insurance_expiry.strftime('%Y-%m-%d')}|{car.road_tax_expiry.strftime('%Y-%m-%d')}|{car._specificRentalRate}|{car.availability}\n")

class Rental:
    
    # Variable to store all rental records
    _rentalList:dict[str:object] = {}

    # Auto incrementing TransactionID
    _newTransactionID = 1

    # For adding new rental info into the records
    def __init__(self, car:Car, customer:Customer, rental_date:datetime, return_date:datetime, transactionID:str|None = None, status:str = 'Pending', rental_fee:float|None = None):
        
        # Assigning values to all attributes

        # Generates TransactionID if no TransactionID given
        if transactionID == None:
            self.transactionID = f'RT{__class__._newTransactionID:0>6}'
        else:
            self.transactionID = transactionID
        
        self.car = car
        self.customer = customer
        self.rental_date = rental_date
        self.return_date = return_date
        self.status = status

        # Deriving rental period
        self.rental_period = (return_date - rental_date).days

        # Deriving rental fee if rental fee not given
        if rental_fee == None:
            self.rental_fee = car.getRentalRate() * self.rental_period
        else:
            self.rental_fee = rental_fee

        __class__._rentalList[self.transactionID] = self

        # Increments TransactionID until next free TransactionID
        while f'RT{__class__._newTransactionID:0>6}' in __class__._rentalList:
            __class__._newTransactionID += 1

    # For displaying rental info
    def __repr__(self) -> str:
        return f"|{self.transactionID:^20}|{self.car.registration_no:^20}|{self.customer.id:^20}|{self.rental_date.strftime('%Y-%m-%d'):^20}|{self.return_date.strftime('%Y-%m-%d'):^20}|{self.rental_fee:^20,.2f}|{self.status:^20}|"
    
    # For deleting a car record
    def delete(self):

        # Ensuring new transactions is recorded under the first free TransactionID
        if (numericId := int(self.transactionID[2:])) < __class__._newTransactionID:
            __class__._newTransactionID = numericId

        del __class__._rentalList[self.transactionID]

    # For querying rental from the records
    @classmethod
    def getRental(cls,transactionID:str) -> object|None:
        if transactionID in cls._rentalList:
            return cls._rentalList[transactionID]
        else:
            return None
        
    # Returns a list of all rental infos
    @classmethod
    def getRentalList(cls):
        return cls._rentalList.values()

    # For checking if a rental in the records
    @classmethod
    def rentalInRecord(cls,transactionID):
        return transactionID in cls._rentalList
    
    # For checking if a customer is involved in a rental
    @classmethod
    def customerInRecord(cls,customer:Customer) -> bool:
        return customer in map(lambda x:x.customer,cls._rentalList.values())
        
    # For checking if a car is involved in a rental
    @classmethod
    def carInRecord(cls,car:Car) -> bool:
        return car in map(lambda x:x.car,cls._rentalList.values())

    # For reading rental records stored in a text file
    @classmethod
    def readRecord(cls):
        with open('RentalRecord.txt','r') as  f:
            for rentalinfo in f.readlines():
                rentalinfo = rentalinfo.strip()
                if rentalinfo != '':
                    rentalinfo = rentalinfo.split('|')
                    rentalinfo[:4] = (Car.getCar(rentalinfo[0]), 
                                      Customer.getCustomer(rentalinfo[1]), 
                                      datetime.strptime(rentalinfo[2],'%Y-%m-%d'), 
                                      datetime.strptime(rentalinfo[3],'%Y-%m-%d') )
                    rentalinfo[6] = None if rentalinfo[6] == 'None' else float(rentalinfo[6])
                    cls(*rentalinfo)

    # For storing rental records in a text file
    @classmethod
    def updateRecord(cls):
        with open('RentalRecord.txt','w') as f:
            for rental in cls._rentalList.values():
                # Only record the rental fee when it has been finalized (customer paid for rental)
                if rental.status == 'Pending':
                    rentalFee = None
                else:
                    rentalFee = f'{rental.rental_fee:.2f}'
                f.write(f"{rental.car.registration_no}|{rental.customer.id}|{rental.rental_date.strftime('%Y-%m-%d')}|{rental.return_date.strftime('%Y-%m-%d')}|{rental.transactionID}|{rental.status}|{rentalFee}\n")

# For debugging purposes only
if __name__ == '__main__':
  
    Staff.readRecord()
    Customer.readRecord()
    Car.readRecord()
    Rental.readRecord()

    Staff.updateRecord()
    Customer.updateRecord()
    Car.updateRecord()
    Rental.updateRecord()
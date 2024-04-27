from datetime import datetime

class Staff:

    _staffList:dict[str:object] = {}

    def __init__(self, id:str, name:str, role:str, password:str, registration_date:datetime,attempts:int=0):
        self.id = id
        self.name = name
        self.role = role # 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'
        self.password = password
        self.registration_date = registration_date

        __class__._staffList[self.id] = self

        self.attempts = attempts

    @classmethod
    def readRecord(cls):
        with open('StaffRecord.txt','r') as f:
            for staffinfo in f.readlines():
                staffinfo = staffinfo.strip()
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
    
    def delete(self):
        del __class__._staffList[self.id]


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

        # Increments CustomerID until next free CustomerId
        while f'C{__class__._newCustomerID}' in __class__._customerList:
            __class__._newCustomerID += 1

    @classmethod
    def readRecord(cls):
        with open('CustomerRecord.txt','r') as f:
            for customerinfo in f.readlines():
                customerinfo = customerinfo.strip()
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
    
    def delete(self):
        # Making sure new customer is registered under the first free CustomerID
        if (numericId := int(self.id[1:])) < __class__._newCustomerID:
            __class__._newCustomerID = numericId

        del __class__._customerList[self.id]

class Car:

    _carList:dict[str:object] = {}
    _carDefaultRentalRate:dict[int:float] = {}

    def __init__(self, registration_no:str, manufacturer:str, model:str, manufacture_year:int, capacity:int, last_service_date:datetime, insurance_policy_number:str, insurance_expiry:datetime, road_tax_expiry:datetime, specificRentalRate:float|None = None, availability:str = 'Available'):
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

        if availability in ['Available','Reserved','Rented','Under Service','Disposed']:
            self.availability = availability
        else:
            self.availability = 'Available'

        __class__._carList[self.registration_no] = self

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

    @classmethod
    def updateRecord(cls):
        with open('CarRecord.txt','w') as f:
            f.write('|'.join(map(lambda x:f'{x:.2f}',cls._carDefaultRentalRate.values()))+'\n')
            for car in cls._carList.values():
                f.write(f"{car.registration_no}|{car.manufacturer}|{car.model}|{car.manufacture_year}|{car.capacity}|{car.last_service_date.strftime('%Y-%m-%d')}|{car.insurance_policy_number}|{car.insurance_expiry.strftime('%Y-%m-%d')}|{car.road_tax_expiry.strftime('%Y-%m-%d')}|{car._specificRentalRate}|{car.availability}\n")

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
        return f"|{self.registration_no:^20}|{self.manufacturer:^15}|{self.model:^15}|{self.manufacture_year:^20}|{self.capacity:^20}|{self.last_service_date.strftime('%Y-%m-%d'):^20}|{self.insurance_policy_number:^20}|{self.insurance_expiry.strftime('%Y-%m-%d'):^20}|{self.road_tax_expiry.strftime('%Y-%m-%d'):^20}|{self.getRentalRate():^20.2f}|{self.availability:^15}|"

    @classmethod
    def getCarList(cls) -> list[object]:
        return cls._carList.values()
    
    def delete(self):
        del __class__._carList[self.registration_no]

    @classmethod
    def updateDefaultRentalRate(cls,capacity:int,rentalRate:float):
        cls._carDefaultRentalRate[capacity] = rentalRate

    def getRentalRate(self):
        if self._specificRentalRate == None:
            return __class__._carDefaultRentalRate[self.capacity]
        else:
            return self._specificRentalRate

    def setSpecificRentalRate(self,rentalRate:float|None):
        self._specificRentalRate = rentalRate
    


class Rental:
    
    _rentalList:dict[str:object] = {}

    # Auto incrementing TransactionID
    _newTransactionID = 1

    def __init__(self, car:Car, customer:Customer, rental_date:datetime, return_date:datetime, 
                 transactionID:str|None = None, status:str = 'Pending',
                 rental_fee:float|None = None
                 ):
        
        if transactionID == None:
            self.transactionID = f'RT{__class__._newTransactionID:0>6}'
        else:
            self.transactionID = transactionID
        
        self.car = car
        self.customer = customer
        self.rental_date = rental_date
        self.return_date = return_date

        self.rental_period = (return_date - rental_date).days

        if rental_fee == None:
            self.rental_fee = car.getRentalRate() * self.rental_period
        else:
            self.rental_fee = rental_fee

        self.status = status

        __class__._rentalList[self.transactionID] = self

        # Increments TransactionID until next free TransactionID
        while f'RT{__class__._newTransactionID:0>6}' in __class__._rentalList:
            __class__._newTransactionID += 1

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

    @classmethod
    def updateRecord(cls):
        with open('RentalRecord.txt','w') as f:
            for rental in cls._rentalList.values():
                if rental.status == 'Pending':
                    rentalFee = None
                else:
                    rentalFee = f'{rental.rental_fee:.2f}'
                f.write(f"{rental.car.registration_no}|{rental.customer.id}|{rental.rental_date.strftime('%Y-%m-%d')}|{rental.return_date.strftime('%Y-%m-%d')}|{rental.transactionID}|{rental.status}|{rentalFee}\n")

    def __repr__(self) -> str:
        return f"|{self.transactionID:^20}|{self.car.registration_no:^20}|{self.customer.id:^20}|{self.rental_date.strftime('%Y-%m-%d'):^20}|{self.return_date.strftime('%Y-%m-%d'):^20}|{self.rental_fee:^20.2f}|{self.status}"
    
    @classmethod
    def customerInRecord(cls,customer:Customer) -> bool:
        if customer in map(lambda x:x.customer,cls._rentalList.values()):
            return True
        else:
            return False
        
    @classmethod
    def carInRecord(cls,car:Car) -> bool:
        if car in map(lambda x:x.car,cls._rentalList.values()):
            return True
        else:
            return False
        
    def delete(self):
        # Making sure new transactions is recorded under the first free TransactionID
        if (numericId := int(self.transactionID[2:])) < __class__._newTransactionID:
            __class__._newTransactionID = numericId

        del __class__._rentalList[self.transactionID]

    @classmethod
    def getRentalList(cls):
        return cls._rentalList.values()

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
from DataStructures import *
from function import *

def registerCustomer():
  name = getValidInput('\nEnter customer name: ',
                       (lambda x:x != '','\nCustomer name cannot be empty!') )
  localness = getValidInput('\nIs customer a local? (Y/N): ',
                            (lambda x:x.upper() in ('Y','N'),'Invalid input!') ).upper()
  if localness == 'Y':
    # if im bothered enough imma do further validation with date, state code and input with - but for now this is good enough 
    nric = getValidInput('\nEnter customer NRIC (without -): ',
                         (lambda x:x.isnumeric() & (len(x) == 12),'\nInvalid NRIC!') )
    passportNumber = 'None'
  else:
    nric = 'None'
    passportNumber = getValidInput('\nEnter customer passport number: ',
                                   (lambda x:x.isalnum(),'\nInvalid passport number!') )
  licenseNo = getValidInput('\nEnter customer driving license card number: ',
                            (lambda x:x.isalnum(),'\nInvalid driving license card number!') )
  address = getValidInput('\nEnter customer address: ',
                          (lambda x:x != '','\nAddress cannot be empty!') )
  # if im bothered enough may actually validate phone number but for now this is fine
  phone = getValidInput('\nEnter customer phone number: ',
                        (lambda x:x.isnumeric(),'\nInvalid phone number!') )
  registrationDate = datetime.today()
  Customer(name,nric,passportNumber,licenseNo,address,phone,registrationDate)
  print('\nCustomer has been successfully registered.\n')

def viewCustomer():
  print()
  for customer in Customer.getCustomerList():
      print(customer)
  print()

def updateCustomer():
  customer:Customer = Customer.getCustomer(getValidInput('\nEnter Customer ID: ',(lambda x:Customer.customerInRecord(x),'\nInvalid Customer ID!')))
  print(f'\nWhich info of {customer.name} would you like to change?\n')
  print('1.\tPhone number')
  print('2.\tAddress')
  print('3.\tLicense number')
  if customer.nric == 'None':
    validInputList = ('1','2','3','4')
    print('4.\tPassport number')
  else:
    validInputList = ('1','2','3')
  toUpdate = getValidInput('\n-> ',(lambda x:x in validInputList,'\nInvalid input!'))
  match toUpdate:
    case '1':
      updatedDetail = 'phone number'
      customer.phone = getValidInput('\nEnter new customer phone number: ',
                                     (lambda x:x.isnumeric(),'\nInvalid phone number!') )
    case '2':
      updatedDetail = 'address'
      customer.address = getValidInput('\nEnter new customer address: ',
                                       (lambda x:x != '','\nAddress cannot be empty!') )
    case '3':
      updatedDetail = 'driving license card number'
      customer.license_no = getValidInput('\nEnter new customer driving license card number: ',
                                          (lambda x:x.isalnum(),'\nInvalid driving license card number!') )
    case '4':
      updatedDetail = 'ppassport number'
      customer.passport_number = getValidInput('\nEnter new customer passport number: ',
                                               (lambda x:x.isalnum(),'\nInvalid passport number!') )
  print(f"\n{customer.name}'s {updatedDetail} has been changed successfully.")

def customer1Menu(user:Staff):
  while True:
    print('1.\tUpdate own profile')
    print('2.\tRegister new customer')
    print('3.\tView registered customers')
    print('4.\tUpdate existing customer')
    print('5.\tDelete inactive customer')
    print('6.\tExit program')

    operation = getValidInput('\nEnter operation number: ',(lambda x:x in ('1','2','3','4','5','6'),'\nInvalid operation number!'))

    match operation:
      case '1':
        updateProfile(user)

      case '2':
        registerCustomer()

      case '3':
        viewCustomer()

      case '4':
        updateCustomer()

      case '5':
        pass

      case '6':
        return
       
# For debugging purposes only
if __name__ == '__main__':
  Staff.readRecord()
  Customer.readRecord()
  Car.readRecord()
  Rental.readRecord()

  customer1Menu(Staff.getStaff('some'))

  Staff.updateRecord()
  Customer.updateRecord()
  Car.updateRecord()
  Rental.updateRecord()
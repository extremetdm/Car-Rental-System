from DataStructures import *
from function import *

def registerCustomer():

  # Gathering all neccessary customer infos
  name = getValidInput('\nEnter customer name: ',
                       (lambda x:x != '','\nCustomer name cannot be empty!') )
  # Determining whether customer is a local or a foreigner
  localness = getValidInput('\nIs customer a local? (Y/N): ',
                            (lambda x:x.upper() in ('Y','N'),'Invalid input!') ).upper()
  if localness == 'Y':
    # Get NRIC if local customer
    nric = getValidInput('\nEnter customer NRIC (without -): ',
                         (lambda x:x.isnumeric() & (len(x) == 12),'\nInvalid NRIC!') )
    passportNumber = 'None'
  else:
    # Get Passport Number if foreign customer
    nric = 'None'
    passportNumber = getValidInput('\nEnter customer passport number: ',
                                   (lambda x:x.isalnum(),'\nInvalid passport number!') )
  licenseNo = getValidInput('\nEnter customer driving license card number: ',
                            (lambda x:x.isalnum(),'\nInvalid driving license card number!') )
  address = getValidInput('\nEnter customer address: ',
                          (lambda x:x != '','\nAddress cannot be empty!') )
  phone = getValidInput('\nEnter customer phone number: ',
                        (lambda x:x.isnumeric(),'\nInvalid phone number!') )
  registrationDate = datetime.today()

  # Add customer to the record
  Customer(name,nric,passportNumber,licenseNo,address,phone,registrationDate)
  Customer.updateRecord()
  print('\nCustomer has been successfully registered.\n')

def viewCustomer(constraint = lambda x:True):
  # Checking if any customer fits the criteria
  if any(map(constraint,Customer.getCustomerList())):

    # Header
    print('\n' + 199*'-')
    print(f"|{'Customer ID':^20}|{'Name':^20}|{'NRIC':^20}|{'Passport Number':^20}|{'Driving License No.':^20}|{'Address':^50}|{'Phone Number':^20}|{'Registration Date':^20}|")
    print(199*'-')

    # Customer info
    for customer in Customer.getCustomerList():
      if constraint(customer):
        print(customer)

    # Footer
    print(199*'-'+'\n')

  else:
    print('\nNo customer record found!\n')

def updateCustomer():

  # Querying customer from the records
  customer:Customer = Customer.getCustomer(getValidInput('\nEnter Customer ID: ',(Customer.customerInRecord,'\nInvalid Customer ID!')))
  
  # Info update options
  print(f'\nWhich info of {customer.name} would you like to change?\n')
  print('1.\tPhone number')
  print('2.\tAddress')
  print('3.\tLicense number')
  if customer.nric == 'None':
    # If customer is foreigner add update passport option
    validInputList = ('1','2','3','4')
    print('4.\tPassport number')
  else:
    validInputList = ('1','2','3')

  # Determining which info needs updating
  toUpdate = int(getValidInput('\n-> ',(lambda x:x in validInputList,'\nInvalid input!')))

  # Accepting new info to update existing info
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
      updatedDetail = 'passport number'
      customer.passport_number = getValidInput('\nEnter new customer passport number: ',
                                               (lambda x:x.isalnum(),'\nInvalid passport number!') )
  
  # Update customer info in the record
  Customer.updateRecord()
  print(f"\n{customer.name}'s {updatedDetail} has been changed successfully.\n")

def deleteCustomer():

  # Checking for any inactive customers
  if all(map(Rental.customerInRecord,Customer.getCustomerList())):

    # Showing list of inactive customers
    print('\nList of inactive customers:')
    viewCustomer(lambda customer:not Rental.customerInRecord(customer))

    # Determining which customer info to be deleted
    customer:Customer = Customer.getCustomer(getValidInput('Enter Customer ID: ',
                                                          (Customer.customerInRecord,'\nInvalid Customer ID!\n'),
                                                          (lambda customerId:not Rental.customerInRecord(Customer.getCustomer(customerId)),'\nCustomer is still active!\n')))
    
    # Confirm deletion
    confirmation = getValidInput(f'\nDelete record of {customer.name}? (Y/N): ',(lambda x:x.upper() in ('Y','N'),'\nInvalid Input!')).upper()

    if confirmation == 'Y':
    # Delete customer info from the records
      customer.delete()
      Customer.updateRecord()
      print('\nCustomer has been deleted successfully.\n')
    
    else:
      print('\nOperation has been cancelled.\n')

  else:
    print('\nNo inactive customers found!\n')

def customer1Menu(user:Staff):
  while True:
    # Menu operation
    print('1.\tUpdate own profile')
    print('2.\tRegister new customer')
    print('3.\tView registered customers')
    print('4.\tUpdate existing customer')
    print('5.\tDelete inactive customer')
    print('6.\tExit program')

    # Determining operation
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
        deleteCustomer()

      case '6':
        return
       
# For debugging purposes only
if __name__ == '__main__':
  Staff.readRecord()
  Customer.readRecord()
  Car.readRecord()
  Rental.readRecord()

  customer1Menu(Staff.getStaff('some'))
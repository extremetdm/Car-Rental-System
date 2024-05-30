from DataStructures import *
from function import *

def recordRental() -> None:

  # Checking for available cars
  if any(map(lambda car:car.availability == 'Available',Car.getCarList())):
    
    # Gathering all neccessary rental infos
    car = Car.getCar(getValidInput('\nEnter car registration number: ',
                                  (Car.carInRecord,'\nCar not registered in car record!'),
                                  (lambda car:Car.getCar(car).availability == 'Available','Car unavailable!')))
    customer = Customer.getCustomer(getValidInput('\nEnter Customer ID: ',
                                                  (Customer.customerInRecord,'\nCustomer not registered in customer record!') ))
    rentalDate = datetime.strptime(getValidInput('\nEnter rental date (YYYY-MM-DD): ', 
                                                (validDate, '\nInvalid date!'),
                                                (lambda date:datetime.strptime(date,'%Y-%m-%d').date() >= datetime.today().date(), '\nRental date cannot be before today!')),'%Y-%m-%d')
    returnDate = datetime.strptime(getValidInput('\nEnter return date (YYYY-MM-DD): ', 
                                                (validDate, '\nInvalid date!'),
                                                (lambda date:datetime.strptime(date,'%Y-%m-%d') > rentalDate, '\nReturn date cannot be before and on rental date!')),'%Y-%m-%d')
    
    # Record rental request and reserve car
    car.availability = 'Reserved'
    rental = Rental(car,customer,rentalDate,returnDate)
    Rental.updateRecord()
    Car.updateRecord()
    print('\nRental request has been successfully recorded.')
    
    # Generate bill if paying immediately
    paying = getValidInput('\nGenerate bill? (Y/N): ',
                        (lambda enteredInput:enteredInput.upper() in ('Y','N'),'\nInvalid input!\n') ).upper()
    if paying == 'Y':
      generateBill(rental)

  else:
    print('\nNo available cars found!\n')

def generateBill(rental:Rental|None = None) -> None:
  
  # Checking for unresolved transactions
  if any(map(lambda rental:rental.status == 'Pending',Rental.getRentalList())):

    if rental == None:
      # Determining rental request for bill generation
      print('\nUnresolved transactions: ')
      viewRental(lambda rental:rental.status == 'Pending')
      rental:Rental = Rental.getRental(getValidInput('Enter Transaction ID: ',
                                                    (Rental.rentalInRecord,'\nInvalid Transaction ID!\n'),
                                                    (lambda transactionID:Rental.getRental(transactionID).status == 'Pending','\nTransaction already resolved!\n')))

    # Generating bill
    print(f"\n{'Receipt':>20}\n")
    print(f"{'CustomerID: ':>18}{rental.customer.id}")
    print(f"{'Name: ':>18}{rental.customer.name}")
    print(f"{'Car Plate Number: ':>18}{rental.car.registration_no}")
    print(f"{'Manufacturer: ':>18}{rental.car.manufacturer}")
    print(f"{'Model: ':>18}{rental.car.model}")
    print(f"{'Rental Date: ':>18}{rental.rental_date.strftime('%Y-%m-%d')}")
    print(f"{'Return Date: ':>18}{rental.return_date.strftime('%Y-%m-%d')}")
    print(f"{'Rental Period: ':>18}{rental.rental_period} day{'s' if rental.rental_period > 1 else ''}")
    print(f"{'Total Due: ':>18}${rental.rental_fee:,.2f}\n")

    # Confirming whether customer has paid the bill
    paid = getValidInput('Customer Paid? (Y/N): ',
                        (lambda enteredInput:enteredInput.upper() in ('Y','N'),'\nInvalid input!\n') ).upper()
    if paid == 'Y':
      # Update transaction status
      rental.status = 'Paid'
      Rental.updateRecord()
      
    print()
  
  else:
    print('\nNo unresolved transactions found!\n')

def deleteRental() -> None:
  
  # Checking for unresolved transactions
  if any(map(lambda rental:rental.status == 'Pending',Rental.getRentalList())):

    # Showing list of unresolved transactions
    print('\nUnresolved transactions: ')
    viewRental(lambda rental:rental.status == 'Pending')

    # Determining which rental info to be deleted
    rental:Rental = Rental.getRental(getValidInput('Enter Transaction ID: ',
                                                  (Rental.rentalInRecord,'\nInvalid Transaction ID!\n'),
                                                  (lambda transactionID:Rental.getRental(transactionID).status == 'Pending','\nTransaction already resolved!\n')))

    # Confirm deletion
    confirmation = getValidInput(f'\nDelete record of {rental.transactionID}? (Y/N): ',(lambda enteredInput:enteredInput.upper() in ('Y','N'),'\nInvalid Input!')).upper()

    if confirmation == 'Y':
      # Delete rental info from the records
      rental.delete()
      Rental.updateRecord()
      print('\nRental request has been deleted successfully.\n')
    
    else:
      print('\nOperation has been cancelled.\n')

  else:
    print('\nNo unresolved transactions found!\n')

def customer2Menu(user:Staff) -> None:
  while True:
    # Menu selection
    print('1.\tUpdate own profile')
    print('2.\tView available cars')
    print('3.\tRecord new rental request')
    print('4.\tGenerate bill')
    print('5.\tView rental transactions')
    print('6.\tCancel and delete rental request')
    print('7.\tExit program')
    
    # Determining operation
    operation = getValidInput('\nEnter operation number: ',(lambda enteredInput:enteredInput in ('1','2','3','4','5','6','7'),'\nInvalid operation number!'))
    match operation:
      case '1':
        updateProfile(user)

      case '2':
        viewCar(lambda car:car.availability == 'Available')

      case '3':
        recordRental()

      case '4':
        generateBill()

      case '5':
        viewRental()

      case '6':
        deleteRental()

      case '7':
        return

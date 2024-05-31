from DataStructures import *
from function import *

# Function to check if a given string is a valid Malaysian car plate number
def is_valid_malaysian_plate(plate: str) -> bool:
  import re
  return re.fullmatch(r'[A-Z]{1,3}\d{1,4}[A-Z]{0,1}', plate) is not None

# Function to register a new car
def registerCar() -> None:
  while True:
    # Ask the user if they want to register a new car
    if getValidInput('\nDo you want to register a new car for rental? (Y/N): ',
                    (lambda enteredInput: enteredInput != '' and enteredInput.upper() in ('Y', 'N'), 'Insert cannot be empty or must be Y/N')).upper() != 'Y':
      break
    else:
      # Print some information for the staff
      print('\nInformation for staff:\nplease take note that if got car plate like <SELANGOR 1>, please contact to Manager to have a manual input')
      print('\nNew Car detail:\n')
      
      # Ask the user for the car plate, manufacturer, model, manufacture year, capacity, last service date, insurance policy number, insurance expiry date, and road tax expiry date
      # Validate each input as necessary
      registration_no = getValidInput('\n-> Car plate: ', 
                                      (lambda enteredInput:enteredInput != '', '\nInput cannot be empty!'), 
                                      (lambda plate:is_valid_malaysian_plate(plate.upper()), '\nCar Plate does not follow the Malaysia JPJ rules')).upper()
      
      manufacturer = getValidInput('\n-> Manufacturer: ', 
                                   (lambda enteredInput:enteredInput != '', '\nInput cannot be empty!')).upper()
      
      model = getValidInput('\n-> Model: ', 
                                   (lambda enteredInput:enteredInput != '', '\nInput cannot be empty!')).upper()
      
      manufacture_year = int(getValidInput('\n-> Manufacture year: ', 
                                   (lambda enteredInput:enteredInput != '', '\nInput cannot be empty!'),
                                   (str.isdigit,'\nManufacture year must be in format (YYYY)'),
                                   (lambda year:len(year) == 4, '\nManufacture year must be a 4-digit number'),
                                   (lambda year:int(year) >= 1803,'\nThe time not even got an engine car yet'),
                                   (lambda year:int(year) <= (datetime.today().year), '\nManufacture year cannot exits current year')))
      
      capacity = int(getValidInput('\n-> capacity: ', 
                     (lambda enteredInput:enteredInput != '', '\nInput cannot be empty!'),
                     (str.isdigit, '\nCapacity must be in number'),
                     (lambda capacity:int(capacity) in (2, 4, 5, 6, 7, 8, 9), '\nCapacity is not recognise')))
      
      if manufacture_year != datetime.today().year:
        last_service_date = datetime.strptime(getValidInput('\nWhat is the car last service date? (YYYY-MM-DD): ', 
                                          (lambda enteredInput:enteredInput != '', '\nLast service date cannot be empty'),
                                          (lambda date:validDate(date) and int(date[:4]) >= 1804,'\nMust be in date format and year must be 1804 or later')), '%Y-%m-%d')

      insurance_policy_number = getValidInput('\nWhat is the car insurance policy number? ', 
                                        (lambda enteredInput:enteredInput != '', '\nInput cannot be empty!'),
                                        (lambda enteredInput:8 <= len(enteredInput) <= 13, '\nInsurance policy number must be 8 to 13 characters long'),
                                        (str.isalnum, '\nInsurance policy number must contain only alphanumeric characters')).upper()
      
      insurance_expiry = datetime.strptime(getValidInput('\nWhat is the car insurance expiry date? (YYYY-MM-DD): ', 
                                        (lambda enteredInput:enteredInput != '', '\nInsurance expiry date cannot be empty'),
                                        (validDate,'\nMust be in date format'),
                                        (lambda date:datetime.strptime(date, '%Y-%m-%d') >= datetime.now(),'\nCar insurance cannot be expired, please inform customer to renew their insurance')), '%Y-%m-%d')
      
      road_tax_expiry = datetime.strptime(getValidInput('\nWhat is the car road tax expiry date? (YYYY-MM-DD): ', 
                                        (lambda enteredInput:enteredInput != '', '\nRoad tax expiry date cannot be empty'),
                                        (validDate,'\nMust be in date format'),
                                        (lambda date:datetime.strptime(date, '%Y-%m-%d') >= datetime.now(),'\nRoad tax cannot be expired, please inform customer to renew their road tax'),
                                        (lambda date:datetime.strptime(date, '%Y-%m-%d').year <= datetime.now().year + 1,'\nRoad tax expiry date cannot be more than one year from the current date')), '%Y-%m-%d')
      
      # If all inputs are valid, create a new Car object and add it to the record
      if manufacture_year != datetime.today().year:
        Car(registration_no,manufacturer,model,manufacture_year,capacity,last_service_date,insurance_policy_number,insurance_expiry,road_tax_expiry)
      else:
        Car(registration_no,manufacturer,model,manufacture_year,capacity,None,insurance_policy_number,insurance_expiry,road_tax_expiry)

      Car.updateRecord()
      
      # Print the new car record
      print()
      header = f"|{'Plate No.':^20}|{'Manufacturer':^15}|{'Model':^15}|{'Manufacture Year':^20}|{'Capacity':^20}|{'Last Service Date':^20}|{'Insurance No.':^20}|{'Insurance Exp. Date':^20}|{'Road Tax Exp. Date':^20}|{'Rental Rate':^20}|{'Availability':^15}|"
      print('New Car Record'.center(len(header)),'\n','-' * (len(header)-2))
      print(header,'\n','-' * (len(header) - 2))
      print(Car.getCar(registration_no))


def displaySimplifiedCarList() -> list[Car]:
    # Get a list of all cars
    car_list = list(Car.getCarList())
    
    # Print a newline for formatting
    print()
    
    # Define the header for the table
    header = f"|{'No.':^5}|{'Registration No.':^20}|{'Manufacturer':^15}|{'Model':^15}|{'Last Service Date':^20}|{'Insurance No.':^20}|{'Insurance Exp. Date':^20}|{'Road Tax Exp. Date':^20}|{'Availability':^15}|"
    
    # Print the table title and header
    print('Car Record'.center(len(header)),'\n','-' * (len(header)-2))
    print(header,'\n','-' * (len(header) - 2))
      
    # For each car in the list, print its details in a new row of the table
    for i, car in enumerate(car_list, start=1):
        # Convert the dates to strings in the 'YYYY-MM-DD' format
        insurance_expiry = car.insurance_expiry.strftime('%Y-%m-%d')
        road_tax_expiry = car.road_tax_expiry.strftime('%Y-%m-%d')
        last_service_date = car.last_service_date.strftime('%Y-%m-%d')
        
        # Print the car's details
        print(f"|{i:^5}|{car.registration_no:^20}|{car.manufacturer:^15}|{car.model:^15}|{last_service_date:^20}|{car.insurance_policy_number:^20}|{insurance_expiry:^20}|{road_tax_expiry:^20}|{car.availability:^15}|")
    
    # Return the list of cars
    return car_list

def viewRentedCars() -> None:
  # Checking if any car fits the criteria
  if any(map(lambda car:car.availability == 'Rented',Car.getCarList())):

    # Header
    print()
    header = f"|{'Plate No.':^20}|{'Manufacturer':^15}|{'Model':^15}|{'Manufacture Year':^20}|{'Capacity':^20}|{'Last Service Date':^20}|{'Insurance No.':^20}|{'Insurance Exp. Date':^20}|{'Road Tax Exp. Date':^20}|{'Rental Rate':^20}|{'Availability':^15}|{'Return Date':^15}|"
    print('Car Record'.center(len(header)),'\n','-' * (len(header)-2))
    print(header,'\n','-' * (len(header) - 2))
        
    # Car Info
    for car in Car.getCarList():
      if car.availability == 'Rented':

        # Get car return day
        returnDate = datetime.today()
        for rental in Rental.getRentalList():
          if rental.car == car and rental.return_date > returnDate:
            returnDate = rental.return_date
      
        print(f"{car}{returnDate.strftime('%Y-%m-%d'):^15}|")

    # Footer
    print(f' {"-" * (len(header) - 2)} ')
        
  else:
    print('\nNo car record found!\n')

def update_carRecord() -> None:
  
  # Define the options for updating the car record
  options = {
    '1': 'Insurance Policy Number',
    '2': 'Insurance Expiry Date',
    '3': 'Road Tax Expiry Date',
    '4': 'Availability',
    '5': 'Exit'
  }
  
  # Print the options to the user
  print('\nWhich record would you like to update?')
  for key, value in options.items():
    print(f'{key}. {value}')
  
  # Get the user's choice
  option = getValidInput('\nYour choice: ',
                        (lambda enteredInput:enteredInput in options, '\nInvalid option! Please enter a number from 1 to 5.'),
                        (lambda enteredInput:enteredInput != '', '\nInput cannot be empty'))
  
  # If the user chose to exit, return immediately
  if option == '5':
    return
  
  # Display the simplified car list and get the list of cars
  car_list = displaySimplifiedCarList()
  if not car_list:
    return

  # Additional input check for updating rental availability
  if option == '4':
    availabilityCheck = lambda carIndex:car_list[int(carIndex) - 1].availability in ('Available','Under service','Disposed')
  else:
    availabilityCheck = lambda enteredInput:True

  # Get the index of the car to update from the user
  car_index = getValidInput("\nEnter the number of the car you want to update: ",
                            (lambda enteredInput:enteredInput.isdigit() and 1 <= int(enteredInput) <= len(car_list), '\nInvalid option! Please enter a valid car number.'),
                            (availabilityCheck,'\nCar is currently in use!'))
  
  # Get the car to update
  car = car_list[int(car_index) - 1]
  
  # Depending on the user's choice, update the corresponding attribute of the car
  match option:
    case '1':
      # Update the insurance policy number
      car.insurance_policy_number = getValidInput('\n-> New Insurance Policy Number: ', 
                                        (lambda enteredInput:enteredInput != '', '\nInput cannot be empty!'),
                                        (lambda enteredInput:8 <= len(enteredInput) <= 13, '\nInsurance policy number must be 8-13 characters long'),
                                        (str.isalnum, '\nInsurance policy number must contain only alphanumeric characters')).upper()
    case '2':
      # Update the insurance expiry date
      car.insurance_expiry = datetime.strptime(getValidInput('\n-> New Insurance Expiry Date(YYYY-MM_DD): ', 
                                        (lambda enteredInput:enteredInput != '', '\nInsurance expiry date cannot be empty'),
                                        (validDate,'\nMust be in date format'),
                                        (lambda date:datetime.strptime(date, '%Y-%m-%d') >= datetime.now(),'\nPlease make sure the insurance is the latest'),
                                        (lambda date:datetime.strptime(date, '%Y-%m-%d') >= car.insurance_expiry,'\nDate must not be earlier than the previous expiry date')), '%Y-%m-%d')
    case '3':
      # Update the road tax expiry date
      car.road_tax_expiry = datetime.strptime(getValidInput('\n-> New Road Tax Expiry Date(YYYY-MM_DD): ', 
                                        (lambda enteredInput:enteredInput != '', '\nRoad tax expiry date cannot be empty'),
                                        (validDate,'\nMust be in date format'),
                                        (lambda date:datetime.strptime(date, '%Y-%m-%d') >= datetime.now(),'\nPlease make sure the road tax is the latest'),
                                        (lambda date:datetime.strptime(date, '%Y-%m-%d').year <= datetime.now().year + 1,'\nRoad tax expiry date cannot be more than one year from the current date'),
                                        (lambda date:datetime.strptime(date, '%Y-%m-%d') >= car.road_tax_expiry,'\nDate must not be earlier than the previous expiry date')), '%Y-%m-%d')
    case '4':
      # Update the rental availability
      availability_options = {
        '1': 'Available',
        '2': 'Under service',
        '3': 'Disposed'
      }
      
      print('\nChange the availability to:')
      for key, value in availability_options.items():
        print(f'{key}. {value}')
      availability = getValidInput('\n-> Your choice: ',
                                  (lambda enteredInput:enteredInput in availability_options, '\nInvalid option! Please enter a number from 1 to 3.'),
                                  (lambda enteredInput:enteredInput != '', '\nInput cannot be empty'))
      
      if availability == '1' and car.availability == 'Under service':
        car.last_service_date = datetime.today()
      car.availability = availability_options[availability]

  # Update the car record
  Car.updateRecord()
  print('\nUpdate has done')

  

def delete_CarRecord() -> None:
    # Start an infinite loop
    while True:
        # Filter out all cars that are disposed
        disposed_cars = list(filter(lambda car: car.availability == 'Disposed', Car.getCarList()))
        
        # If there are no disposed cars, print a message and break the loop
        if not disposed_cars:
            print("There are none of the car to be <Disposed> already.")
            break
        
        # Display all disposed cars
        viewCar(lambda car: car.availability == 'Disposed')
        
        # Ask the user if they want to remove any disposed car
        if getValidInput('\nWould you like to remove any car that is disposed? (Y/N): ', 
                         (lambda enteredInput: enteredInput != '' and enteredInput.upper() in ('Y', 'N'), 'Insert cannot be empty or must be Y/N')).upper() != 'Y':
            break
          
        print("\nWhich car would you like to delete?")
        
        # Display all disposed cars with an index
        for i, car in enumerate(disposed_cars, start=1):
            print(f"{i}. {car.registration_no}")
        print(f"{len(disposed_cars) + 1}. All")
        
        # Get the user's choice of car to delete
        deleteChoice = getValidInput('Enter your choice: ',
                                     (lambda enteredInput: enteredInput.isdigit() and 1 <= int(enteredInput) <= len(disposed_cars) + 1, 'Invalid choice. Please enter a number from the list.'))
        
        # If the user chooses to delete all cars
        if deleteChoice == str(len(disposed_cars) + 1):
            for car in disposed_cars:
                car.delete()
            print("All disposed cars have been removed.")
        else:
            # If the user chooses to delete a specific car
            car_to_delete = disposed_cars[int(deleteChoice) - 1]
            car_to_delete.delete()
            print(f'Car <{car_to_delete.registration_no}> has been removed')
        
        # Update the car record
        Car.updateRecord()



def carMenu(user:Staff) -> None:
  while True:
    # Menu selection
    print('1.\tUpdate own profile')
    print('2.\tRegister new car')
    print('3.\tView registered cars')
    print('4.\tView available cars')
    print('5.\tView rented cars')
    print('6.\tUpdate existing car record')
    print('7.\tDelete car record')
    print('8.\tExit program')
  
    # Determining operation
    operation = getValidInput('\nEnter operation number: ',(lambda enteredInput:enteredInput in ('1','2','3','4','5','6','7','8'),'\nInvalid operation number!'))
    match operation:
      case '1':
        updateProfile(user)

      case '2':
        registerCar()

      case '3':
        viewCar()

      case '4':
        viewCar(lambda car:car.availability == 'Available')

      case '5':
        viewRentedCars()

      case '6':
        update_carRecord()

      case '7':
        delete_CarRecord()

      case '8':
        return

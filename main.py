from DataStructures import *
from function import *
from managerMenu import *
from customer1Menu import *
from customer2Menu import *
from carMenu import *

if __name__ == '__main__':
  
  Staff.readRecord()
  Customer.readRecord()
  Car.readRecord()
  Rental.readRecord()

  # Automatically updates car availability
  for rental in Rental.getRentalList():
    if rental.rental_date <= datetime.today() <= rental.return_date:
      if rental.status == 'Paid':
        rental.car.availability = 'Rented'
      else:
        # Cancel transaction if customer haven't pay before rental date
        rental.car.availability = 'Available'
        rental.delete()
    elif rental.return_date <= datetime.today():
      if rental.car.availability == 'Rented':
        rental.car.availability = 'Available'
  Rental.updateRecord()

  user = login()

  print(f'\nWelcome, {user.name}\n')
  match user.role:
    case 'Manager':
      managerMenu(user)
    case 'Customer Service Staff I':
      customer1Menu(user)
    case 'Customer Service Staff II':
      customer2Menu(user)
    case 'Car Service Staff':
      carMenu(user)
    case _:
      print('An error has occured. Please contact a manager.')

  Staff.updateRecord()
  Customer.updateRecord()
  Car.updateRecord()
  Rental.updateRecord()
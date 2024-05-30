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
  toDeleteList:list[Rental] = []
  for rental in Rental.getRentalList():
    if rental.rental_date <= datetime.today():
      if (rental.status == 'Paid') & (datetime.today() < rental.return_date):
        # Update car availability to rented during rental period if customer has paid for the rental
        rental.car.availability = 'Rented'
      
      elif rental.status == 'Pending':
        # Cancel transaction if customer haven't pay before rental date
        rental.car.availability = 'Available'
        toDeleteList.append(rental)
    
    elif rental.return_date <= datetime.today():
      # Update car availability to available on and after return date
      if rental.car.availability == 'Rented':
        rental.car.availability = 'Available'
  # Delete cancelled transactions
  toDeleteList = list(map(Rental.delete,toDeleteList))
  
  Car.updateRecord()
  Rental.updateRecord()

  user = login()

  print(f'\nWelcome, {user.name}\n')

  # Menu page based on user role
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
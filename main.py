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
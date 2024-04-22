from DataStructures import *
from function import *

def customer2Menu(user:Staff):
  # may subject to change because it is kinda unclear what is expected from the program here
  while True:
    print('1.\tUpdate own profile')
    print('2.\tRecord new rental request')
    print('3.\tGenerate bill')
    print('4.\tView rental transactions')
    print('5.\tDelete rental record')
    print('6.\tExit program')
    while (operation := input('\nEnter operation number: ')) not in ('1','2','3','4','5','6'):
      print('\nInvalid operation number!')
    match operation:
      case '1':
        updateStaff(user)

      case '2':
        pass

      case '3':
        pass

      case '4':
        pass

      case '5':
        pass

      case '6':
        return
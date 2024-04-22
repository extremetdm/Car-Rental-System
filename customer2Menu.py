from DataStructures import *
from function import *

def customer2Menu(user:Staff):
  # may subject to change because it is kinda unclear what is expected from the program here
  while True:
    print('1.\tUpdate own profile')
    print('2.\tCheck car availability')
    print('3.\tRecord new rental request')
    print('4.\tGenerate bill')
    print('5.\tView rental transactions')
    print('6.\tDelete rental record')
    print('7.\tExit program')
    while (operation := input('\nEnter operation number: ')) not in ('1','2','3','4','5','6','7'):
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
        pass

      case '7':
        return
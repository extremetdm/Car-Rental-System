"""code from chatgpt"""


from datetime import datetime

class Staff:
    
    StaffList = {}

    def __init__(self, id, name, role, password, date_of_register,status):
        self.id = id
        self.name = name
        if role in ['Manager','Customer Service Staff I','Customer Service Staff II']:
            self.role = role
        else:
            self.role = 'N/A'
        self.password = password
        self.date_of_register = date_of_register
        self.status = status
        __class__.StaffList[id] = self

    def login(username, password):
        if username in __class__.StaffList:
            staff = __class__.StaffList[username]
            if password == staff.password:
                return staff
            else:
                return 'Wrong Password'
        else:
            return 'Invalid StaffID'
        
    def update_staff(self, staff_id, field, new_value):
        if staff_id in self.staff_data:
            self.staff_data[staff_id][field] = new_value

    def view_monthly_revenue(self):
        # This function needs to be implemented based on how you track transactions
        pass

    def update_profile(self, field, new_value):
        setattr(self, field, new_value)


class CustomerServiceStaffI:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_attempts = 0
        self.customers = {}

    def login(self, username, password):
        if self.login_attempts < 3:
            if username == self.username and password == self.password:
                self.login_attempts = 0
                return True
            else:
                self.login_attempts += 1
                return False
        else:
            return "Login attempts exceeded."

    def register_customer(self, customer_id, name, nric, passport_no, license_no, address, phone, registration_date):
        self.customers[customer_id] = {
            'Name': name,
            'NRIC': nric,
            'Passport Number': passport_no,
            'Driving License No': license_no,
            'Contact Address': address,
            'Phone Number': phone,
            'Registration Date': registration_date
        }

    def update_customer_details(self, customer_id, field, new_value):
        if customer_id in self.customers:
            self.customers[customer_id][field] = new_value

    def view_customers(self):
        return self.customers

    def update_profile(self, field, new_value):
        setattr(self, field, new_value)


class CustomerServiceStaffII:
    def __init__(self):
        self.rental_transactions = {}
        self.cars = {}

    def check_car_availability(self, car_reg_no):
        return self.cars.get(car_reg_no, {}).get('Status', 'Not registered')

    def record_rental_details(self, car_reg_no, customer_id, rental_date, return_date):
        rental_period = (datetime.strptime(return_date, '%d %B %Y') - datetime.strptime(rental_date, '%d %B %Y')).days
        total_rental = self.cars[car_reg_no]['Price per day'] * rental_period
        self.rental_transactions[customer_id] = {
            'Car Registration Number': car_reg_no,
            'Car Rental Date': rental_date,
            'Car Returning Date': return_date,
            'Rental Periods (Days)': rental_period,
            'Total Rental': total_rental
        }
        self.update_car_status(car_reg_no, 'Reserved')

    def generate_bill(self, customer_id):
        transaction = self.rental_transactions.get(customer_id)
        if transaction:
            # Implement payment acceptance and receipt generation logic
            self.update_car_status(transaction['Car Registration Number'], 'Rented')
            return transaction['Total Rental']
        return 'No rental found for this customer ID.'

    def update_car_status(self, car_reg_no, status):
        if car_reg_no in self.cars:
            self.cars[car_reg_no]['Status'] = status

    def view_rental_transactions(self, date):
        transactions_on_date = {k: v for k, v in self.rental_transactions.items() if v['Car Rental Date'] == date}
        return transactions_on_date


class CarServiceStaff:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_attempts = 0
        self.cars = {}

    def login(self, username, password):
        if self.login_attempts < 3:
            if username == self.username and password == self.password:
                self.login_attempts = 0
                return True
            else:
                self.login_attempts += 1
                return False
        else:
            return "Login attempts exceeded."

    def register_car(self, reg_no, manufacturer, model, year, seating_capacity, service_date, insurance_policy, insurance_expiry, road_tax_expiry, rate_per_day):
        self.cars[reg_no] = {
            'Manufacturer': manufacturer,
            'Model': model,
            'Year of Manufacturer': year,
            'Seating Capacity': seating_capacity,
            'Last Service Date': service_date,
            'Insurance Policy Number': insurance_policy,
            'Insurance Expiry Date': insurance_expiry,
            'Road Tax Expiry Date': road_tax_expiry,
            'Renting Rate per Day': rate_per_day,
            'Rental Availability': 'Available'
        }

    def update_car_details(self, reg_no, field, new_value):
        if reg_no in self.cars:
            self.cars[reg_no][field] = new_value

    def view_registered_cars(self):
        return self.cars

    def update_profile(self, field, new_value):
        setattr(self, field, new_value)

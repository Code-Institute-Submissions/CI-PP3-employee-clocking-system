import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('employee_clocking_system')

in_out_sheet = SHEET.worksheet('in_out_sheet')

data = in_out_sheet.get_all_values()

employeeList = [ {
    "employeeNumber": 111,
    "name": "John Doe",
    "hourlyRate": "10.00"
    },
    {
    "employeeNumber": 112,
    "name": "Jane Doe",
    "hourlyRate": "11.00"
    }
]

#Employee Validation

def list_of_employees_numbers():
    """
    Itterates throught employees numbers.
    """
    all_employees_numbers = [num["employeeNumber"] for num in employeeList if "employeeNumber" in num]
    return all_employees_numbers


def employee_input():
    """
    Takes user input (Employee number)
    """
    employee_number = input("Please enter you employee number: ")
    return int(employee_number)
        

def find_employee_details():
    """
    Takes return value from employee_input()
    Then checks it against employeeNumber in employeeList
    """
    all_employees_numbers = list_of_employees_numbers()
    entered_number_by_employee = employee_input()
    for i in all_employees_numbers:
        print("This is entered_number_by_employee: ", entered_number_by_employee)
        if entered_number_by_employee is i:
            print(f" {entered_number_by_employee} is = {i} \n")
            return i
        else:
            print("is not = \n")

#Update Google Sheets

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("in_out_sheet")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")

def transfer_of_data():
    """
    Takes data in and formats to list.
    Updates csv file
    """
    data = find_employee_details()
    csv_result = [data]
    update_sales_worksheet(csv_result)

def main():
    transfer_of_data()
    
main()
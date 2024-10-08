# Import the entire gspread libraries and the Credentials
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDENTIALS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDENTIALS = CREDENTIALS.with_scopes(SCOPE)
GSPREAD_CLIENTS = gspread.authorize(SCOPED_CREDENTIALS)
SHEET = GSPREAD_CLIENTS.open('kfc_data_automation')

def get_sales_data():
    """
    Collect the sales data from the user
    """
    print('Enter sales data from the last business day: ')
    print('The data should be 13 and separated by comma. ')

    data_string = input('Enter your data: ')
    #print(f'The data provided is: {data_string}')
    sales_data = data_string.split(',') #Remove commas from the string
    validate_data(sales_data)


def validate_data(values):
    """
    Convert the string to integers, raise valueerror if the string 
    cannot be converted into integers and if the values are not equal to 13
    exactly.
    """  
    try:
        if len(values) != 13:
            raise ValueError(
                f'13 values required, provided values is {len(values)}'
            )
    except ValueError as ve:
        print(f'Invalid data: {ve}, Put 13 values.\n')        

get_sales_data()
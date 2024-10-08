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
    print(f'The data provided is: {data_string}')
    sales_data = data_string.split(',') #Remove commas from the string

get_sales_data()
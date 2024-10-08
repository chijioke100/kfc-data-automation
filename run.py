# Import the entire gspread libraries and the Credentials
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Collect the sales data from the user and 
    request for data until when valid.
    """
    while True: #To request for data until is valid
        print('Enter sales data from the last business day: ')
        print('The data should be 13 and separated by comma. ')

        data_string = input('Enter your data: ')
   
        sales_data = data_string.split(',') #Remove commas from the string
        

        if validate_data(sales_data):
            print('Data is valid')
            break
    return sales_data

def validate_data(values):
    """
    Convert the string to integers, raise valueerror if the string 
    cannot be converted into integers and if the values are not equal to 13
    exactly.
    """  
    try:
        [int(value) for value in values] #Convert the values to integers
        if len(values) != 13:
            raise ValueError(
                f'13 values required, provided values is {len(values)}'
            )
    except ValueError as ve:
        print(f'Invalid data: {ve}, Put 13 values.\n')
        return False

    return True      

def update_sales_worksheet(data):
    """
    Add in to our sales worksheet with the data provided.
    """
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('New sales worksheet added. \n')

def calculate_excess_data(sales_row):
    """
    Function to calculate the excess bewteen the sales and goods;
    where excess is the difference between sales from goods.
    """    
    print('Calculate excess data \n')
    goods = SHEET.worksheet('goods').get_all_values()
    goods_row = goods[-1] #Using list slicing and indexing to get the goods last row data
    #pprint(goods_row) #Using pprint makes it easier to read

    excess_data = []
    for goods, sales in zip(goods_row, sales_row):
        excess = int(goods) - sales
        excess_data.append(excess)
    print(excess_data)    


def all_functions():
    """
    Function to run all the programs.
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_excess_data(sales_data)

print('Welcome! This is KFC Data Automation')
all_functions()   
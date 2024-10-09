# Import the entire gspread libraries and the Credentials
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
SHEET = GSPREAD_CLIENT.open('kfc_data_automation')

def get_sales_data():
    """
    Collect the sales data from the user and 
    request for data until when valid.
    """
    while True: #To request for data until is valid
        print('Enter sales data from the last business day: ')
        print('The data should be 13 and each separated by a comma. ')

        data_string = input('Enter your data:\n')
   
        sales_data = data_string.split(',') #Remove commas from the string
        

        if validate_data(sales_data):
            print('Data is valid.')
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

def update_worksheet(data, worksheet): 
    """
    Receive and update the sales and excess
    worksheet with the data.
    """
    print(f'Updating {worksheet} worksheet. \n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet.capitalize()} worksheet added \n')



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

    return excess_data

def get_last_7_data():
    """
    Get the column list of sales worksheet and and 
    collect the 7 days(everyday in a week) data entries
    """
    sales = SHEET.worksheet('sales')
   
    columns = []
    for indexes in range(1, 14):
        column = sales.col_values(indexes)
        columns.append(column[-7:])
    
    return columns

def calculate_goods_data(data):
    """
    Calculate the average of goods 
    data and add 5% profit 
    """    
    print('Calculating goods data \n')
    new_goods_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        goods_num = average * 1.05
        new_goods_data.append(int(goods_num))

    return new_goods_data



def all_functions():
    """
    Function to run all the programs.
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'sales')
    new_excess_data = calculate_excess_data(sales_data)
    update_worksheet(new_excess_data, 'excess')
    sales_columns = get_last_7_data()
    goods_data = calculate_goods_data(sales_columns)
    update_worksheet(goods_data, 'goods')
    
print('Welcome! This is KFC Data Automation')
all_functions()   

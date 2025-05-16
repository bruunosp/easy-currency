from tkinter import *
import requests

# need to def a function to call it later


def requisition_currency():
    # Give the API site to get the requisition currency
    requisition = requests.get(
        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    # get a json
    requisition_dic = requisition.json()

    # create variables to save information about the currency you want to see
    price_dollar = requisition_dic['USDBRL']['bid']
    price_euro = requisition_dic['EURBRL']['bid']
    price_bitcoin = requisition_dic['BTCBRL']['bid']

    # text how you need to see the information about currency requisition
    text = (f'''The price BRL in USD is: R${price_dollar} 
    The price EUR in BRL is: R${price_euro}
    The price BTC in BRL is: R${price_bitcoin}''')

    # edit text from the variable to show in window
    currency_price['text'] = text


# CREATE A WINDOW THAT YOU CAN UPDATE THE CURRENCY REQUISITION IN REAL TIME
# from tkinter importe everything that exist

# create a window function
window = Tk()

# title for window
window.title('Requesition Currency Actual')
# choose the size of window
# window.geometry('400x400')

# give a first text to user for he knows what he needs to do
text_orientation = Label(
    window, text='Click on the bottom bellow to update with recently currency requisition')
text_orientation.grid(column=0, row=0)

# create a bottom to run the requisition_currency
click_bottom = Button(window, text='Refresh', command=requisition_currency)
click_bottom.grid(column=0, rows=1)

# shows the text you create in requisition_currency with the actual currency requisition
currency_price = Label(window, text='')
currency_price.grid(column=0, rows=2)

# make a loop for window not close
window.mainloop()

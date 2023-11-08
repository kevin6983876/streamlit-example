import numpy as np
import pandas as pd
import streamlit as st
import datetime

"""
# SIMOA consumable inventory
"""
report_issue = st.button('Report an issue')
if report_issue:
    username = st.selectbox('User',('Matthew', 'Lizzie', 
    'Trevor', 'Jeff', 'Emre', 'Dorothea', 'Ron', 'Florence'))
    message = st.text_input('message',value='')
    error = pd.read_csv('error.csv')
    current_datetime = datetime.datetime.now()
    new_row = {"Name":username, "Time":str(current_datetime),"message":message}
    new_error_message = pd.DataFrame([new_row],index=[3])
    error = pd.concat([error, new_error_message], ignore_index=True)
    error.to_csv('error.csv', index=False)
view_previous_message = st.button('View previous message')
if view_previous_message:
    error = pd.read_csv('error.csv')
    st.dataframe(error)
operation = st.selectbox('Operation',('Experiment', 'Purchase', 'Check stock'))
username = st.selectbox('User',('Matthew', 'Lizzie', 
'Trevor', 'Jeff', 'Emre', 'Dorothea', 'Ron', 'Florence'))
st.write('---')

# exp_purchase = pd.read_csv('exp_purchase.csv')
stock = pd.read_csv('stock.csv')
if operation == 'Experiment':
    sample = st.number_input('Sample/Detector Diluent (ml)', 0)/250                                      
    bead = st.number_input('Bead diluent (ml)', 0)/100
    SBG_diluent = st.number_input('SBG diluent (ml)',0)/100
    SBG_concentrate = st.number_input(r'SBG concentrate ($\mu$l)',0)/1000
    disc = st.number_input('Disc',0)/16
    plate = st.number_input('Plate',0)
    RGP = st.number_input('RGP (bottle)', 0)
    wash_buffer_A = st.number_input('Wash buffer A (pack)',0)
    wash_buffer_B = st.number_input('Wash buffer B (pack)',0)
    submit = st.button('submit')
    if submit:
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()
        new_row = {"Date":str(current_date), "Time":str(current_time),
                   "User":username,"Operation":'Exp',
                    "Sample/Detector Diluent (bottles)":sample,
                    'Bead diluent (bottles)':bead,
                    'SBG diluent (bottles)':SBG_diluent ,
                    'SBG concentrate (vials)':SBG_concentrate,
                    'Disc (packs of 16)':disc,
                    'Plate':plate, 'RGP (bottles)': RGP, 
                    'Wash buffer A (pack)': wash_buffer_A,
                    'Wash buffer B (pack)': wash_buffer_B}
        exp = pd.DataFrame([new_row],index=[13])
        stock_tmp = pd.concat([stock, exp], ignore_index=True)
        last_stock = stock.tail(1)
        last_stock_array = last_stock.to_numpy()
        exp_array = exp.to_numpy()
        new_stock = last_stock_array[0,4:]-exp_array[0,4:]
        new_stock_list = new_stock.tolist()
        new_stock = np.array([[str(current_date),str(current_time),username,'Stock']+new_stock_list])
        new_stock_series = pd.DataFrame(new_stock, columns=exp.columns)
        stock = pd.concat([stock_tmp, new_stock_series], ignore_index=True)
        st.dataframe(stock)
        stock.to_csv('stock.csv', index=False)
if operation == 'Purchase':
    sample = st.number_input('Sample/Detector Diluent (bottles)', 0)                                      
    bead = st.number_input('Bead diluent (bottles)', 0)
    SBG_diluent = st.number_input('SBG diluent (bottles)',0)
    SBG_concentrate = st.number_input(r'SBG concentrate (vials)',0)
    disc = st.number_input('Disc (pack of 16)',0)
    plate = st.number_input('Plate',0)
    RGP = st.number_input('RGP (bottle)', 0)
    wash_buffer_A = st.number_input('Wash buffer A (pack)',0)
    wash_buffer_B = st.number_input('Wash buffer B (pack)',0)
    submit = st.button('submit')
    if submit:
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()
        new_row = {"Date":str(current_date), "Time":str(current_time),
                   "User":username,"Operation":'Purchase',
                    "Sample/Detector Diluent (bottles)":sample,
                    'Bead diluent (bottles)':bead,
                    'SBG diluent (bottles)':SBG_diluent ,
                    'SBG concentrate (vials)':SBG_concentrate,
                    'Disc (packs of 16)':disc,
                    'Plate':plate, 'RGP (bottles)': RGP, 
                    'Wash buffer A (pack)': wash_buffer_A,
                    'Wash buffer B (pack)': wash_buffer_B}
        purchase = pd.DataFrame([new_row],index=[13])
        stock_tmp = pd.concat([stock, purchase], ignore_index=True)
        last_stock = stock.tail(1)
        last_stock_array = last_stock.to_numpy()
        purchase_array = purchase.to_numpy()
        new_stock = last_stock_array[0,4:]+purchase_array[0,4:]
        new_stock_list = new_stock.tolist()
        new_stock = np.array([[str(current_date),str(current_time),username,'Stock']+new_stock_list])
        new_stock_series = pd.DataFrame(new_stock, columns=purchase.columns)
        stock = pd.concat([stock_tmp, new_stock_series], ignore_index=True)
        st.dataframe(stock)
        stock.to_csv('stock.csv', index=False)
if operation == 'Check stock':
    sample = st.number_input('Sample/Detector Diluent (bottles)', 0.0)                                      
    bead = st.number_input('Bead diluent (bottles)', 0.0)
    SBG_diluent = st.number_input('SBG diluent (bottles)',0.0)
    SBG_concentrate = st.number_input(r'SBG concentrate (vials)',0.0)
    disc = st.number_input('Disc (pack of 16)',0)
    plate = st.number_input('Plate',0)
    RGP = st.number_input('RGP (bottle)', 0)
    wash_buffer_A = st.number_input('Wash buffer A (pack)',0)
    wash_buffer_B = st.number_input('Wash buffer B (pack)',0)
    submit = st.button('submit')
    if submit:
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()
        new_row = {"Date":str(current_date), "Time":str(current_time),
                   "User":username,"Operation":'Stock',
                    "Sample/Detector Diluent (bottles)":sample,
                    'Bead diluent (bottles)':bead,
                    'SBG diluent (bottles)':SBG_diluent ,
                    'SBG concentrate (vials)':SBG_concentrate,
                    'Disc (packs of 16)':disc,
                    'Plate':plate, 'RGP (bottles)': RGP, 
                    'Wash buffer A (pack)': wash_buffer_A,
                    'Wash buffer B (pack)': wash_buffer_B}
        new_stock = pd.DataFrame([new_row],index=[13])
        stock = pd.concat([stock, new_stock], ignore_index=True)
        st.dataframe(stock)
        stock.to_csv('stock.csv', index=False)
last_stock = stock.tail(1)
if np.float32(last_stock["Sample/Detector Diluent (bottles)"])<2.5:
    st.write('### WARNING: Sample/Detector Diluent (bottles) is running low!')
if np.float32(last_stock["Bead diluent (bottles)"])<2:
    st.write('### WARNING: Bead diluent (bottles) is running low!')
if np.float32(last_stock["SBG diluent (bottles)"])<3:
    st.write('### WARNING: SBG diluent (bottles) is running low!')
if np.float32(last_stock["SBG concentrate (vials)"])<1:
    st.write('### WARNING: SBG concentrate (vials) is running low!')
if np.float32(last_stock["Disc (packs of 16)"])<5:
    st.write('### WARNING: Disc (packs of 16) is running low!')
if np.float32(last_stock["Plate"])<30:
    st.write('### WARNING: Plate is running low!')
if np.float32(last_stock["RGP (bottles)"])<20:
    st.write('### WARNING: RGP (bottles) is running low!')
if np.float32(last_stock["Wash buffer A (pack)"])<10:
    st.write('### WARNING: Wash buffer A (pack) is running low!')
if np.float32(last_stock["Wash buffer B (pack)"])<6:
    st.write('### WARNING: Wash buffer B (pack) is running low!')
st.write('---')
view_stock = st.button('### View current stock')
if view_stock:
    last_stock = stock.tail(1)
    st.dataframe(last_stock)

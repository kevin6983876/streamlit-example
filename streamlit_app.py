import numpy as np
import pandas as pd
import streamlit as st
import datetime

"""
# SIMOA consumable inventory
"""
operation = st.selectbox('Operation',('Experiment', 'Purchase', 'Check stock'))
user = st.selectbox('Username',('Matthew','Lizzie','Trevor',
'Jeff', 'Emre', 'Dorothea','Ron','Florence'))
st.write('---')
stock = pd.read_csv('stock.csv')
if operation == 'Experiment':
    sample = st.number_input('Sample/Detector Diluent (ml)', 0)/250                                      
    bead = st.number_input('Bead diluent (ml)', 0)/100
    SBG_diluent = st.number_input('SBG diluent (ml)',0)/100
    SBG_concentrate = st.number_input(r'SBG concentrate ($\mu$l)',0)/1000
    disc = st.number_input('Disc',0)
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
                   "Operation":'Exp',
                    "Sample/Detector Diluent (bottles)":sample,
                    'Bead diluent (bottles)':bead,
                    'SBG diluent (bottles)':SBG_diluent ,
                    'SBG concentrate (vials)':SBG_concentrate,
                    'Disc (packs of 16)':disc,
                    'Plate':plate, 'RGP (bottles)': RGP, 
                    'Wash buffer A (pack)': wash_buffer_A,
                    'Wash buffer B (pack)': wash_buffer_B}
        exp = pd.DataFrame([new_row],index=[12])
        stock_tmp = pd.concat([stock, exp], ignore_index=True)
        last_stock = stock.tail(1)
        last_stock_array = last_stock.to_numpy()
        exp_array = exp.to_numpy()
        new_stock = last_stock_array[0,3:]-exp_array[0,3:]
        new_stock_list = new_stock.tolist()
        new_stock = np.array([[str(current_date),str(current_time),'Stock']+new_stock_list])
        new_stock_series = pd.DataFrame(new_stock, columns=exp.columns)
        stock = pd.concat([stock_tmp, new_stock_series], ignore_index=True)
        st.dataframe(stock)
        stock.to_csv('stock.csv', index=False)
if operation == 'Purchase':
    sample = st.number_input('Sample/Detector Diluent (bottles)', 0)                                      
    bead = st.number_input('Bead diluent (bottles)', 0)
    SBG_diluent = st.number_input('SBG diluent (bottles)',0)
    SBG_concentrate = st.number_input(r'SBG concentrate (vials)',0)
    disc = st.number_input('Disc',0)
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
                   "Operation":'Purchase',
                    "Sample/Detector Diluent (bottles)":sample,
                    'Bead diluent (bottles)':bead,
                    'SBG diluent (bottles)':SBG_diluent ,
                    'SBG concentrate (vials)':SBG_concentrate,
                    'Disc (packs of 16)':disc,
                    'Plate':plate, 'RGP (bottles)': RGP, 
                    'Wash buffer A (pack)': wash_buffer_A,
                    'Wash buffer B (pack)': wash_buffer_B}
        purchase = pd.DataFrame([new_row],index=[12])
        stock_tmp = pd.concat([stock, purchase], ignore_index=True)
        last_stock = stock.tail(1)
        last_stock_array = last_stock.to_numpy()
        purchase_array = purchase.to_numpy()
        new_stock = last_stock_array[0,3:]+purchase_array[0,3:]
        new_stock_list = new_stock.tolist()
        new_stock = np.array([[str(current_date),str(current_time),'Stock']+new_stock_list])
        new_stock_series = pd.DataFrame(new_stock, columns=purchase.columns)
        stock = pd.concat([stock_tmp, new_stock_series], ignore_index=True)
        st.dataframe(stock)
        stock.to_csv('stock.csv', index=False)
if operation == 'Check stock':
    sample = st.number_input('Sample/Detector Diluent (bottles)', 0.0)                                      
    bead = st.number_input('Bead diluent (bottles)', 0.0)
    SBG_diluent = st.number_input('SBG diluent (bottles)',0.0)
    SBG_concentrate = st.number_input(r'SBG concentrate (vials)',0.0)
    disc = st.number_input('Disc',0)
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
                   "Operation":'Stock',
                    "Sample/Detector Diluent (bottles)":sample,
                    'Bead diluent (bottles)':bead,
                    'SBG diluent (bottles)':SBG_diluent ,
                    'SBG concentrate (vials)':SBG_concentrate,
                    'Disc (packs of 16)':disc,
                    'Plate':plate, 'RGP (bottles)': RGP, 
                    'Wash buffer A (pack)': wash_buffer_A,
                    'Wash buffer B (pack)': wash_buffer_B}
        new_stock = pd.DataFrame([new_row],index=[12])
        stock = pd.concat([stock, new_stock], ignore_index=True)
        st.dataframe(stock)
        stock.to_csv('stock.csv', index=False)
st.write('### View stock')
st.dataframe(stock)

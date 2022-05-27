from regex import P
import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

date = st.date_input(
     "Pick-up date:",
     datetime.date.today())

time = st.time_input(
     "Pick-up hour:",
    datetime.datetime.now())

date_and_time=datetime. datetime. combine(date, time)

pickup_lon = st.number_input('Pick-up longitude :', -74.00597)
pickup_lat = st.number_input('Pick-up latitude :', 40.71427)

dropoff_lon = st.number_input('Drop-off longitude :', -74.0156334)
dropoff_lat = st.number_input('Drop-off latitude :', 40.7055689)

passenger_count=st.number_input('Nombre de passager :',1)

url = 'https://api-5vvrxbd5cq-ew.a.run.app//predict'

'''
## One click away from the best taxi experience
'''

if st.button('Check rate'):
    # print is visible in the server output, not in the page
    print('Powering the best API ever ...')

    params={
            'key':'predict key',
            'pickup_datetime':date_and_time,
            'pickup_longitude':pickup_lon,
            'pickup_latitude':pickup_lat,
            'dropoff_longitude':dropoff_lon,
            'dropoff_latitude':dropoff_lat,
            'passenger_count':passenger_count
            }

    st.write('Wait fort it 🎉')

    api_data = requests.get(url,params)
    rate=round(float(api_data.json()['fare']),2)

    st.info(f"Le tarif de la course sera de {rate} fucking dollars.")

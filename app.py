import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Flight Fare Predictor")
Airline = st.selectbox('Airline',df['Airline'].unique())
Source=st.selectbox('Source',df['Source'].unique())
Destination = st.selectbox('Destination',df['Destination'].unique())
Total_Stops=st.selectbox('Total_Stops',df['Total_Stops'].unique())
Additional_Info = st.selectbox('Additional_Info',df['Additional_Info'].unique())
day=st.selectbox('Day',df['day'].unique())
month = st.selectbox('Month',df['month'].unique())
Dep_time_hr=st.selectbox('Dep_time_hr',df['Dep_time_hr'].unique())
Dep_time_min=st.selectbox('Dep_time_min',df['Dep_time_min'].unique())
Arr_time_hr = st.selectbox('Arr_time_hr',df['Arr_time_hr'].unique())
Arr_time_min=st.selectbox('Arr_time_min',df['Arr_time_min'].unique())
Duration_bool=st.selectbox('Duration_bool',df['Duration_bool'].unique())
query=np.array([Airline,Source,Destination,Total_Stops,Additional_Info,day,month,Dep_time_hr,Dep_time_min,Arr_time_hr,Arr_time_min,Duration_bool])
query=query.reshape(1,12)
st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))
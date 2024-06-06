import streamlit as st
import pandas as pd
#import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data_daily = pd.read_csv("Apple-daily.csv")
x = data_daily[['Open','High','Low','Volume']]
y = data_daily[['Close']]

x_train , x_test , y_train , y_test = train_test_split( x , y , test_size = 0.2)

model = LinearRegression()
model.fit(x_train , y_train)
pred = model.predict(x_test)

#pickle.dump(model , open("Linear_model.pkl" , "wb"))

st.title("Apple-Stock-Close-Price-Pridiction-Model")
open = float(st.text_input("Open Price : " , "0" , key = "open"))
high = float(st.text_input("Highest Price :" , "0" , key = "high"))
low = float(st.text_input("Low Price :" , "0" , key = "low"))
vol = int(st.text_input("Volume :" , "0" , key = "volume"))
result = ""
if st.button("Predict") :
    result = model.predict([[open , high , low , vol]])
st.text("The Close Price is {}".format(result))
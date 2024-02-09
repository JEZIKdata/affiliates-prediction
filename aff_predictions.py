import streamlit as st
import random
import numpy as np
from PIL import Image
import gc
import os
import logging
import datetime
import warnings
import numpy as np
import pandas as pd
#pipfrom tqdm import tqdm_notebook
import matplotlib.pyplot as plt


#webapp


markets = ["China","USA","United Kingdom","Denmark","Norway","Hong Kong","Finland","Switzerland","Canada","Austria","France",
"Netherlands","New Zealand","Taiwan","Australia","Sweden","Belgium","Germany","Japan","Singapore","Israel","South Korea",
"Portugal","Italy","Greece","Spain","United Arab Emirates","Morocco","Turkey","Chile","Czech Republic","Romania",
"Russia","Uruguay","Poland","Saudi Arabia","Mexico","Lithuania","Hungary","Argentina","Peru","Latvia","India",
"Nigeria","Estonia","Slovakia","Thailand","Brazil","Indonesia","Malaysia","Colombia","Bulgaria","Egypt",
"Ukraine","Vietnam","Philippines","South Africa","Kazakhstan","Kenya", 'World Wide']

#sidebar
st.sidebar.subheader("Select market for which you would like to predict:")
selected_market = st.sidebar.selectbox("", markets)


#main
st.title("Select metrics:")
st.text("            ")
avg_conv = st.slider("Average daily conversions:", 0, 1000, 50)
avg_basket = st.slider("Average basket in EUR:", 0, 2000, 100)
avg_share= st.slider("Expected Average Share in %:", 0, 20, 5)
commission = st.slider("Commission in %:", 0, 100, 10)
st.text("            ")
st.text("            ")

if st.button("Run Prediction"):

    #prediction

    monthly_conversions = avg_conv * 30
    monthly_revenue = avg_basket * monthly_conversions
    blue_sales = avg_conv /100 * avg_share
    blue_revenue = blue_sales * avg_basket
    daily_media_cost = blue_revenue /100 * commission
    monthly_media_cost = daily_media_cost * 30

    dictionary = {
        "China": 199.481481481481,
        "USA": 173.333333333333,
        "United Kingdom": 167.259259259259,
        "Denmark": 151.259259259259,
        "Norway": 126.222222222222,
        "Hong Kong": 122.259259259259,
        "Finland": 120.222222222222,
        "Switzerland": 97.1481481481482,
        "Canada": 83.4444444444444,
        "Austria": 82.6296296296296,
        "France": 79.5185185185185,
        "Netherlands": 77.7037037037037,
        "New Zealand": 73.962962962963,
        "Taiwan": 73.0740740740741,
        "Australia": 71.6666666666667,
        "Sweden": 70.1111111111111,
        "Belgium": 67.7407407407407,
        "Germany": 67.5555555555556,
        "Japan": 61.7037037037037,
        "Singapore": 61.037037037037,
        "Israel": 60.3333333333333,
        "South Korea": 59.4074074074074,
        "Portugal": 57.5925925925926,
        "Italy": 55.9259259259259,
        "Greece": 53.8148148148148,
        "Spain": 53.5925925925926,
        "United Arab Emirates": 48.5185185185185,
        "Morocco": 36.6666666666667,
        "Turkey": 35.5555555555556,
        "Chile": 33.8148148148148,
        "Czech Republic": 32.9259259259259,
        "Romania": 29.7777777777778,
        "Russia": 28.9259259259259,
        "Uruguay": 28.8148148148148,
        "Poland": 23.8888888888889,
        "Saudi Arabia": 22.2962962962963,
        "Mexico": 22.037037037037,
        "Lithuania": 20.3333333333333,
        "Hungary": 19.4444444444444,
        "Argentina": 17.6296296296296,
        "Peru": 17.4814814814815,
        "Latvia": 16.037037037037,
        "India": 15.8518518518519,
        "Nigeria": 15.4444444444444,
        "Estonia": 15.3703703703704,
        "Slovakia": 15.2222222222222,
        "Thailand": 14.962962962963,
        "Brazil": 14.037037037037,
        "Indonesia": 13.3333333333333,
        "Malaysia": 13.037037037037,
        "Colombia": 13,
        "Bulgaria": 12.3703703703704,
        "Egypt": 11.2592592592593,
        "Ukraine": 5.51851851851852,
        "Vietnam": 4.88888888888889,
        "Philippines": 4.14814814814815,
        "South Africa": 3.62962962962963,
        "Kazakhstan": 3.2962962962963,
        "Kenya": 1,
        "World Wide": 50,

    }

    monthly_media_cost_lower = round(monthly_media_cost - random.uniform(10,20),2)
    monthly_media_cost_higher = monthly_media_cost + dictionary[selected_market]
    monthly_media_cost_higher = round(monthly_media_cost_higher,2)

    st.text("            ")

    st.markdown(f"Predicted monthly revenue for **Blue** on {selected_market} market is **{monthly_media_cost_lower}** - **{monthly_media_cost_higher}** €.")

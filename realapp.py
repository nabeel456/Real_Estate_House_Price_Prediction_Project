# import pandas as pd
# import numpy as np
# import pickle
# import streamlit as st
# import random

# sentence=['Are you going to buy the house of your dreams?','Muhammad Nabeel Khan','House Price Prediction']
# new_model = pickle.load(open('rf.pkl', 'rb'))
  
# def welcome():
#     return 'Basic App'
  
# def prediction(val):  
   
#     prediction = new_model.predict(
#         [val])
#     print(prediction)
#     ans = 'NULL'
#     if prediction >= 0.5:
#         ans = 'Exited'
#     else:
#         ans = 'Not Exited'
#     return ans
      

# def main():
#     cols = ['id','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
#     st.markdown("<h1 style='text-align: center;'>House Price Prediction</h1>", unsafe_allow_html=True)
#     st.sidebar.markdown(
#     f"""
#     <div style='display: flex; justify-content: center;'>
#         <img src='Nabeel.jpg' alt='Image' width='150px' height='150px'><img src='your_image_relative_path_here/Nabeel.jpg' alt='Image' width='150px' height='150px'>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
#     st.sidebar.markdown("<h1 style='text-align: center;'>Muhammad Nabeel Khan</h1>", unsafe_allow_html=True)
#     st.sidebar.subheader("This Website is part of my Final Project at FAST IT BootCamp")
    
      
#     html_temp = """
#     <div style ="background-color:blue;padding:13px">
#     <h1 style ="color:black;text-align:center;">Find Out The Latest House Prices in King County</h1>
#     </div>
#     """
      
#     st.markdown(html_temp, unsafe_allow_html = True)
      
#     val = []
#     for x in cols:
#         try:
#             val.append(int(st.text_input(x, "")))
#         except ValueError as v:
#             print(v)

#     result =""

#     if st.button("Predict"):
#         print(val)

#         result = prediction(val)
#     st.success(result)
     
# if __name__=='__main__':
#     main()

import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Load the trained machine learning model
new_model = pickle.load(open('rf.pkl', 'rb'))

# Define a function to display the app title
def welcome():
    return 'House Price Prediction App'

# Define a function to make predictions
def prediction(val):
    prediction = new_model.predict([val])
   
    return str(prediction[0]) + " $"

# Define the main function for your Streamlit app
def main():
    # Define the columns for input data
    cols = ['id','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
    
    # Set the title in the center of the main page
    st.markdown("<h1 style='text-align: center;'>House Price Prediction</h1>", unsafe_allow_html=True)
    
    with st.sidebar:
        # offset = (st.sidebar.width - 150) // 2  # Adjust 150 to your image width

    # Add an empty space to the sidebar to center the image
        st.write("")
        st.write("")

        # Display the image with the calculated offset
        st.image('Nabeel.jpg', width=150, caption="Muhammad Nabeel Khan")


    st.sidebar.subheader("This Website is part of my Final Project at FAST IT BootCamp")
    
    html_temp = """
    <div style ="background-color:lightblue;padding:13px">
    <h1 style ="color:black;text-align:center;">Find Out The Latest House Prices in King County</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Collect user input for prediction
    val = []
    for x in cols:
        try:
            val.append(int(st.text_input(x, "")))
        except ValueError as v:
            print(v)

    result = ""

    # Make a prediction when the "Predict" button is clicked
    if st.button("Predict"):
        result = prediction(val)
    
    # Display the prediction result
    st.success(result)

# Run the Streamlit app
if __name__ == '__main__':
    main()

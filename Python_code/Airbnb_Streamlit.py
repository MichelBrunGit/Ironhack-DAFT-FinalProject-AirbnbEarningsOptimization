# coding: utf-8

#To run Streamlit : Go on Anaconda prompt command and enter ->
# streamlit run C:\Users\Michel\git2\Ironhack-DAFT-FinalProject-AirbnbEarningsOptimization\Python_code\Airbnb_Streamlit.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
from sklearn import datasets
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns
import plotly.graph_objects as go
import warnings
import streamlit as st
from bokeh.plotting import figure
#import squarify
warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")
from PIL import Image

####### Load Dataset #####################

##Exporting File after encoding
from pathlib import Path

#file_csv = Path(__file__).parents[1] / 'bank_loans_clean_with_encoding.csv'

#To put it online:
#anaconda prompt : pipreqs C:\Users\Michel\git2\Ironhack-DAFT-FinalProject-AirbnbEarningsOptimization\Python_code
#requirement.txt file to be put on github (add, commit and push)
#transform local path to online path
#local path
data = pd.read_csv(r"C:\Users\Michel\git2\Ironhack-DAFT-FinalProject-AirbnbEarningsOptimization\Data\detailed_listings_paris_clean.csv")
#online path
#file = pd.read_csv(r"/app/ironhack-daft-project5-data_visualization_and_reporting_in_streamlit/Python/bank_loans_clean_with_encoding.csv")





plt.style.use("dark_background")

for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '#000000'  # very light grey

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#86EAE9'  # bluish dark grey
    
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.serif'] = 'Abramo'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 5
plt.rcParams['axes.labelsize'] = 3
plt.rcParams['axes.titlesize'] = 3
plt.rcParams['xtick.labelsize'] = 3
plt.rcParams['ytick.labelsize'] = 3
plt.rcParams['legend.fontsize'] = 3
plt.rcParams['figure.titlesize'] = 6

col1, col2, col3 = st.columns([1.5,5,1.5])

with col1:
    st.write("")

with col2:
    image1 = Image.open(r"C:\Users\Michel\git2\Ironhack-DAFT-FinalProject-AirbnbEarningsOptimization\Images\airbnb_logo.png")
    st.image(image1, use_column_width=True)
    st.markdown("<h1 style='text-align: center; color: '#000000'>Earnings Optimization in Paris</h1>", unsafe_allow_html=True)
    #st.title("Earnings Optimization in Paris") 
    st.markdown("")
    st.markdown("")

with col3:
    st.write("")

st.markdown("")
st.markdown("")
st.markdown("")
st.header("Description")
st.markdown("This page will allow you to get specific information in order to make the best profit of your place on Airbnb")
st.markdown("It is composed of one bashboard with general information of listings in Paris, price per night prediction of your apartment, listing content advisor and best place recommendation for having a place")

################# SideBar #################

st.sidebar.write("# Filters")
st.sidebar.write("")
st.sidebar.write("Please select information about your listing for price per night prediction")   

st.sidebar.write("")
st.sidebar.write("- About You")

host_since_year = st.sidebar.selectbox("Host since : Year", sorted(data["host_since_year"].unique()),index =5)
host_is_superhost = st.sidebar.checkbox('Superhost')
host_has_profile_pic = st.sidebar.checkbox('Have a Profile Picture',value=True)
host_identity_verified = st.sidebar.checkbox('Identity verified',value=True)
host_listings_count = st.sidebar.selectbox("How many listings do you have :", sorted(data["host_listings_count"].unique()),index=1)
st.sidebar.write("")
st.sidebar.write("- About Your Place")
neighbourhood_num=st.sidebar.selectbox("Location (# of neighbourhood) :", sorted(data["neighbourhood_num"].unique()),index=9)
room_type=st.sidebar.selectbox("Room type :", sorted(data["room_type"].unique()),index=0)
accommodates = st.sidebar.selectbox("# persons accomodated :", sorted(data["accommodates"].unique()),index=2)
bedrooms = st.sidebar.selectbox("# bedrooms :", sorted(data["bedrooms"].unique()),index=1)
beds = st.sidebar.selectbox("# beds :", sorted(data["beds"].unique()),index=0)
bathrooms = st.sidebar.selectbox("# bathrooms :", sorted(data["bathrooms"].unique()),index=2)
is_shared_bathrooms = st.sidebar.checkbox('Shared bathrooms :',value=False)

st.sidebar.write("")
st.sidebar.write("- About Your Booking Policy")
has_availability = st.sidebar.checkbox('Available for booking',value=True)
instant_bookable = st.sidebar.checkbox('Instant bookable',value=True)
minimum_nights = st.sidebar.selectbox("# Nights Minimum :", sorted(data["minimum_nights"].unique()),index=1)
maximum_nights = st.sidebar.selectbox("# Nights Maximum :", sorted(data["maximum_nights"].unique(),reverse=True),index=100)
st.sidebar.write("")
st.sidebar.write("- About Your Reviews & Ratings")
number_of_reviews = st.sidebar.selectbox("# of Total Reviews :", sorted(data["number_of_reviews"].unique()),index=4)
number_of_reviews_ltm = st.sidebar.selectbox("# of Reviews over last 12 months :", sorted(data["number_of_reviews_ltm"].unique()),index=2)
number_of_reviews_l30d = st.sidebar.selectbox("# of Reviews over last 30 days :", sorted(data["number_of_reviews_l30d"].unique()),index=0)
review_scores_rating = st.sidebar.selectbox("Total Rating Score:", sorted(data["review_scores_rating"].unique(),reverse=True),index=0)
review_scores_cleanliness = st.sidebar.selectbox("Cleanliness Rating Score:", sorted(data["review_scores_cleanliness"].unique(),reverse=True),index=0)
review_scores_checkin = st.sidebar.selectbox("Checkin Rating Score:", sorted(data["review_scores_checkin"].unique(),reverse=True),index=0)
review_scores_location = st.sidebar.selectbox("Location Rating Score:", sorted(data["review_scores_location"].unique(),reverse=True),index=0)
review_scores_communication = st.sidebar.selectbox("Communication Rating Score:", sorted(data["review_scores_communication"].unique(),reverse=True),index=0)
st.sidebar.write("")
st.sidebar.write("- About Your Amenities")
wifi = st.sidebar.checkbox('WiFi',value=True)
tv = st.sidebar.checkbox('TV',value=True)
elevator = st.sidebar.checkbox('Elevator',value=True)
workspace = st.sidebar.checkbox('Workspace',value=True)
kitchen = st.sidebar.checkbox('Kitchen',value=True)
parking = st.sidebar.checkbox('Parking',value=False)
pool = st.sidebar.checkbox('Pool',value=False)
breakfast = st.sidebar.checkbox('Breakfast',value=False)
bathtub = st.sidebar.checkbox('Bathtub',value=False)
pet = st.sidebar.checkbox('Allows pet',value=False)
balcony = st.sidebar.checkbox('Balcony',value=False)
ethernet = st.sidebar.checkbox('Ethernet',value=False)
fireplace = st.sidebar.checkbox('Fireplace',value=False)
gym = st.sidebar.checkbox('Gym',value=False)

#st.sidebar.write("")

#makes2=['All','African American','Asian','Caucasian','Hispanic','Native American','Other/Unknown' ]
#make_choice2 = st.sidebar.selectbox('Select the Ethnicity:', makes2)



################# Scatter Chart Logic #################

st.markdown("")
st.markdown("")


with st.container():
    st.header("General Overview")

    col1, col2, col3 = st.columns([3,3,3])
                           
    col1.metric("Total number of listing in Paris", "49,255 \xF0\x9F\x8F\xA0")
    
    col2.metric("Average Price per Night", "129$ \xF0\x9F\x92\xB8")
    
    col3.metric("Average Review per Month", "0.63")

  
st.markdown("")
st.markdown("")

#st.markdown("Information about the patients that died during their stay in ICU") 



# if make_choice2=='All':
#     lables = ['African American','Asian','Caucasian','Hispanic','Native American','Other/Unknown' ]
#     set2=data
# if make_choice2=='African American':
#     set2=data[data['ethnicity']=='African American']
#     lables = ['African American']
# if make_choice2=='Asian':
#     set2=data[data['ethnicity']=='Asian']
#     lables = ['Asian']
# if make_choice2=='Caucasian':
#     set2=data[data['ethnicity']=='Caucasian']
#     lables = ['Caucasian']
# if make_choice2=='Hispanic':
#     set2=data[data['ethnicity']=='Hispanic']
#     lables = ['Hispanic']
# if make_choice2=='Native American':
#     set2=data[data['ethnicity']=='Native American']
#     lables = ['Native American']
# if make_choice2=='Other/Unknown':
#     set2=data[data['ethnicity']=='Other/Unknown']
#     lables = ['Other/Unknown']
    
    
with st.container():
        import plotly.express as px


        st.subheader("Number of listings per Neighbourhood depending on SuperHost status")

        g=pd.pivot_table(data,values='price',index=['neighbourhood_cleansed'],columns=['host_is_superhost'], aggfunc='count')
        g.reset_index(level=0, inplace=True)
        g=g.rename(columns={0:"No",1:"Yes"})
    
        fig = px.bar(g, x="neighbourhood_cleansed", y=["Yes","No"],                 
       labels={"value": "Number of listings",
               "neighbourhood_cleansed": "Neighbourhood",
                "variable": "Is SuperHost"
                 },
        color_discrete_map={
        'Yes': 'lightblue',
        'No': '#e8585b'}
      )
    
        
        st.plotly_chart(fig,use_container_width=True)
        st.markdown("")
        st.markdown("")


with st.container():
        st.header("Price prediction - Supervised Machine Learning")
        x="test"
        st.markdown("Based on all your input regarding your listing, we advise you to choose a price per night in this range :")   
        st.markdown("#### 100-120 $")  
        st.markdown("")
        st.markdown("")

with st.container():
        st.header("Content advisor - Data Visualization / NLP")
        st.markdown("")
        st.markdown("You will find below words depicted in different sizes. The bigger and bolder the word appears, the more often it is mentioned within the following category and the more important it is.")   
        st.markdown("")
        st.subheader("Listing's Name")
        st.markdown("")

col1, col2, col3 = st.columns([1.5,5,1.5])

with col1:
    st.write("")

with col2:
    image2 = Image.open(r"C:\Users\Michel\git2\Ironhack-DAFT-FinalProject-AirbnbEarningsOptimization\Images\airbnb_name_wordcloud.png")
    st.image(image2, use_column_width=True)
    st.markdown("")

with col3:
    st.write("")

with st.container():
        st.markdown("")
        st.subheader("Listing's Amenities")
        st.markdown("")

col1, col2, col3 = st.columns([0.5,7,0.5])

with col1:
    st.write("")

with col2:
    image3 = Image.open(r"C:\Users\Michel\git2\Ironhack-DAFT-FinalProject-AirbnbEarningsOptimization\Images\airbnb_amenities_wordcloud.png")
    st.image(image3, use_column_width=True)
    st.markdown("")
    st.markdown("")

with col3:
    st.write("")


from streamlit_folium import folium_static
import folium



with st.container():
        st.header("Location Centers with Highest Occupancy Rate - Unsupervised Machine Learning")
        st.markdown("")
        st.markdown("This are the two centers in Paris where there is a big concentration of listings with the lowest vacancies.")   
        st.markdown("We then recommend you to pick a place around those centers if you plan on investing in a place to rent on Airbnb.") 
        st.markdown("")

col1, col2, col3 = st.columns([1.5,5,1.5])

with col1:
    st.write("")

with col2:
    # center on Liberty Bell
        m = folium.Map(tiles='Stamen Toner', location=[48.856614,2.3522219],zoom_start=12, prefer_canvas=True)

        # add marker for Liberty Bell
        tooltip = "Liberty Bell"
        folium.CircleMarker(location=[48.86545594821669,2.359576547050914],
                    color='#e8585b',
                    fill_color='#e8585b',
                    radius=20,
                    weight=5).add_to(m)
        folium.CircleMarker(location=[48.857176546907944,2.305401143940956],
                    color='#e8585b',
                    fill_color='#e8585b',
                    radius=20,
                    weight=5).add_to(m)

    #folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip).add_to(m)

    # call to render Folium map in Streamlit
#with st.echo():
        folium_static(m)

with col3:
    st.write("")
        
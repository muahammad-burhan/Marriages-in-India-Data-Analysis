import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide" )
# --- Main Page ---
st.title(":bar_chart: Dashboard")

marriage_data=pd.read_csv('marriage_data_india.csv')

# --- Hide Streamlit Style ---

hide_st_style = """
                <style>
                #MainMenue {visibilty: hidden;}
                footer {visibilty: hidden;}
                header {visibilty: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- sidebar ----

st.sidebar.image("Couple.jpeg")
st.sidebar.title("Marriages data in India")

st.sidebar.header("Filter here:")
Marriage_Type = st.sidebar.multiselect(
    "Select the  Marriage Type:",
    options= marriage_data["Marriage_Type"].unique(),
    default=marriage_data["Marriage_Type"].unique()
)
Gender = st.sidebar.multiselect(
    "Select the Gender:",
    options= marriage_data['Gender'].unique(),
    default=marriage_data["Gender"].unique()
)

Parental_Approval = st.sidebar.multiselect(
    "Select the Parental_Approval Status:",
    options= marriage_data["Parental_Approval"].unique(),
    default=marriage_data["Parental_Approval"].unique()
)

Inter_Caste = st.sidebar.multiselect(
    "Select the Inter Cast Status:",
    options= marriage_data["Inter_Caste"].unique(),
    default=marriage_data["Inter_Caste"].unique()
)


Inter_Religion = st.sidebar.multiselect(
    "Select the Inter Religion Status:",
    options= marriage_data["Inter_Religion"].unique(),
    default=marriage_data["Inter_Religion"].unique()
)



marriage_data_selection = marriage_data.query(
    "Marriage_Type == @Marriage_Type & Inter_Caste == @Inter_Caste & Inter_Religion == @Inter_Religion & Gender == @Gender & Parental_Approval == @Parental_Approval" 
)





# --- Charts ---

# --- Gender Div Chart ---

Gender_div = marriage_data_selection.groupby(['Gender', 'Marriage_Type']).size().reset_index(name='count')
fig_Gender = px.bar(Gender_div, 
             x='Marriage_Type', 
             y='count', 
             color='Gender', 
             hover_data=['count', 'Gender'], 
             title='Marriage Data by Marriage Type and Gender')
st.plotly_chart(fig_Gender)

# --- Martial Satisfation Chart ---

Marital_Satisfaction= marriage_data_selection.groupby(['Marriage_Type', 'Marital_Satisfaction' ,
                                            'Parental_Approval']).size().reset_index(name='count')

Marital_Satisfaction['Type_Approval'] = Marital_Satisfaction['Marriage_Type'] + " | " + Marital_Satisfaction['Parental_Approval']
fig_Martial = px.bar(Marital_Satisfaction, 
             x='Marital_Satisfaction', 
             y='count', 
             color='Type_Approval', 
             hover_data=['count', 'Marital_Satisfaction'], 
             title='Marital Satisfaction by Marriage Type and Parrent Approval')
st.plotly_chart(fig_Martial)

# --- Divorce Statu Chart ---

Divorce_Status= marriage_data_selection.groupby(['Marriage_Type', 'Divorce_Status' , 'Parental_Approval']).size().reset_index(name='count')

Divorce_Status['Type_Approval'] = Divorce_Status['Marriage_Type'] + " | " + Divorce_Status['Parental_Approval']
fig_Divorce = px.bar(Divorce_Status, 
             x='Divorce_Status', 
             y='count', 
             color='Type_Approval', 
             hover_data=['count'], 
             title='Divorce Status by Marriage Type and Parrent Approval')
st.plotly_chart(fig_Divorce)

# --- Divorce Status Chart 2 ---

Divorce_Status2= marriage_data_selection.groupby(['Marriage_Type', 'Divorce_Status' , 'Inter_Caste' , 'Inter_Religion']).size().reset_index(name='count')

Divorce_Status2['Type_Caste_Religion'] = Divorce_Status2['Marriage_Type'] + " | " + Divorce_Status2['Inter_Caste'] + " | " + Divorce_Status2['Inter_Religion']

fig_Divorce2 = px.bar(Divorce_Status2, 
             x='Divorce_Status', 
             y='count', 
             color='Type_Caste_Religion', 
             hover_data=['count'], 
             title='Divorce Status by Marriage Type, Inter Caste and Inter Religion')

st.plotly_chart(fig_Divorce2)
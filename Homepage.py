import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt 

st.set_page_config(page_title="Car Selection",page_icon=":car:")
st.title(":red[Car Selection]:car:")
st.sidebar.success("Select a page above")
st.sidebar.title("Dashboard for car selection")
st.sidebar.markdown('###')

df=pd.read_csv("car data.csv")
tab1,tab2=st.tabs(['Categories','Details'])
add=st.sidebar.multiselect(
        "Choose the fuel type",
        options=df["Fuel type"].unique(),
        default=df['Fuel type'].unique()
    )

with tab1:
    st.subheader("Categories")
    st.write("Car manufacturers and categories of cars they provide")
    left_column, right_column = st.columns(2)
    df_rng=df[df['Fuel type'].isin(add)]
    source = df_rng
    base = alt.Chart(source).properties(height=500)
    bar = base.mark_bar(size =15).encode(
    y=alt.Y('count(Manufacturer):Q', title='Number of cars'),
    x=alt.X('Manufacturer:N', title='Manufacturers'),
    color=alt.Color('Manufacturer:N', title ='',
                    legend=alt.Legend(orient='top'))
    )
    st.altair_chart(bar, use_container_width=False)

    bar = base.mark_bar(size =15).encode(
    y=alt.Y('count(Category):Q', title='Number of cars'),
    x=alt.X('Category:N', title='Category'),
    color=alt.Color('Category:N', title ='',
                    legend=alt.Legend(orient='top'))
    )
    st.altair_chart(bar, use_container_width=False)

    

with tab2:
    st.subheader("Details")
    left_column, right_column = st.columns(2)
    with left_column:st.write("Available Fuel Types")
    with right_column:st.write("Drive wheels")
    df_rnp=df[df['Fuel type'].isin(add)]
    source = df_rnp
    base = alt.Chart(source).properties(height=300)
    bar = base.mark_bar(size = 10 ).encode(
    x=alt.X('count(Fuel type):Q', title='Number of cars'),
    y=alt.Y('Fuel type:N', title='Fuel type'),
    color=alt.Color('Fuel type:N', title ='',
                    legend=alt.Legend(orient='top-right'))
    )
    left_column.altair_chart(bar, use_container_width=True)
    dfp=pd.DataFrame({'Number of cars':pd.value_counts(df_rnp['Drive wheels']),'Drive Wheel type':df['Drive wheels'].unique()})
    source=dfp
    base=alt.Chart(source).properties(height=300)
    pie=base.mark_arc(size=10).encode(
        theta=alt.Theta(field="Number of cars", type="quantitative"),
        color=alt.Color(field="Drive Wheel type", type="nominal")
    )
    right_column.altair_chart(pie)
    
    st.write("Number of cars according to mileage range")
    df_rnp=df[df['Fuel type'].isin(add)]
    source = df_rnp
    base = alt.Chart(source)
    bar = base.mark_bar(size =66).encode(
    x=alt.X('Mileage(in km):Q', title='Mileage range',bin=True),
    y=alt.Y('count()',title='Number of cars'),
    color=alt.condition(alt.datum.Creditworthiness < 50,alt.value("steelblue"),alt.value("orange"))
    )
    st.altair_chart(bar)
    




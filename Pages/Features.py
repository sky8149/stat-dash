import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 
import seaborn as sns
import altair as alt

st.set_page_config(
        page_title="Car Selection",page_icon=":car:"
)
df=pd.read_csv("car data.csv")
st.title(":red[Car Features]")


add = st.sidebar.selectbox(
    "Content",
    ("Engine Details","Exterior Details","Interior Details","Features Effect")
)
min_pr = 0
max_pr = df['Price'].max().item()
l_pr, m_pr = st.sidebar.slider(
    "Price",
    min_value=min_pr, max_value=max_pr,
    value=(min_pr, max_pr))
df_rng = df[(df['Price'] >= l_pr) & (df['Price'] <= m_pr)]

if add=="Engine Details":
    st.subheader("Engine Details")
    left_column, right_column = st.columns(2)
    with left_column:st.write("Engine volumes")
    source = df_rng[df_rng['Engine volume'].isin(df_rng['Engine volume'])]
    base = alt.Chart(source).properties(height=300)
    bar = base.mark_bar(size = 10 ).encode(
    y=alt.Y('count(Engine volume):Q', title='Number of cars'),
    x=alt.X('Engine volume:N', title='Engine volume'),
    color=alt.Color('Engine volume:N', title ='',
                    legend=alt.Legend(orient='bottom-right'))
    )
    left_column.altair_chart(bar, use_container_width=True)
    with left_column:st.write("Number of cylinders in the engine")
    source = df_rng[df_rng['Cylinders'].isin(df_rng['Cylinders'])]
    base = alt.Chart(source).properties(height=400)
    bar = base.mark_bar(size =15).encode(
    y=alt.Y('count(Cylinders):Q', title='Number of cars'),
    x=alt.X('Cylinders:N', title='Cylinders'),
    color=alt.Color('Cylinders:N', title ='',
                    legend=alt.Legend(orient='top-right'))
    )
    left_column.altair_chart(bar, use_container_width=False)
    right_column.write("Gear box transmission types")
    dfp=pd.DataFrame({'Number of cars':pd.value_counts(df_rng['Gear box type']),'Gear Transmission':df['Gear box type'].unique()})
    source=dfp
    base=alt.Chart(source).properties(height=300)
    pie=base.mark_arc(size=10).encode(
        theta=alt.Theta(field="Number of cars", type="quantitative"),
        color=alt.Color(field="Gear Transmission", type="nominal")
    )
    right_column.altair_chart(pie)

elif add=="Exterior Details":
    st.subheader("Exterior Details")
    st.write("Available colors of cars")
    source = df_rng[df_rng['Color'].isin(df_rng['Color'])]
    base = alt.Chart(source).properties(height=300)
    bar = base.mark_bar(size =20).encode(
    y=alt.Y('count(Color):Q', title='Number of cars'),
    x=alt.X('Color:N', title='Engine volume'),
    color=alt.Color('Color:N', title ='',
                    legend=alt.Legend(orient='top'))
    )
    st.altair_chart(bar, use_container_width=True)

    dfp=pd.DataFrame({'Number of cars':pd.value_counts(df_rng['Doors']),'Doors':df['Doors'].unique()})
    source=dfp
    base=alt.Chart(source).properties(height=300)
    pie=base.mark_arc(size=10).encode(
        theta=alt.Theta(field="Number of cars", type="quantitative"),
        color=alt.Color(field="Doors", type="nominal")
    )
    st.altair_chart(pie)
    
elif add=="Interior Details":
    st.subheader("Interior Details")
    left_column, right_column = st.columns(2)
    with left_column:st.write("Leather interior(1=Yes,2=No)")
    source = df_rng[df_rng['Color'].isin(df_rng['Color'])]
    base = alt.Chart(source).properties(height=300)
    bar = base.mark_bar(size =15).encode(
    x=alt.X('count(Leather interior):Q', title='Number of cars'),
    y=alt.Y('Leather interior:N', title='Leather interior'),
    color=alt.Color('Leather interior:N', title ='',
                    legend=alt.Legend(orient='top'))
    )
    left_column.altair_chart(bar,use_container_width=False)
    dfp=pd.DataFrame({'Number of cars':pd.value_counts(df_rng['Wheel']),'Stearing wheel side':df['Wheel'].unique()})
    source=dfp
    base=alt.Chart(source).properties(height=300)
    pie=base.mark_arc(size=10).encode(
        theta=alt.Theta(field="Number of cars", type="quantitative"),
        color=alt.Color(field="Stearing wheel side", type="nominal")
    )
    right_column.altair_chart(pie)


elif add=="Features Effect":
    st.subheader("Features Effect")
    st.write("It explains how the features included in the cars are effect the price of the cars")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), ax=ax)
    st.write(fig)
    st.text("The above chart explains the relation between the price of cars of the features of")
    st.text("the car.Basically it is a correlation chart.The closer the correlation between a car's")
    st.text("price and the respective feature it faces to one, the more impact that feature has ")
    st.text("on the car's price.")
  

   

        

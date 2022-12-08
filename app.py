# module imports
import pandas as pd
import plotly.express as px
import streamlit as st
import re

# reading in the data
df_arabica = pd.read_csv('arabica_data_cleaned.csv')

# dropping columns with data irrelevant to the project
# also dropping row 1310 as the score are all zeroes
cols_to_drop = [0, 2, 5, 6, 7, 9, 11, 16, 17, 33, 36, 37, 38, 39, 40, 41, 42, 43] 
df_arabica.drop(df_arabica.columns[cols_to_drop], axis=1, inplace=True)
df_arabica.drop(1310, inplace=True)

# renaming the columns to snake_case and filling empty values with 'unknown'
df_arabica.rename(str.lower, axis=1, inplace=True)
df_arabica.columns = [re.sub('\.', '_', col) for col in df_arabica]
df_arabica.fillna('unknown', inplace=True)

# viewer for the resultant dataframe
st.header('Data Viewer')
st.dataframe(df_arabica)

# histogram of coffee rating by bean variety
st.header('Coffee Score by Bean Variety')
min_score = st.slider("Pick a minimum cup score", 0, 100)
df_score = df_arabica[df_arabica['total_cup_points'] >= min_score]
fig = px.histogram(df_score, x='total_cup_points', color='variety')
fig.update_layout(xaxis_title='Score out of 100', yaxis_title='Number of Samples')
st.write(fig)

# scatter plot of individual category rating
st.header('Compare Individual Categories by Bean Variety')
categories = ['aroma', 'flavor', 'aftertaste', 'acidity', 'body', 'balance', 'uniformity', 'clean_cup', 'sweetness']

cat1 = st.selectbox(label='Select category 1',
                    options=categories,
                    index=categories.index('aroma'))

cat2 = st.selectbox(label='Select category 2',
                    options=categories,
                    index=categories.index('sweetness'))

fig = px.scatter(df_arabica, x=cat1, y=cat2, color='variety')
st.write(fig)

# histogram to compare coffee rating distribution by country of origin
st.header('Compare Score Distribution Between Countries')
country_list = sorted(df_arabica['country_of_origin'].unique())
country_1 = st.selectbox(label='Select country 1',
                        options=country_list,
                        index=country_list.index('United States (Hawaii)'))

country_2 = st.selectbox(label='Select country 2',
                        options=country_list,
                        index=country_list.index('Colombia'))

mask_filter = (df_arabica['country_of_origin'] == country_1) | (df_arabica['country_of_origin'] == country_2)
df_filtered = df_arabica[mask_filter]

normalize = st.checkbox('Normalize histogram', value=True)

if normalize:
    histnorm = 'percent'
else:
    histnorm = None

fig = px.histogram(df_filtered, x='total_cup_points', nbins=30, color='country_of_origin', histnorm=histnorm, barmode='overlay')
fig.update_layout(xaxis_title='Score out of 100')
st.write(fig)
import streamlit as st
import twint
import pandas as pd
import os
import re

st.title('Sentiment Analysis Marvel Movie Review')

st.subheader('''
Scraping Data from Twitter
''')

with st.form(key='Twitter_form'):
    search_term = st.text_input('What do you want to search for?')
    limit = st.slider('How many tweets do you want to get?', 0, 500, step=20)
    output_csv = st.radio('Save a CSV file?', ['Yes', 'No'])
    file_name = st.text_input('Name the CSV file:')
    submit_button = st.form_submit_button(label='Search')

    if submit_button:
        # configure twint
        c = twint.Config()

        c.Search = search_term
        c.Limit = limit

        c.Store_csv = True

        if c.Store_csv:
            c.Output = f'{file_name}.csv'

        twint.run.Search(c)

        data = pd.read_csv(f'{file_name}.csv', usecols=['date', 'tweet'])
        st.table(data)
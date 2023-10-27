import streamlit as st
from pickle import load
import pandas as pd
import re
import random
import tldextract
from urllib.parse import urlparse


#       'qty_exclamation_directory', 'qty_space_directory',
#      'qty_plus_directory', 'qty_asterisk_directory', 'qty_hashtag_directory',
#      'qty_dollar_directory', 'qty_slash_file', 'qty_questionmark_file',
 #      'qty_at_file', 'qty_and_file', 'qty_exclamation_file', 'qty_space_file',
  #     'qty_tilde_file', 'qty_plus_file', 'qty_asterisk_file',
   #    'qty_hashtag_file', 'qty_dollar_file'

st.title('Model Deployment: Phishing Domain Detection')
def prediction():    
    pass
def user_input_features(url1):
    tld = tldextract.extract(url1).suffix
    dir = urlparse(url1).path
    path = (url1.split('/'))[-1]
    # vowels = ['a','e','i','o','u','A','E','I','O','U']

    qty_comma_directory = dir.count(',')
    qty_comma_file = path.count(',')
    qty_comma_params = url1.count(',')
    qty_dollar_params = url1.count('$')
    qty_dot_directory = dir.count('.')
    qty_slash_directory = dir.count('/')
    qty_questionmark_directory = dir.count('?')
    qty_at_directory = dir.count('@')
    qty_exclamation_directory = dir.count('!')
    qty_space_directory = dir.count(' ')
    qty_plus_directory = dir.count('+')
    qty_asterisk_directory = dir.count('*')
    qty_hashtag_directory = dir.count('#')
    qty_dollar_directory = dir.count('$')
    qty_slash_file = path.count('/')
    qty_questionmark_file = path.count('?')
    qty_at_file = path.count('@')
    qty_and_file = path.count('&')
    qty_exclamation_file = path.count('!')
    qty_space_file = path.count(' ')
    qty_tilde_file = path.count('~')
    qty_plus_file = path.count('+')
    qty_asterisk_file = path.count('*')
    qty_hashtag_file = path.count('#')
    qty_dollar_file = path.count('$')
    qty_and_directory = dir.count('&')
    qty_and_params = url1.count('@')
    qty_asterisk_params = url1.count('*')
    qty_at_params = url1.count('@')

    domain_length = len(tld)
    domain_spf = random.choice([-1, 0, 1])

# 'qty_slash_directory', 'qty_questionmark_directory', 'qty_at_directory',
#        'qty_exclamation_directory', 'qty_space_directory',
#        'qty_plus_directory', 'qty_asterisk_directory', 'qty_hashtag_directory',
#        'qty_dollar_directory', 'qty_slash_file', 'qty_questionmark_file',
#        'qty_at_file', 'qty_and_file', 'qty_exclamation_file', 'qty_space_file',
#        'qty_tilde_file', 'qty_plus_file', 'qty_asterisk_file',
#        'qty_hashtag_file', 'qty_dollar_file'

    data = {
            'qty_slash_directory':qty_slash_directory,
            'qty_questionmark_directory':qty_questionmark_directory,
            'qty_at_directory':qty_at_directory,
            'qty_exclamation_directory':qty_exclamation_directory,
            'qty_space_directory':qty_space_directory,
            'qty_plus_directory':qty_plus_directory,
            'qty_asterisk_directory':qty_asterisk_directory,
            'qty_hashtag_directory':qty_hashtag_directory,
            'qty_dollar_directory':qty_dollar_directory,
            'qty_slash_file':qty_slash_file,
            'qty_questionmark_file':qty_questionmark_file,
            'qty_at_file':qty_at_file,
            'qty_and_file':qty_and_file,
            'qty_exclamation_file':qty_exclamation_file,
            'qty_space_file':qty_space_file,
            'qty_tilde_file':qty_tilde_file,
            'qty_plus_file':qty_plus_file,
            'qty_asterisk_file':qty_asterisk_file,
            'qty_hashtag_file':qty_hashtag_file,
            'qty_dollar_file':qty_dollar_file,
    }
    features = pd.DataFrame(data,index = [0])
    return features

url = st.text_input("Enter a URL")
df = user_input_features(url)
st.subheader('User Input parameters')
st.write(df)

loaded_model = load(open('my_model.pkl', 'rb'))

prediction = loaded_model.predict(df)

if url!="":
    st.subheader('Predicted Result')
    if prediction == 0 :
        st.write("Yes")
    else:
        st.write("No")

    st.subheader('Prediction Probability')
    st.write(prediction)
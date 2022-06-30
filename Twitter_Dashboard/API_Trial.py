import pandas as pd
from pandas import json_normalize
import jmespath
import streamlit as st
import requests
from requests.structures import CaseInsensitiveDict
import collections

# URL For class 7, Science Book, Gujarat Board
#url = 'https://api.dev.diksha.gov.in/api/collection/v1/hierarchy/do_213480167763345408149'

#URL For Class 10, chapter Maths Book, CBSE

# url = 'https://api.dev.diksha.gov.in/api/collection/v1/hierarchy/do_213480174309482496161'

# url = 'https://api.dev.diksha.gov.in/api/collection/v1/hierarchy/do_213480175331049472162'

# url = 'https://api.dev.diksha.gov.in/api/collection/v1/hierarchy/do_213480167763345408149'

url = 'https://api.dev.diksha.gov.in/api/collection/v1/hierarchy/do_213480182062153728170'

headers = CaseInsensitiveDict()

headers['Accept'] = 'application/json'

headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvOFlFYkpNcDY4bHpVTGoyVDRLR2pJbG9SZ2E2alZHRiJ9.zqCo7U8JFQD2Gtc1Ai1rCcPLP8hZsVO49ssrX_yCWvw"


r = requests.get(url, headers=headers).json()

print(type(r))

def nested_dict_iter(nested):
    for key, value in nested.iteritems():
        if isinstance(value, collections.Mapping):
            for inner_key, inner_value in nested_dict_iter(value):
                yield inner_key, inner_value
        else:
            yield key, value

st.write(list(dict.items(r)))

#st.write(r)



st.write(r['result']['content']['downloadUrl'])

st.write(r['result']['content']['variants'])


st.write(r['result']['content']['children'][0]['children'][0])



st.write(r['result']['content']['children'][0]['children'][0]['variants'])

st.write(r['result']['content']['children'][0]['children'][0]['streamingUrl'])

st.write(r['result']['content']['children'][0]['children'][0]['previewUrl'])

st.write(r['result']['content']['children'][0]['children'][0]['artifactUrl'])

st.write(r['result']['content']['children'][0]['children'][0]['downloadUrl'])
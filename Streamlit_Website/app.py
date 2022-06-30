from matplotlib import container
import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()


animationurl = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_sfiiilbf.json")


#Header section
with st.container():
    st.subheader("Hi this is madhur!")
    st.title("A busy dude from India ")
    st.write("I am passionate about learning about technology/coding, cooking, reading and caring for my family!")
    st.write("[Learn more>] (https://www.pyharsh.com)")

  #  st.image('rocket.gif')


with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i Do")
        st.write("###")
        st.write("""
                  Blah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah 
                  BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah Blah  
                    Blah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah BlahBlah Blah Blah

        """
        )
        st.write("[You Tube Channel>](https://www.youtube.com)")
    with right_column:
        st_lottie(animationurl, height=300,key='rocket')
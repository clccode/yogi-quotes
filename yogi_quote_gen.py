import yogi_quotes
import random
import streamlit as st

def get_random_quote():
    """
    Returns a random Yogi Berra quote from the list of quotes.
    """
    return random.choice(yogi_quotes.yogi_quotes)

st.set_page_config(page_title="Yogi Berra Quote Generator", page_icon=":baseball:", layout="centered")

st.title("Yogi Berra Quote Generator")
st.image("Yogi_Berra_1956.png", caption="Yogi Berra in 1956", width=300)
st.write("Click the button below to get a random Yogi Berra quote!")
if st.button("Get Quote"):
    quote = get_random_quote()
    st.write(f"*{quote}*")
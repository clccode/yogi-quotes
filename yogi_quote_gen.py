import yogi_quotes
import random
import streamlit as st

def get_random_quote():
    """
    Returns a random Yogi Berra quote from the list of quotes.
    """
    return random.choice(yogi_quotes.yogi_quotes)

st.set_page_config(page_title="Yogi Berra Quotes", page_icon=":baseball:", layout="centered")

# Center all content
st.markdown(
    """
    <div style='display: flex; flex-direction: column; align-items: center; justify-content: center;'>
    """,
    unsafe_allow_html=True
)

st.title("Yogi Berra Quotes")
st.image("Yogi_Berra_1956.png", caption="Yogi Berra in 1956", width=200)
st.write("Click the button below to get a random Yogi Berra quote!")
if st.button("Get Quote"):
    quote = get_random_quote()
    st.markdown(
        f"<span style='font-size:1.5rem; font-style:italic'>&ldquo;{quote}&rdquo;</span>",
        unsafe_allow_html=True
    )
    
st.markdown("</div>", unsafe_allow_html=True)
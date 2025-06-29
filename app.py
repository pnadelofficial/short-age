import streamlit as st

st.title("Short Age")
st.subheader("A Height Game")

with st.expander(expanded=True):
    st.markdown("""
The object of this game is to find a celebrity who has the same age as their height. For example, if you guess an actor is 55 and 5ft 5 then you would win. Otherwise... well... you're a loser. Select a celeb below to get started. 
    """)

@st.cache_data
def read_data():
    import pandas as pd
    df = pd.read_csv("shortage_aheightgame.csv")
    answers = df[df['short-age']].name.to_list()
    return df, answers

df, answers = read_data()

choices = df.name.to_list()
choice = st.selectbox(label="Choose a celeb...", options=choices, index=None)
if choice:
    is_correct = choice in answers
    choice_row = df[df['name'] == choice]
    if is_correct:
        st.success(f"Yay! You did it! {choice} is {int(choice_row.age.values[0])} years old and {str(choice_row.height.values[0])}!")
        
    else:
        st.error(f"Nope. {choice} is {int(choice_row.age.values[0])} years old and {str(choice_row.height.values[0])}... Try again.")

import streamlit as st

st.title("Short Age")
st.subheader("A Height Game")

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
        st.error(f"Nope. {int(choice_row.age.values[0])} years old and {str(choice_row.height.values[0])}... Try again.")

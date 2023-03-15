import streamlit as st

st.title("Registration Form")

col1, col2 = st.columns(2)

col1.text_input("First Name")
col2.text_input("Last Name")

email, mob = st.columns([3,1])

email.text_input("Email ID")
mob.text_input("Mobile Number")

user, pw1, pw2 = st.columns(3)

user.text_input("Username")
pw1.text_input("Password", type="password")
pw2.text_input("Re-Enter Password", type="password")

ch,cl,sub = st.columns(3)

ch.checkbox("I Agree")
sub.button("Submit")
import streamlit as st
import re 

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("🔐Password Strentght Checker")
st.markdown("""
## Welcome To THe Ultimate password Strenght Checker!👋
use this simple tool to check the strenght of your password and get suggestions on how to make it stronger.🔐
            we will give you helpful tips to create a **Strong Password🔐** """)

password = st.text_input("Enter Your Password", type="password")

feedback =[]

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌password should be at least 8 Characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌password should contain both upper anf lower case characters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌password should contain at least one digit.")

    if re.search(r'[!@#$%^&*-+]', password):
        score += 1
    else:
        feedback.append("❌password should contain at least and special charachters.(!@#$%^&*-+)")
    
    if score == 4:
        feedback.append("✅Your Password is strong")
    elif score == 3:
        feedback.append("🟡Your password is medium strength")
    else:
        feedback.append("🔴your password is weak, pleae make it stronger.")
    
    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("please enter your password to get started.")
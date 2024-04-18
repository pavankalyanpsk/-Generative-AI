import streamlit as st
from openai import OpenAI

f = open(r"C:\Users\pavan\Desktop\satya\Machine learning\Internship\INtern\AI_code_reviewer\open_ai_key.txt")
OPENAI_API_KEY = f.read()

st.title("Genarative AI Code Reviewer")
st.subheader("Review your code here")

client = OpenAI(api_key = OPENAI_API_KEY)

prompt = st.text_area("Enter a Code")

if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an expert code review , you need to identify bugs and errors in code and provide corrected versions."},
        {"role": "user", "content": prompt}
      ]
    )
    st.write(response.choices[0].message.content)
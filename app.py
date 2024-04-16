import streamlit as st
from openai import OpenAI


with open('D:/INNOMATICS INTERN/GEN AI/api_key.txt', mode='r') as api_key_file:
    api_key = api_key_file.read().strip()

client = OpenAI(api_key=api_key)


st.set_page_config(layout="wide")
st.title("Python Code Review Tool")
st.markdown("---")

prompt = st.text_area("Enter your Python code here:")

if st.button("Submit"):
    response = client.chat.completions.create(
		model="gpt-3.5-turbo-0125",
    	messages=[
        			{"role": "system", "content": "You are developing a Python application for code review. The goal is to create a user-friendly tool where users can submit their Python code and receive feedback on potential bugs, along with suggestions for fixes. The application should be efficient, providing accurate bug reports and fixed code snippets"},
        			{'role': 'user', "content": prompt}
    			]
	)

    st.write(response.choices[0].message.content)

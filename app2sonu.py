from openai import OpenAI
import streamlit as st

# Embedding the API key directly
api_key = "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"
client = OpenAI(api_key=api_key)

st.snow()
st.title(":rainbow[SOnuVikas GenAI]")
st.header('MCQ GENERATOR APP', divider='rainbow')

prompt = st.text_input('Enter a data science topic')
if st.button("Generate"):
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Generate 5 data Science questions and answer for MCQ test in MCQ format."},
            {"role": "user", "content": prompt}
        ]
    )

    if response.choices:
        st.write(response.choices[0].message.content)

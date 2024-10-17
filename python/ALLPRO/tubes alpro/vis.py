import streamlit as st
import random
import time
import requests

st.write('halo')

url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

headers = {
	"x-rapidapi-key": "701c7df520msh3aced452a67326ep1f26f2jsn40c63f9fb446",
	"x-rapidapi-host": "chatgpt-best-price.p.rapidapi.com",
	"Content-Type": "application/json"
}

def userinput(prompt):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    output = result['choices'][0]['message']['content']
    return output

def response_generator(prompt):
    response = userinput(prompt)

    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title('Chat dengan Mentally Bot!')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Tuliskan pertanyaan anda disini..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # response = f"Mentally Bot: {prompt}"
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    st.session_state.messages.append({"role": "assistant", "content": response})
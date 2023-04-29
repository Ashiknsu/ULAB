import openai
import os
import streamlit as st
openai.api_key = os.environ["OPENAI_API_KEY"]

st.header("CHATBOT")
prompt = st.text_input("Prompt")


st.sidebar.title("Chatbot")
if st.sidebar.button("ULAB"):
        st.session_state["messages"] += [{"role": "user", "content": "Under construction"}]

else:
if st.button("Send"):
    with st.spinner("Generating response..."):
        st.session_state["messages"] += [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=st.session_state["messages"]
        )
        message_response = response["choices"][0]["message"]["content"]
        st.session_state["messages"] += [
            {"role": "system", "content": message_response}
        ]
        show_messages(text)



def show_messages(text):
    messages_str = [
        f"{_['role']}: {_['content']}" for _ in st.session_state["messages"][1:]
    ]
    text.text_area("Messages", value=str("\n".join(messages_str)), height=400)


BASE_PROMPT = [{"role": "CSE Department", "content": "You are a helpful assistant."}]

if "messages" not in st.session_state:
    st.session_state["messages"] = BASE_PROMPT



text = st.empty()
show_messages(text)

if st.button("Clear"):
    st.session_state["messages"] = BASE_PROMPT
    show_messages(text)



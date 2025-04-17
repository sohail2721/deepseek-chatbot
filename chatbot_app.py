import streamlit as st
from openai import OpenAI

# Set your Together.ai API key and base URL
client = OpenAI(
    api_key="d50ef2fb93e8f58882b3997a1d90d5b7ae2c9ba9d66cfb5b70fa7a007ce6bfa8",  # replace with your Together.ai API key
    base_url="https://api.together.xyz/v1",
)

st.title("🤖 DeepSeek Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask me anything...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  # Change this to a valid model
                    messages=st.session_state.messages,
                    temperature=0.7,
                )

                reply = response.choices[0].message.content
                st.write(reply)
                st.session_state.messages.append(
                    {"role": "assistant", "content": reply}
                )
            except Exception as e:
                st.error(f"Failed to get response: {e}")

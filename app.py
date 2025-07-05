from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import requests
import os

# Load your GROQ API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-70b-8192"

# App Title
st.title("🧠 Random Fun Fact Generator")
st.write("Curious about the world? Get a fun, fascinating fact about any topic you choose!")

# User Input
topic = st.text_input(
    "Enter a topic (optional):",
    placeholder="E.g. space, history, animals"
)

# Generate button
if st.button("Generate Fun Fact"):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # Build the user prompt
    if topic.strip():
        user_prompt = (
            f"Give me one fun, surprising, or little-known fact about the topic: {topic}. "
            f"Keep it under 50 words and make it engaging."
        )
    else:
        user_prompt = (
            "Give me one random fun, surprising, or little-known fact about any topic. "
            "Keep it under 50 words and make it engaging."
        )

    data = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "You are a knowledgeable trivia expert who shares fun, surprising facts in an engaging and concise way."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "temperature": 0.8
    }

    with st.spinner("Fetching your fun fact..."):
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        if response.status_code == 200:
            fun_fact = response.json()["choices"][0]["message"]["content"]
            st.subheader("🎉 Here's your fun fact:")
            st.write(fun_fact)
        else:
            st.error("Failed to generate a fun fact. Please check your API key or try again later.")

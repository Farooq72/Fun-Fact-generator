# ✨ AI Fun Fact Generator

A Streamlit-based web application that uses the **Groq API with LLaMA 3** to generate fun, surprising facts on any topic. Type a topic you’re curious about—or leave it blank for a random fact—and let the AI amaze you!

---

## 🚀 Live Demo

👉 [Open the App](https://your-fun-fact-generator-app-url.streamlit.app/)

*(Replace with your actual deployed Streamlit URL if you deploy the app.)*

---

## 📌 Features

* 🧠 AI-generated fun facts using Groq’s LLaMA 3 model
* 🎯 Facts tailored to any topic you enter—or random surprises
* ⚡ Fast and user-friendly interface with Streamlit
* 🔐 Secure API key management via `.env` locally and Streamlit Secrets on deployment

---

## 💠 Tech Stack

* [Streamlit](https://streamlit.io/) – UI framework
* [Groq API](https://console.groq.com/) – LLaMA 3 model
* [Python](https://www.python.org/)
* `requests`, `python-dotenv`

---

## 📅 Local Installation

Follow these steps to run the app locally on your machine:

1. **Clone this repository:**

```bash
git clone https://github.com/Farooq72/Fun-Fact-generator
cd ai-fun-fact-generator


2. **(Optional) Create a virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

4. **Set up the `.env` file:**

Create a `.env` file in the root directory with your Groq API key:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

5. **Run the app:**

```bash
streamlit run app.py
```

---
## 🎞️ Project Working

1. Open the web app.
2. Enter a topic in the input box (e.g., "space", "history", "animals") or leave it blank for a random fact.
3. Click the **Generate Fun Fact** button.
4. The app sends your request to Groq's LLaMA 3 model via API.
5. A fun fact is displayed below the input field.

---


## 🙌 Author

Made by [Farooq Azeem](https://github.com/Farooq72) using Groq API.

---

## 📋 License

This project is licensed under the [MIT License](LICENSE).

---

## 📢 Feedback or Contributions?

Feel free to open issues or submit pull requests. All contributions are welcome!


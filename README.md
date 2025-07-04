````markdown
# 💬 LangChain + Ollama + Streamlit: Ask Anything with Gemma 2

Hey there! 👋

This is a small but fun project I built to explore how to use [LangChain](https://www.langchain.com/), [Ollama](https://ollama.com/), and [Streamlit](https://streamlit.io/) together to create a simple interactive chatbot. It's powered by the lightweight **Gemma 2** model, running locally via Ollama.

Basically, you type in a question, and the model (with a bit of LangChain prompt magic) tries its best to answer it like a helpful assistant.

---

## ✨ Features

- 💡 Ask any question — the assistant responds in real time
- 🧱 Powered by **Gemma 2B** running locally through Ollama
- 🧠 Uses LangChain's prompt templates and chaining to structure the conversation
- 🎛️ Clean and minimal UI built with Streamlit
- 📈 Optional LangSmith tracking enabled for monitoring and debugging

---

## 🔧 Technologies Used

- Python 🐍
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- [LangSmith](https://docs.smith.langchain.com/) (optional, for tracing)
- [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variable management

---

## 🚀 Getting Started

> Make sure you have Python 3.8+ and Ollama installed on your machine.

### 1. Clone the repo

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
````

### 2. Set up your environment

Create a `.env` file in the root of the project with the following variables:

```env
LANGCHAIN_API_KEY=your-langsmith-api-key
LANGCHAIN_PROJECT=YourProjectName
```

(You can skip this if you're not using LangSmith tracking.)

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can manually install:

```bash
pip install streamlit langchain langchain-community langchain-core langchain-ollama python-dotenv
```

### 4. Make sure Ollama is running and has the Gemma model pulled

```bash
ollama run gemma:2b
```

### 5. Run the app!

```bash
streamlit run app.py
```

---

## 🛠️ Notes & Things to Improve

* Right now it's a pretty basic one-shot Q\&A — no memory, context, or chat history.
* Could use more feedback handling for empty inputs or failed model loads.
* Would love to try out other models too (e.g. LLaMA 3 or Mistral).
* Open to UI improvements or adding support for conversation logging.

---

## 🤝 Let’s Connect!

This project is a learning experiment for me, so if you have ideas, feedback, or just want to say hi — feel free to open an issue or submit a pull request.

Happy hacking! 🚀

— *Saketh*

```

# 🤖 Customer Support AI Agent

## Overview

Customer Support AI Agent is a Python and Streamlit-based application that simulates a customer support assistant. The agent can answer customer enquiries, remember user information, retrieve order statuses, and provide refund policy information through an interactive chat interface.

This project demonstrates fundamental AI Agent concepts including memory management, tool integration, persistent storage, and conversational interfaces.

---

## Features

* Interactive ChatGPT-style interface using Streamlit
* Persistent memory using SQLite
* Customer name recognition and recall
* Order lookup tool
* Refund policy tool
* Session-based conversation history
* Modular Python architecture
* GitHub-ready project structure

---

## Project Structure

```text
customer-support-agent/
│
├── app/
│   ├── database.py
│   ├── tools.py
│   └── __init__.py
│
├── ui/
│   └── streamlit_app.py
│
├── customer_support.db
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Technologies Used

* Python
* Streamlit
* SQLite
* Git
* GitHub

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd customer-support-agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python -m streamlit run ui/streamlit_app.py
```

---

## Example Usage

User:

```text
My name is Olu
```

Agent:

```text
Nice to meet you, Olu.
```

User:

```text
What is my name?
```

Agent:

```text
Your name is Olu.
```

User:

```text
My order number is 12345
```

Agent:

```text
Your order is out for delivery and should arrive today.
```

---

## Skills Demonstrated

* Python Programming
* AI Agent Development
* Streamlit Web Applications
* SQLite Database Integration
* State Management
* Tool Calling Architecture
* Software Development Best Practices
* Version Control with Git

---

## Future Enhancements

* Amazon Bedrock Integration
* OpenAI Integration
* Retrieval-Augmented Generation (RAG)
* PostgreSQL Database
* User Authentication
* Customer Knowledge Base
* Cloud Deployment
* Multi-Agent Architecture

---

## Author

Olufunso Ojo

AI Engineering and Data Science Portfolio Project

# 🤖 AI Customer Support Agent with Amazon Bedrock

## Overview

This project is an AI-powered Customer Support Agent built using Python, Streamlit, SQLite, and Amazon Bedrock. The application provides a conversational interface that can remember customer information, retrieve order statuses, answer refund-related questions, and generate intelligent responses using Amazon Nova Lite through Amazon Bedrock.

The project demonstrates key AI Agent concepts including memory management, tool calling, persistent storage, cloud AI integration, and conversational user interfaces.

---

## Features

### Conversational AI

* ChatGPT-style chat interface
* Interactive customer support experience
* AI-generated responses using Amazon Bedrock

### Persistent Memory

* Stores customer information in SQLite
* Remembers customer names across application restarts
* Retrieves stored information during future conversations

### Customer Support Tools

* Order status lookup
* Refund policy lookup
* Customer information retrieval

### Amazon Bedrock Integration

* Connected to Amazon Bedrock Runtime
* Uses Amazon Nova Lite foundation model
* Includes fallback handling when Bedrock quotas are exceeded

---

## Architecture

```text
User
 │
 ▼
Streamlit Chat Interface
 │
 ▼
Customer Support Agent
 ├── SQLite Memory
 ├── Order Lookup Tool
 ├── Refund Policy Tool
 └── Amazon Bedrock (Nova Lite)
```

---

## Technologies Used

* Python
* Streamlit
* SQLite
* Amazon Bedrock
* Amazon Nova Lite
* Boto3
* Git
* GitHub

---

## Project Structure

customer-support-agent/

├── app/

│   ├── bedrock_client.py

│   ├── database.py

│   ├── tools.py

│   └── **init**.py

│

├── ui/

│   └── streamlit_app.py

│

├── requirements.txt

├── README.md

└── .gitignore

---

## Installation

Clone the repository:

```bash
git clone https://github.com/olufuns/customer-support-agent.git
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

## AWS Configuration

Configure AWS credentials:

```bash
aws configure
```

Use:

```text
Region: us-west-2
Output: json
```

Enable Amazon Nova Lite access in Amazon Bedrock.

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

* AI Agent Development
* Amazon Bedrock Integration
* Foundation Model Usage
* Python Programming
* Streamlit Application Development
* SQLite Database Management
* Tool Calling Architecture
* Memory Systems
* Cloud AI Services
* Git and GitHub

---

## Future Enhancements

* Retrieval-Augmented Generation (RAG)
* Knowledge Base Integration
* Customer Authentication
* PostgreSQL Migration
* Multi-Agent Architecture
* Deployment on AWS

---

## Author

Olufunso Ojo

AI Engineering and Data Science Portfolio Project


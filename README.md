# Toxic Comment Detection System

## 🔍 Overview

The **Toxic Comment Detection & Moderation System** is an AI-powered web application that analyzes user comments and classifies them as toxic or non-toxic.

Beyond basic classification, the system also provides:

**Toxicity probability**

**Severity level**

**AI-based moderation suggestions**

This makes the project suitable for social media content moderation scenarios.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## 🌟 Key Highlights

✅ Real-time toxic vs non-toxic classification

📊 Toxicity probability score

🚦 Severity classification (Clean, Mild, Moderate, Severe)

🛡️ AI-based moderation suggestions (Allow, Hide, Warn, Block)

🎨 Color-coded results for better user experience

⚡ Auto-reloading backend during development

---

## 🖼️ Screenshots

### 🌐 Web App
![Web App Screenshot](images/web-ui.jpg)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## 🛠️ Tech Stack

| Layer             | Technology                                 |
|-------------------|--------------------------------------------|
| **Frontend**      | HTML, Tailwind CSS, JavaScript             |
| **Backend**       | Flask (Python)                             |
| **ML Model**      | fine-tunned BERT (`transformers`)          |
| **Model Hosting** | Hugging Face                               |
| **Environment**   | Pythong Virtual Environment(venv)          |
|-------------------|--------------------------------------------|


## 📖 How It Works

>User enters a comment in the web interface.

>The text is sent to the Flask backend using JavaScript fetch.

>The AI model predicts toxicity probability.

>The system assigns:

  ## Label (toxic / non-toxic)

  ## Severity level

  ## Moderation action

>Results are displayed dynamically on the webpage.


## 🧠 Severity & Moderation Logic

|Toxic Probability |	Severity |	Suggested Action |
|------------------|-----------|-------------------|
|   < 0.30	       |  Clean	   |   Allow comment   |
|  0.30 – 0.50	   |  Mild	   |   Hide comment    |
|  0.50 – 0.75	   |  Moderate |   Warn user       |
|   > 0.75         |  Severe	 |   Block & report  |
|------------------|-----------|-------------------|


## 📚 Acknowledgments

🤗 Hugging Face for pre-trained NLP models

🐍 Flask for lightweight backend development

📘 Transformers library for NLP pipelines




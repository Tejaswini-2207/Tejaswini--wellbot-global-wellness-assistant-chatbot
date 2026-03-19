# Tejaswini--wellbot-global-wellness-assistant-chatbot
🌿 WellBot – AI-Powered Wellness Assistant
📌 Project Overview

WellBot is an AI-driven wellness platform that combines chatbot intelligence with health analytics tools to help users manage their physical and mental well-being effectively.

It integrates multiple AI models, health tracking tools, and prescription analysis into a single unified system.

🚀 Core Features
🤖 AI Wellness Chatbot

Conversational AI for health-related queries

Intelligent responses using multi-model orchestration

📸 Prescription Image Analysis

Upload prescription images

Extracts medicine names

Provides dosage and guidance

🩺 Symptom Checker

Helps users understand possible health conditions

Provides basic medical suggestions

🍎 Nutrition Guidance

Personalized diet suggestions

Detailed nutrient information

📊 Health Monitoring Dashboard

Track daily wellness metrics

Visual insights with charts

🧑‍💻 Admin Monitoring System

Manage users and chats

Monitor system performance

🏗️ System Architecture
User Interface (HTML/CSS/JS)
        ↓
Frontend Dashboard
        ↓
Flask Backend API
        ↓
AI Model Router
        ↓
Groq | Gemini | Ollama | OpenAI
        ↓
MongoDB Database

✅ Hybrid AI architecture ensures:

High reliability

Automatic fallback support

💻 Technologies Used
🎨 Frontend

HTML5

CSS3

JavaScript (ES6)

Chart.js

Google Fonts (Inter, Poppins)

📄 Pages

index.html

login.html

register.html

dashboard.html

chatbot.html

admin_dashboard.html

⚙ Backend

Python

Flask

Flask-CORS

Authlib (Google OAuth)

🔧 Responsibilities

API routing

Authentication

AI request handling

Image processing

Database operations

📌 Main File: app.py

🧠 AI Models Integrated
Model	Purpose
Rule-Based AIML	Basic chatbot responses
Groq (Llama 3.3)	Primary LLM
Gemini 1.5 Flash	Cloud fallback
Ollama	Local AI model
OpenAI GPT-4o Vision	Prescription analysis
🗄 Database

Database: MongoDB

📂 Collections

users

chats

feedback

reported_issues

prescriptions

📌 Stores

User accounts

Chat history

Feedback

Uploaded prescriptions

Issue reports

📦 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yourusername/wellbot.git
cd wellbot
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Setup Environment Variables

Create a .env file:

MONGO_URI=your_mongodb_uri
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_gemini_key
4️⃣ Run the Server
python app.py

🌐 Server runs at:

http://localhost:5000
👤 User Dashboard Features
🏃 Health Tracking Tools

👣 Step Counter

😊 Mood Tracker

😴 Sleep Tracker

❤️ Heart Rate Monitor

⚖ BMI Calculator

🔥 Calories Tracker

🥗 AI Diet Planner

🍎 Nutrition Guide
Vitamins

Vitamin A, B, C, D, E

Minerals

Iron, Zinc, Magnesium, Calcium, Potassium

Protein Sources

Eggs, Fish, Chicken

Lentils, Beans, Tofu

Milk

📸 AI Prescription Analysis
Workflow

Upload prescription image

Extract medicine details

Identify dosage

Provide medical guidance

Supported Models

OpenAI Vision

Gemini Vision

Ollama Vision

🧑‍💻 Admin Dashboard
Features

👥 User Management

💬 Chat Monitoring

📊 Usage Analytics

⚠ Issue Reports

🤖 Floating Chatbot

🛡 System Health Monitor

🔐 Security Features

SHA-256 password hashing

Token-based authentication

Secure API keys (.env)

Crisis message detection

Protected admin routes

🌍 Accessibility

English

🎨 Themes

Light Mode

Dark Mode

📊 System Monitoring

Tracks:

Active users

AI model usage

System health

Chat statistics

🎯 Project Goal

To provide accessible, AI-powered healthcare assistance that improves understanding and promotes better health decisions.

🏁 Conclusion

WellBot demonstrates how modern AI can enhance healthcare by combining:

Intelligent chatbots

Prescription analysis

Wellness tracking

Admin monitoring systems

✨ Making healthcare faster, smarter, and accessible for everyone.

👥 Contributors

Tejaswini

Avinash

Sameer

Sakshi

Harika

Apeksha


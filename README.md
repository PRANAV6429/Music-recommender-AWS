# 🎵 AI-Powered Music Recommendation System

An AI-powered cloud-native music recommendation system that analyzes user emotions using Natural Language Processing (NLP) and recommends songs based on the detected mood. The application integrates AWS services for sentiment analysis, voice generation, and user interaction logging while being containerized with Docker and deployed on Railway.

## 🚀 Features

- Mood-based song recommendations
- Sentiment analysis using AWS Comprehend
- Voice responses using AWS Polly
- User interaction logging with DynamoDB
- Responsive Flask web interface
- Dockerized application for portability
- Cloud deployment on Railway
- Real-time recommendation generation

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Cloud Services
- AWS Comprehend
- AWS Polly
- Amazon DynamoDB

### DevOps & Deployment
- Docker
- Railway
- GitHub

### AI / NLP
- Sentiment Analysis
- Mood Detection

---

## 🏗️ Architecture

```text
User Input
     │
     ▼
Flask Web Application
     │
     ▼
AWS Comprehend
(Sentiment Analysis)
     │
     ▼
Mood Detection
     │
 ┌───┴───────────┐
 ▼               ▼
Song Engine   DynamoDB
              User Logs
     │
     ▼
AWS Polly
(Text-To-Speech)
     │
     ▼
Music Recommendations
```

---

## ⚙️ How It Works

1. User enters a text message describing their mood.
2. AWS Comprehend analyzes the sentiment.
3. The system detects the user's emotional state.
4. Relevant songs are selected from the recommendation dataset.
5. User interactions are stored in DynamoDB.
6. AWS Polly generates a voice response.
7. Recommended songs are displayed to the user.

---

## ☁️ AWS Services Used

### Amazon Comprehend
Performs sentiment analysis to identify user emotions from text input.

### Amazon Polly
Converts recommendation messages into speech for a better user experience.

### Amazon DynamoDB
Stores user mood, input text, timestamps, and recommendation history.

---

## 🐳 Running Locally

### Clone the Repository

```bash
git clone https://github.com/PRANAV6429/Music-recommender-AWS.git
cd Music-recommender-AWS
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure AWS Credentials

```bash
aws configure
```

### Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🐳 Docker Setup

### Build Image

```bash
docker build -t music-recommender .
```

### Run Container

```bash
docker run -p 5000:5000 music-recommender
```

---

## 📈 Project Highlights

- Developed an AI-powered recommendation engine based on mood detection.
- Integrated AWS Comprehend, Polly, and DynamoDB into a single cloud-native application.
- Containerized the application using Docker for consistent deployment.
- Deployed the solution on Railway with zero server management.
- Demonstrated practical implementation of AI, Cloud Computing, and DevOps concepts.

---

## 🔮 Future Enhancements

- Spotify API integration
- Personalized recommendation history
- User authentication and profiles
- CI/CD pipeline using GitHub Actions
- Kubernetes deployment on AWS EKS
- Advanced machine learning recommendation models

---

## 👨‍💻 Author

**Pranav Sai Aditya**

Aspiring Cloud & DevOps Engineer | AWS Enthusiast | Software Developer

GitHub: https://github.com/PRANAV6429

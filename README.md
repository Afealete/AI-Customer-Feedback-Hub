# ☁️ AI Feedback Hub

A fully serverless, AI-powered customer feedback system built on AWS.  
Users submit feedback through a web form, AWS processes it with AI (sentiment + entity extraction), and results are visualized in a live analytics dashboard.

---

## 📌 Overview

The AI Feedback Hub is a **production-style serverless application** that demonstrates modern cloud architecture patterns:

- Static frontend hosting
- API-driven backend
- AI-powered text analysis
- NoSQL data storage
- Automated CI/CD deployment

It is designed as a **portfolio-ready capstone project** showcasing full-stack cloud engineering skills.

---

## 🏗️ System Architecture

---

## ⚙️ Architecture Summary

The system is composed of 5 core layers:

### 1. Frontend (S3 Static Website)
- Hosts:
  - Feedback form (`index.html`)
  - Admin dashboard (`dashboard.html`)
- Built with HTML, CSS, and JavaScript
- Communicates with backend via REST API

---

### 2. API Layer (Amazon API Gateway)
- Exposes REST endpoints:
  - `POST /feedback`
  - `GET /stats`
- Handles routing, request validation, and CORS

---

### 3. Compute Layer (AWS Lambda)
Two Lambda functions:
- `cloudwithshad-process-feedback` → processes incoming feedback
- `get-feedback-stats` → aggregates analytics for dashboard

---

### 4. AI Layer (Amazon Comprehend)
- Sentiment analysis (Positive, Negative, Neutral, Mixed)
- Named entity recognition (people, organizations, locations)

---

### 5. Database (Amazon DynamoDB)
Stores structured feedback data:

- feedback_id
- name
- email
- message
- sentiment
- sentiment_score
- entities
- timestamp

---

## 🔁 Data Flow

### 📥 Feedback Submission Flow
1. User submits feedback form
2. API Gateway receives request
3. Lambda processes data
4. Amazon Comprehend analyzes text
5. Results stored in DynamoDB
6. Response returned to frontend

---

### 📊 Analytics Flow
1. Admin opens dashboard
2. Dashboard calls `/stats` API
3. Lambda scans DynamoDB
4. Aggregates:
   - Sentiment breakdown
   - Top entities
   - Recent feedback
5. Returns JSON for visualization

---

## 🌐 API Endpoints

| Method | Endpoint      | Description               |
|--------|--------------|---------------------------|
| POST   | /feedback    | Submit customer feedback  |
| GET    | /stats       | Retrieve analytics data   |

---

## 🧰 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** AWS Lambda (Python 3.12)
- **API:** Amazon API Gateway
- **AI:** Amazon Comprehend
- **Database:** Amazon DynamoDB
- **Hosting:** Amazon S3
- **CI/CD:** GitHub Actions

---

## 🚀 CI/CD Pipeline

Automated deployment flow:

1. Push code to GitHub
2. GitHub Actions triggers workflow
3. Build & validation (lint/tests if enabled)
4. Sync frontend to S3
5. Invalidate cache (if configured)
6. Live deployment updated

---

## 🔐 Security Best Practices

- IAM roles follow **least privilege principle**
- No secrets stored in frontend
- CORS enabled for controlled API access
- Separate roles for Lambda execution
- Serverless architecture reduces attack surface

---

## 📦 Project Structure
/frontend
├── index.html
├── dashboard.html

/lambda
├── cloudwithshad-process-feedback-c85a3588-a7d7-4268-947a-6aa3dccaf10a/
    lambda_function.py
├── get-feedback-stats-29c89483-6d19-4eb2-8fe0-0db8ef128c21/
    lambda_function.py

.github/workflows
├── deploy.yml



---

## 💡 Key Features

- Real-time AI sentiment analysis
- Entity extraction from user feedback
- Live analytics dashboard
- Fully serverless architecture
- Auto-deployed via GitHub Actions
- Scalable cloud-native design

---

## 📈 Why This Project Matters

This project demonstrates:

- Full-stack cloud engineering
- AI integration in real applications
- Event-driven serverless systems
- Production-grade architecture design
- CI/CD automation skills

It is designed to be **employer-facing and portfolio-ready**.

---

## 📌 Future Improvements

- Add authentication (Cognito)
- Add real-time dashboard updates (WebSockets)
- Add data export (CSV/PDF reports)
- Upgrade analytics with Athena + S3 data lake
- Add sentiment trend visualization over time


---
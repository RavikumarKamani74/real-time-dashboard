# 📊 Real-Time Metrics Dashboard

A serverless real-time dashboard built with **React** and powered by **AWS Lambda**, **API Gateway**, **DynamoDB**, **S3**, **CloudFront**, and automated deployment using **GitHub Actions**.

---

## 🚀 Live Demo

🔗 [View Dashboard](https://dpf18rjfqfy56.cloudfront.net)  
(API-backed frontend with real-time metric data)

---

## 🛠️ Tech Stack

| Layer       | Technology                            |
|------------|----------------------------------------|
| Frontend    | React (hosted on S3 + CloudFront)     |
| Backend     | AWS Lambda (Python)                   |
| API Gateway | RESTful API Layer                     |
| Database    | DynamoDB (real-time metric storage)   |
| CI/CD       | GitHub Actions + OIDC IAM Role        |

---

## 📦 Features

- 📡 Fetches live CPU metrics from DynamoDB via API Gateway
- 📊 Displays metrics in a clean, timestamped dashboard
- ☁️ Fully serverless architecture (no EC2, no backend servers)
- 🔄 Automatic CI/CD deployment using GitHub Actions

---

## 🧱 Project Structure

├── public/ # HTML template, favicon
├── src/ # React components
│ └── App.js # Main dashboard logic
├── simulate_metrics.py # (Optional) Metric simulation script
├── package.json # React + dependencies
├── .github/
│ └── workflows/
│ └── deploy.yml # CI/CD pipeline


---

## 🚀 Deployment Process (CI/CD)

This project uses GitHub Actions to automate frontend deployment:

- On every `push` to `main`:
  - React app is built
  - Static files synced to S3 (`real-time-metrics`)
  - CloudFront cache is invalidated (`E2141FI3L1865X`)
  - Done in seconds

> AWS credentials are assumed using GitHub OIDC with role:  
> `arn:aws:iam::358238714507:role/GitHubOIDCRole`

---

## 🧪 Local Development

```bash
# Install dependencies
npm install

# Start local dev server
npm start

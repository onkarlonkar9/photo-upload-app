# 🖼️ Serverless Photo Upload App

A **modern serverless photo upload application** that allows users to upload images directly from their browser to **AWS S3** via **AWS Lambda** and **API Gateway**. Built with **Python Flask** for the backend.  

---

## 🚀 Features

- Upload images from browser to AWS S3  
- Serverless architecture using AWS Lambda & API Gateway  
- Real-time image URL generation  
-  **Python Flask**  
- Fully public or private S3 integration  

---

## 🛠️ Tech Stack

| Layer      | Technology                     |
|----------- |--------------------------------|
| Backend    | Python 3, Flask                |
| Serverless | AWS Lambda, API Gateway        |
| Storage    | AWS S3                         |
| Tools      | Git, GitHub, Postman           |

---


## ⚡ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/onkarlonkar9/photo-upload-app.git
cd photo-upload-app
```
Setup (Python Flask)

Install Python from python.org

Create a virtual environment:
```bash

cd photo-upload-app
python -m venv venv
```


Activate virtual environment:

Windows:
```bash
.\venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the Flask app:
```bash
python app.py
```

Open browser: http://127.0.0.1:5000

🖌️ Usage
![](./img/output.png)
Open the app in your browser

Choose an image file

Click Upload

Image is uploaded to AWS S3 and a public URL is generated

View or share the image using the generated link

🔐 AWS Setup

S3 Bucket:

Create a bucket in your region (e.g., ap-southeast-1)

Enable public read access (or use pre-signed URLs for security)
![](./img/S3-output.png)
Lambda Permissions:

Attach AmazonS3FullAccess to Lambda execution role
![](./img/IAM.png)
API Gateway:

Create HTTP API

Route: POST /upload → Lambda integration
![](./img/api-route.png)

Enable CORS: Allowed Origins *, Allowed Methods POST
![](./img/cors.png)
🎨 Screenshots

![](./img/lambda-function.png)
![](./img/test.png)


Ensure API_URL in the Flask app points to your API Gateway endpoint
![](./img/Stage.png)
❤️ Contributing

Fork the repository

Create a new branch feature/your-feature

Commit your changes

Push to the branch

Create a Pull Request

📄 License

MIT License © 2025 Omkar Lonkar

✨ Built with ❤️ for learning and real-world serverless apps.


---

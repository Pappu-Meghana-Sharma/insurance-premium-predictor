# Insurance Premium Prediction System

This project is an end-to-end machine learning application that predicts the insurance premium category (**Low / Medium / High**) based on user details.

I built this project to understand how a machine learning model can be taken from training to a fully deployed system with a backend API and a frontend interface, and to learn how deployment differs from local development.

---

## Project Overview

The system consists of two main components:

- **Backend**: A FastAPI service that loads a trained machine learning model and exposes a `/predict` API.
- **Frontend**: A Streamlit application that collects user inputs and displays predictions along with confidence scores and class probabilities.

The backend is containerized using Docker and deployed on Render.  
The frontend is deployed using Streamlit Cloud.

---

## Tech Stack

- Python 3.10
- Scikit-learn
- FastAPI
- Uvicorn
- Streamlit
- Docker
- Docker Compose
- Render (Backend deployment)
- Streamlit Cloud (Frontend deployment)

---

## Live Applications

- **Backend API**  
  https://insurance-premium-predictor-bbzf.onrender.com/docs

- **Frontend App**  
  https://pappu-meghana-sharma-insurance-premium-predi-frontendapp-ckdsie.streamlit.app/

---

## Features

- Predicts insurance premium category: **Low / Medium / High**
- Returns prediction confidence
- Shows class-wise probabilities
- Input validation using Pydantic
- Health check endpoint for backend monitoring

---

## API Endpoints

### Health Check
```
GET /health
```

### Prediction
```
POST /predict
```

Example request body:
```json
{
  "user_age": 20,
  "weight": 45,
  "height": 1.7,
  "income_lpa": 12,
  "smoker": true,
  "city": "Mumbai",
  "occupation": "retired"
}
```

---

## Project Structure
```
backend/
 ├── app/
 │   ├── model/
 │   ├── schema/
 │   ├── config/
 │   └── main.py
 ├── Dockerfile
 └── requirements.txt

frontend/
 ├── app.py
 └── requirements.txt
```

---

## Development Notes

During local development, the FastAPI backend and Streamlit frontend worked correctly when run directly on the host machine. However, after containerizing the backend, the frontend could no longer communicate with the API using `localhost`.

This issue occurred because `localhost` inside a Docker container refers to the container itself, not the host machine or another container. As a result, API calls failed even though the backend service was running.

To solve this, I used **Docker Compose** to run the frontend and backend as separate services on the same Docker network. Docker Compose enables service-to-service communication using service names instead of `localhost`, which resolved the connectivity issue.

Running single containers separately was not enough for inter-service communication.

### Other Issues Encountered

- **POST vs GET**: FastAPI's `/docs` worked because the browser sends requests directly. But the frontend sends requests from its own runtime, so the API URL and method must be correct. POST endpoints cannot be tested by simply opening a URL.

- **Deployment vs Local Success**: The API worked locally but failed after deployment because of some code issues. Deployment platforms rebuild from scratch, so local success does not guarantee remote success.

- **Requirements and Python Version**: `requirements.txt` must match the Python version used in the Docker image. Mismatches cause silent failures or runtime errors.

---

## Learnings
- Local machine is not simply local when Docker is involved.
Each container has its own isolated environment
So localhost inside one container is different from localhost inside another container
- That is why frontend could not talk to backend after containerizing
Even though both were working fine when run directly using Streamlit and Uvicorn
- How frontend–backend communication changes after deployment
- Managing Python versions and dependencies during deployment is a must...


---

Author: Meghana Sharma
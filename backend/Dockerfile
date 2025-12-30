#First layer is operating system here python version(Base Image)
FROM python:3.10.9-slim

#workdir
WORKDIR /app


#copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy rest of the application code
COPY . .

#port
EXPOSE 8000

#command
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]


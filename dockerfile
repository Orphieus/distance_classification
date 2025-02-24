FROM python:3.12
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0
RUN pip install numpy pandas scikit-learn wandb opencv-python-headless
CMD ["python", "distance_classification.py"]

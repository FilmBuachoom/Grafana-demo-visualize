FROM python:3.10-slim

RUN apt-get update && apt-get install -y python3-pip

# Install py env
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Run py file
CMD ["python", "./app/insert_data.py"]
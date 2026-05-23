FROM python:3.10

WORKDIR /workspace

# Uncomment and use if you have requirements
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

CMD ["python"]

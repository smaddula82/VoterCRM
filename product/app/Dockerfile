FROM python:latest
EXPOSE 8000
WORKDIR /app
copy requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY api.py /app
CMD python api.py

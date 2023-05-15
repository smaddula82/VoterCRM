FROM python:latest
EXPOSE 8501
WORKDIR /app
copy requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY main.py /app
ENTRYPOINT ["streamlit","run"]
CMD ["main.py"]

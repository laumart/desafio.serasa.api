FROM python:3.8
COPY . /home/user-api
WORKDIR /home/user-api
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "main.py"]
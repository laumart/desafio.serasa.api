FROM python:3.8
COPY . /home/order-api
WORKDIR /home/order-api
RUN pip install -r requirements.txt
EXPOSE 8081
CMD ["python", "main.py"]

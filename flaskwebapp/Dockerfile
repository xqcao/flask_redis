FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5001

CMD ["python","app.py"]


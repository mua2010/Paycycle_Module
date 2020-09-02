# INSTRUCTION TO BUILD
# $docker build .

FROM python:3.8-slim-buster

ADD ./enums.py /app/
ADD ./helpers.py /app/
ADD ./pay_cycle.py /app/
ADD ./test_suite/ /app/test_suite/
ADD ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python3 -m unittest discover -v -s ./test_suite -p "*_test.py" 
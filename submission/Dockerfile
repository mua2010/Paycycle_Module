# INSTRUCTION TO BUILD
# $docker build .

FROM python:3.8-slim-buster

ADD ./enums.py /app/
ADD ./helpers.py /app/
ADD ./pay_cycle.py /app/
ADD ./pay_cycle_test.py /app/
ADD ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python3 -m unittest -v pay_cycle_test.py
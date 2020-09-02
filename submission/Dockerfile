# INSTRUCTION TO BUILD
# docker build .

FROM python:3.8-slim-buster

ADD ./helpers.py /app/
ADD ./helpers_test.py /app/
ADD ./pay_cycle.py /app/
ADD ./pay_cycle_test.py /app/
ADD ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python3 -m unittest discover -v -s ./ -p "*_test.py"
FROM python:3.13

WORKDIR /app

COPY requirement.txt /app/
COPY Application/App.py Application/
COPY Application/Calculator.py Application/


RUN pip install -r requirement.txt

CMD ["python","Application/App.py"]
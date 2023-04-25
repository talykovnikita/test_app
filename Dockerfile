FROM python:3.11
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r ./requirements/prod.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app", "--log-level", "DEBUG"]
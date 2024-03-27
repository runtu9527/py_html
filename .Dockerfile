# 
FROM python:3.10

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
COPY ./static /code/static
COPY ./templates /code/templates

EXPOSE 8080
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
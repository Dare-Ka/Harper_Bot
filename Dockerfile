FROM python:3.11-alpine
RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR /Harper

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .



CMD python main.py
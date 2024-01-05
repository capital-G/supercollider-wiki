FROM python:3.10-alpine

WORKDIR /home/app

# cache dependencies
ADD requirements.txt .
RUN pip install -r requirements.txt

# now add source code
ADD . .

ENTRYPOINT [ "make", "html" ]

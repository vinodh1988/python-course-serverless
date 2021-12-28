From Python:3

WORKDIR /app

ENV MYSQL_HOST=13.233.83.152
ENV MYSQL_USER=vinodh
ENV MYSQL_PASS=Pass@123

copy ./requirements.txt ./

RUN pip install- requirements.txt

COPY index.py ./

cmd python index.py
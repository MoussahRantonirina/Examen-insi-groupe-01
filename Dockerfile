FROM python:3-bullseye

RUN apt update
RUN apt install mariadb-client -y
RUN pip install --no-cache-dir --upgrade web.py mysqlclient
COPY ./server.py /server.py
COPY ./database.py /database.py
COPY ./nav.py /nav.py
COPY ./home.py /home.py
COPY ./details.py /details.py 
COPY ./login.py /login.py
COPY ./logout.py /logout.py

CMD [ "python", "/server.py" ]

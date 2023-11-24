FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
WORKDIR /home/app

RUN apt-get update -y 
RUN apt-get install nano unzip -y
RUN apt install curl -y
RUN curl -fsSL https://get.deta.dev/cli.sh | sh

COPY ./app/requirements.txt /home/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install -U kaleido


COPY ./app /home/app/
RUN wget https://opendata.ecdc.europa.eu/covid19/nationalcasedeath_eueea_daily_ei/csv/data.csv

CMD gunicorn main:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker --error-logfile - --access-logfile - --log-level 'debug' --reload
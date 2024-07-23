FROM python:3.10-bullseye

# создаем и назначаем рабочию директорию
WORKDIR /app

# копируем все в раб.директорию
COPY . /app

# создаем пользователя, чтоб контейнер не работал под root
RUN /bin/bash -c 'chmod -R 740 /app \
                  && apt update --fix-missing \
                  && apt install -y python3-pip libffi-dev gunicorn libpango-1.0-0 libpangoft2-1.0-0 \
                  && python3 -m pip install --upgrade pip \
                  && python3 -m pip install --no-cache-dir -r requirements.txt \
                  && apt clean \
                  && apt autoremove'

EXPOSE 8000

CMD ["python3", "-m" , "src"]

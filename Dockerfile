FROM ubuntu

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -qqy python3 python3-pip

RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /

EXPOSE 5000

ENTRYPOINT [ "bash" ]

CMD ["wrapper.sh"]
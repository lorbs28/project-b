FROM ubuntu

WORKDIR /

COPY . .

RUN apt-get update \
    && apt-get install -qqy python3 python3-pip
    
RUN pip3 install flask

EXPOSE 5000

ENTRYPOINT [ "bash" ]

CMD ["wrapper.sh"]
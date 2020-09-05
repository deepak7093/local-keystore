FROM python:3.6
WORKDIR /keystore
COPY . /keystore
RUN pip install -r requirements.txt
CMD ["keystore-server.py"]
ENTRYPOINT ["python"]

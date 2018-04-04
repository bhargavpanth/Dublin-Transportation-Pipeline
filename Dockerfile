FROM ubuntu:16.04

FROM python:2

ADD ./ Dublin_Bus_pipeline/

WORKDIR Dublin_Bus_pipeline/

ENV PATH=$PATH:/Dublin_Bus_pipeline/lib

ENV PYTHONPATH /Dublin_Bus_pipeline
ENV PYTHONPATH lib/DublinBus/
ENV PYTHONPATH lib/DublinBikes/

ADD main.py /

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


# run python with flag = bus | bike | luas
# host = host location (default localhost)
# start_index = model start index
# end_index = model end index
# mongodb://ec2-34-241-2-13.eu-west-1.compute.amazonaws.com:27017/

CMD ["python", "main.py", "--flag=bus", "--host=localhost", "--start_index=0", "--end_index=100"]

EXPOSE 8000
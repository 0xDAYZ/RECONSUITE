FROM python:3.10

RUN pip install pyfiglet 

RUN pip install colorama

WORKDIR ~

RUN apt-get install git -y

RUN git clone https://github.com/0xDAYZ/RECONSUITE.git

WORKDIR ./RECONSUITE

CMD ["./reconx"]

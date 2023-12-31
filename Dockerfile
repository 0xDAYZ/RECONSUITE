FROM python:3.10

RUN pip install pyfiglet 

RUN pip install colorama

WOKRDIR ~

RUN apt-get install git -y

git clone https://github.com/0xDAYZ/RECONSUITE.git

WORKDIR ./RECONSUITE

CMD ["./reconx"]

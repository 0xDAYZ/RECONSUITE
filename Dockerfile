FROM kalilinux/kali-rolling

RUN apt-get update

RUN apt-get install libnetfilter-queue-dev -y

RUN apt-get install net-tools -y

RUN apt-get install python2 -y

RUN apt-get install python3 -y

RUN apt-get install pip -y

RUN pip install pyfiglet colorama scapy datetime requests netfilterqueue prettytable

WORKDIR ~

RUN apt install git -y

RUN git clone https://github.com/0xDAYZ/RECONSUITE.git

WORKDIR RECONSUITE

CMD ["./reconx"]


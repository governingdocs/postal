FROM ubuntu:noble-20240127.1

RUN apt-get update
RUN apt-get -y install debconf apt-utils
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install ca-certificates
RUN apt-get -y install --fix-missing python3-pip python3 curl autoconf automake libtool pkg-config git
RUN git clone https://github.com/openvenues/libpostal
RUN rm /usr/lib/python3.12/EXTERNALLY-MANAGED

RUN mkdir -p /install/libpostal/data

WORKDIR libpostal
RUN ./bootstrap.sh
RUN ./configure --datadir=/install/libpostal/data
RUN make -j4
RUN make install
RUN ldconfig

WORKDIR /
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD app ./app
ADD main.py .
ADD docker-entrypoint.sh .
RUN chmod a+x docker-entrypoint.sh

ENTRYPOINT ["bash", "docker-entrypoint.sh"]

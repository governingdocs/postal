FROM ubuntu:noble-20240127.1

RUN apt-get update
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

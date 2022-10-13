FROM amazonlinux:2017.09

RUN yum -y update && yum -y install \
    python38 \
    python38-pip \
    python38-devel \
    git \
    gcc \
    unzip

RUN pip-3.8 install chalice

ADD resources /resources/
WORKDIR /resources/
RUN pip-3.8 install -r ./requirements.txt

ARG USERNAME_LOCAL
ARG UID_LOCAL
ARG GID_LOCAL

RUN groupadd -g $GID_LOCAL $USERNAME_LOCAL || echo "This group already exists!"
RUN useradd -u $UID_LOCAL -g $GID_LOCAL $USERNAME_LOCAL

WORKDIR /app

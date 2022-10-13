ARG IMAGE_CLI
FROM $IMAGE_CLI

RUN yum -y update && yum -y install nginx

COPY ./entrypoint.sh /init/entrypoint.sh
RUN chmod +x /init/entrypoint.sh

WORKDIR /app

EXPOSE 7415

ENTRYPOINT ["/init/entrypoint.sh"]

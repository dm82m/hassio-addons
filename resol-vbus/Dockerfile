FROM node:24-alpine

RUN apk add --no-cache \
    git \
    bash

WORKDIR /bin
RUN git clone https://github.com/danielwippermann/resol-vbus.git

WORKDIR /bin/resol-vbus
RUN npm install

WORKDIR /bin/resol-vbus/examples/json-live-data-server
RUN npm install

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

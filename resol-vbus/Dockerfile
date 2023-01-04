ARG BUILD_FROM
FROM $BUILD_FROM
  
RUN curl -fsSL https://deb.nodesource.com/setup_current.x | bash -

RUN apt-get -y install \
  git \
  nodejs

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

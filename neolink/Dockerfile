ARG BUILD_FROM
FROM $BUILD_FROM

RUN apt-get update

RUN apt-get -y install \
  wget \
  unzip \
  libgstrtspserver-1.0-0 \
  libgstreamer1.0-0 \
  libgstreamer-plugins-bad1.0-0 \
  gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad

RUN wget https://nightly.link/thirtythreeforty/neolink/workflows/build/master/release-arm64-buster.zip
RUN unzip release-arm64-buster.zip
RUN cp neolink /bin/neolink_aarch64
RUN chmod +x /bin/neolink_aarch64
RUN rm release-arm64-buster.zip neolink neolink.d

RUN wget https://nightly.link/thirtythreeforty/neolink/workflows/build/master/release-ubuntu-18.04.zip
RUN unzip release-ubuntu-18.04.zip
RUN cp neolink /bin/neolink_amd64
RUN chmod +x /bin/neolink_amd64
RUN rm release-ubuntu-18.04.zip neolink neolink.d

RUN wget https://nightly.link/thirtythreeforty/neolink/workflows/build/master/release-armhf-buster.zip
RUN unzip release-armhf-buster.zip
RUN cp neolink /bin/neolink_armhf
RUN chmod +x /bin/neolink_armhf
RUN rm release-armhf-buster.zip neolink neolink.d

RUN wget https://nightly.link/thirtythreeforty/neolink/workflows/build/master/release-i386-buster.zip
RUN unzip release-i386-buster.zip
RUN cp neolink /bin/neolink_i386
RUN chmod +x /bin/neolink_i386
RUN rm release-i386-buster.zip neolink neolink.d

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

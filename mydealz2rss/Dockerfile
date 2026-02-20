ARG BUILD_FROM
FROM $BUILD_FROM

ARG FEEDGEN2_VERSION="2.0.1"

# Install the stuff we need
RUN apk add --no-cache \
        python3 \
        py3-pip \
        py3-lxml \
        py3-requests \
        py3-beautifulsoup4

# We fix the use of feedgen2 version
RUN pip install --no-cache-dir --break-system-packages \
        feedgen2==${FEEDGEN2_VERSION}

# Copy data for App
COPY mydealz.py /
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

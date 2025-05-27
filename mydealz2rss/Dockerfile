ARG BUILD_FROM
FROM $BUILD_FROM

RUN apt-get update && \
    apt-get install -y \
        python \
        pip && \
    apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    feedgen \
    requests \
    beautifulsoup4 \
    lxml

# Copy data for add-on
COPY mydealz.py /
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

ARG BUILD_FROM
FROM $BUILD_FROM

ARG BUILD_ARCH

ARG NZB_MONKEY_VERSION="v0.2.1"
ARG STREAMLIT_VERSION="1.54.0"

# Install the stuff we need
RUN apk add --no-cache python3 py3-pip wget unzip gcompat ca-certificates
RUN pip install streamlit==${STREAMLIT_VERSION} --break-system-packages

# Install nzb-monkey-go
RUN if [ "${BUILD_ARCH}" = "aarch64" ]; then ARCH="arm64"; \
    elif [ "${BUILD_ARCH}" = "amd64" ]; then ARCH="amd64"; \
    else echo "Unsupported arch: ${BUILD_ARCH}" && exit 1; fi && \
    wget https://github.com/Tensai75/nzb-monkey-go/releases/download/${NZB_MONKEY_VERSION}/nzb-monkey-go_${NZB_MONKEY_VERSION}-linux-${ARCH}.zip && \
    unzip *.zip && \
    chmod +x nzb-monkey-go && \
    rm *.zip

# Copy scripts and app into container
COPY run.sh app.py n.sh nd.sh icon.png /
RUN chmod a+x /run.sh /n.sh /nd.sh
COPY .streamlit/config.toml /root/.streamlit/config.toml

EXPOSE 8501

# Start script
CMD [ "/run.sh" ]

FROM vyahello/async-weather-api-base:0.1.0
LABEL version=0.5.0 \
      metadata="The main image for async weather apo code" \
      maintainer="Volodymyr Yahello <vyahello@gmail.com>"
WORKDIR "/code"
COPY weather weather
COPY requirements.txt docker-entry.sh ./
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt
ENTRYPOINT ["/code/docker-entry.sh"]
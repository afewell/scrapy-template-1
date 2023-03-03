FROM heroku/heroku:18-build

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3-dev python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the Scrapy project into the container
COPY . /app

# Install the necessary Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["scrapy", "crawl", "myspider"]

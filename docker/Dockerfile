FROM ubuntu:22.04
LABEL maintainer="xyz@gail.com"
LABEL description="Amazon search engine worker image"
WORKDIR /app
RUN apt-get update && apt-get install -y python3
COPY . .
CMD ["python3", "search_engine.py"]

FROM ubuntu:latest
LABEL authors="tiger"

ENTRYPOINT ["top", "-b"]
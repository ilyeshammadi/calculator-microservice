FROM python:3.8.1-alpine AS tester
WORKDIR /app
COPY setup.py setup.py
COPY README.md README.md
COPY CHANGES.txt CHANGES.txt
RUN pip install -e ".[testing]"
COPY . .
RUN pytest


FROM python:3.8.1-alpine
WORKDIR /app
COPY setup.py setup.py
COPY README.md README.md
COPY CHANGES.txt CHANGES.txt
RUN pip install -e .
COPY . .
CMD ["pserve", "production.ini"]
EXPOSE 6543
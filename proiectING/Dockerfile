FROM python:3-alpine

ENV FLASK_APP endpoint.py
ENV FLASK_END development

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000    

CMD ["flask","run","--host","0.0.0.0","--port","5000"]
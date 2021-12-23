FROM python:3-alpine

WORKDIR /app

COPY requirements.txt /var/jenkins_home/workspace/DevOps_Academy_Project/cidr_convert_api/python/
RUN pip install -r requirements.txt

COPY . .
CMD ["ash", "-c", "python api.py"]
# docker build -t pym .
# docker run -ti -p 8000:8000 pym

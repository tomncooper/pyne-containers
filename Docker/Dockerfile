FROM python:2.7
#The next two lines could be replaced by using FROM python:2-onbuild in the line above
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD ./code /code
WORKDIR /code
EXPOSE 5000
CMD ["python", "app.py"]

FROM python:3.6

COPY fileuploads.py /app/fileuploads.py
COPY requirements.txt app/requirements.txt

WORKDIR /app
RUN pip3 install --trusted-host mirrors.aliyun.com -i https://mirrors.aliyun.com/pypi/simple/  -r requirements.txt && mkdir uploads

VOLUME /app/uploads

ENTRYPOINT ["waitress-serve", "--port=8083", "--call", "fileuploads:create_app"]

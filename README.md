HTTP文件上传工具

## 运行

```bash
$ pip3 install -r requrements.py
$ ./fileuploads.py # development
$ waitress-serve --port=8083 --call 'fileuploads:create_app' # production
```

## 接口

### 文件上传

```
$ curl http://127.0.0.1:5000/ --form file=@file
```

### 访问已上传的文件

```
$ curl http://127.0.0.1:5000/uploads/<filename>
```

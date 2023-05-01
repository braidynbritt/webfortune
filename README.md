# webfortune
A Dockerized Flask application that provides a Web front-end to the well-known Linux programs 'cowsay' and 'fortune'. 

## How to Build

### Local Run
```flask run --host=0.0.0.0 --port=<PORT>```
  
  GOTO URL
  ```http://127.0.0.1:<PORT>```
  
### Docker Run
```docker build -t <BUILD_NAME> .```

```docker run -dp <PORT>:5000 <BUILD_NAME>```
  
  GOTO URL
  ```http://<IP>:<PORT>```
  
## Routes
```http://<IP>:<PORT>/fortune/```
```http://<IP>:<PORT>/cowsay/<message>/```
```http://<IP>:<PORT>/cowfortune/```

## Pytest in Command Line
```pytest```

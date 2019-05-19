# [썸머코딩 과제 (웹서버)] 선다은
<http://sssunda.pythonanywhere.com>

### Development Environment
- OS : Ubuntu
- Language : Python 3.6
- Framework : Django 2.0.13
- DB : Sqlite
- Front-UI : Material


#### 1. Github 에서 소스 가져오기
sssunda's github : <http://github.com/sssunda/programmers_summercoding>


```bash
$ git clone http://github.com/sssunda/programmers_summercoding
```


#### 2. 서버 초기화 및 시작


```bash
# 초기화
bash ./programmers_summercoding/init_app.sh
# 시작
bash ./programmers_summercoding/run_app.sh
```

#### [참고]
##### init_app.sh 소스

```bash
# 가상환경 생성 및 진입(서버 초기설정) 
virtualenv --python=python3.6 myvenv
source myvenv/bin/activate

# 장고 설치
pip install django~=2.0

# DB 초기화
python manage.py migrate

# 웹 서버 실행
python manage.py runserver
```

##### run_app.sh 소스(서버 구동)

```bash
# 가상환경 진입
source myvenv/bin/activate

# DB 초기화
python manage.py migrate

# 웹 서버 실행
python manage.py runserver
```

명령을 실행한 후, <http://127.0.0.1:8000>에 접속하면 만들어진 웹사이트를 볼 수 있습니다.

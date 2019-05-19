# [썸머코딩 과제 (웹서버)] 선다은


### Development Environment
- OS : Ubuntu
- Language : Python 3.6
- Framework : Django 2.0.13
- DB : Sqlite
- Front-Ui : Material


#### 1. Github 에서 소스 가져오기
sssunda's github : <http://github.com/sssunda/programmers_summercoding>


```bash
$ git clone http://github.com/sssunda/programmers_summercoding
```


#### 2. Github에서 가져온 소스가 있는 폴더로 이동한다.


```bash
cd programmers_summercoding

./script_programmers_summercoding_sundaeun.sh
```


##### script_programmers_summercoding_sundaeun.sh 소스
```bash
# 가상환경 생성
virtualenv --python=python3.6 myvenv

source myvenv/bin/activate

# 장고 설치
pip install django~=2.0

# DB 초기화
python manage.py migrate

# 웹 서버 실행
python manage.py runserver
```


명령을 실행한 후, <http://127.0.0.1:8000>에 접속하면 만들어진 웹사이트를 볼 수 있습니다.

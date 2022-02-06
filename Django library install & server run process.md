# Django 라이브러리 설치 & 서버 실행 프로세스



##### 1. Django 메인폴더 생성하고 들어가기

```
cmd (관리자권한으로 실행)

cd ..  # 명령어로 c drive까지 나가기 

mkdir work_django -> work_django   # 폴더가 생깁니다.

cd work_django

mkdir django_mldl-> django_mldl   # 폴더가 생깁니다.

cd django_mldl
```



##### 2. 가상환경 생성하고 활성화하기

```
1) pip install virtualenv==16.7.7     # 가상 환경을 만들어주는 라이브러리입니다.

2) virtualenv django_env -> django_env    # django_env 라는 이름으로 가상 환경을 새로이 만듭니다.

3) django_env\Scripts\activate -> Scripts     # 폴더 내의 activate 파일을 실행해 가상 환경을 활성화합니다. 
```



##### 3. 필수 라이브러리 설치하고 서버 켜기

```
1) cd mldl_project 

2) pip install -r requirements.txt 

3) python manage.py runserver
```


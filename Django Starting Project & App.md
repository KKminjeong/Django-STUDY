# Django Starting Project & App



### 프로젝트 생성하기 (하나의 웹사이트에 해당)

```
$ django-admin startproject proj_1
```



### manage.py 파일을 통해 각종 명령어를 실행

```
$ proj_1/python manange.py startapp app_1
```


#### manage.py 주요 명령어

| manage.py  주요 명령어 | 역할                                                     | 참고                                                         |
| ---------------------- | :------------------------------------------------------- | :----------------------------------------------------------- |
| startapp [name]        | 앱생성                                                   |                                                              |
| runserver              | 서버실행                                                 |                                                              |
| makemigrations         | model 변경 사항을 DB에 방영하기 위한 migration 파일 생성 | models.py 내용 변경 시 <br />(DB Schema 변경 시)             |
| migrate                | model 변경 사항을 DB에 실제로 반영                       | models.py 내용 변경 시 <br />(DB Schema 변경 시)             |
| createsuperuser        | 관리자 계정 생성                                         |                                                              |
| collectstatic          | 파일들을 한곳에 모음                                     | static 파일 변경/추가/삭제 시<br />(css, js, image files 등) |
| shell                  | shell을 활용해 장고 프로젝트 내 기능들을 확인            |                                                              |


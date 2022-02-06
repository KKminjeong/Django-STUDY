# Django의 구조와 패턴

#### " The central idea behind MVC is code reusability and separation of concerns"



## Django

* Django는 Pythton 의 오픈소스 웹 프레임워크 (Full stack framework)
* Disqus, Instagram, Pinterest 등 유명한 서비스들이 Django 로 서비스되어짐
* Django 에서는 MTV Pattern 을 채용하여 사용
* MTV 는 Model, Template, View 를 말하는 것으로 다른 웹 프로그램에서의 MVC 패턴과 매우 유사



## MVC Pattern(Original design pattern)

* 코드를 짜기 위한 패턴
* Model : 데이터베이스 조작(데이터베이스를 다루는 코드를 가져옴 / DB와의 소통)
* View : 사용자 인터페이스 구현 (화면을 구성하기 위한 자산과 코드 )
* Controller : 내부 계산 & 데이터 처리 로직

![](C:\Users\kanga\gitProjects\Django study\mvc pattern.PNG)

1. User가 web browser을 통해 요청을 보냄.

2. controller가 user의 요청을 받아서 해석한 후 DB와 통신을 주고 받아야 하는 게 있다면 model로 보내고, model의 java 코드가 DB에 SQL 같은 형식으로 요청을 함.
3. model이 받은 DB를 Controller에게 반환.
4. controller가 판단 후 view에 넘겨줌
5. View에 있는 HTML, Css, Java 등에 데이터를 넘겨주고 묶어서 User에게 넘겨줌.



## MTV Pattern ( Django )

* Model 
  * 데이터베이스 조작
  * Model 은 MVC 패턴의 Model 과 같은 역할을 수행
  * DB과 연관된 데이터들을 관리하며, 데이터베이스에 있는 내용을 가지고 오거나 수정, 삭제, 저장(CRUD) 등을 한다.
* Template : 사용자 인터페이스 구현 
  * Template 은 MVC 패턴의 View 와 같은 역할을 수행
  * 실제 사용자에게 보여지는 페이지를 만드는 과정을 여기서 수행
* View : 내부 계산 & 데이터 처리 로직
  * View 는 MVC 패턴의 Controller 역할
  * Model 에서 데이터를 가져오고, 데이터를 처리한 결과를 Template 에 전달하는 역할을 수행하며, 최종 결과를 유저에게 응답

​                                 ![](C:\Users\kanga\gitProjects\Django study\MTV.PNG)



#### MTV Pattern 진행 과정

![](C:\Users\kanga\gitProjects\Django study\Django process.PNG)

* 클라언트로부터 요청을 받으면 URLconf 모듈을 이용하여 URL 을 분석.
* URL 분석 결과를 통해 해당 URL 에 대한 처리를 담당할 VIew를 결정.
* View 는 자신의 로직을 실행하면서, DB 처리가 필요한 경우 Model 을 통해 처리하고 그 결과를 받음.
* View 는 자신의 로직 처리가 끝나면 Template 을 사용하여 클라이언트(유저)에 응답할 HTML 파일을 생성.
* View 는 최종적으로 HTML 파일을 클라이언트(유저)에게 보내 응답.



#### 참고자료

![](C:\Users\kanga\gitProjects\Django study\장고 과정.PNG)
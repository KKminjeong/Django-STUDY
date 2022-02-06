# HTTP Request? HTTP Response?



## Server & Client (Network architecture)

* Server : 특정한 서비스를 제공하는 컴퓨터
* Client : 서비스를 사용하는 사용자 혹은 사용자의 단말기



## 서버의 주소 (URL : Uniform Resource Locator)

* "통신규칙(Protocol) : //인터넷 호스트 주소(IP):Port/경로 이름"
* http://125.209.222.142:80 == https://www.naver.com/

실제로 네이버 도메인 주소(https://www.naver.com/)를 치면 바로 네이버로 가는게 아니라 IP 주소를 찾으러 감



## 서버의 종류 (default port numbers)

* Web server : 80 (http port)
* Database server : 3306, etc
* FTP server : 21
* etc.
* 81, 88, 888, 8888, 8080 : 소프트웨어들이 임의로 포트 지정을 할 때 많이 사용하는 포트 번호 



## HTTP (HyperText Transfer Protocol)

* WWW 상에서 정보를 주고받을 수 있는 통신 프로토콜
* 클라이언트와 서버 사이에 이루어지는 요청/응답(request/response) 프로토콜

#### Request : 서버로의 요청

* GET(method) : 정보를 가져오는 역할
* Post(method) : 요청 데이터 처리, 정보를 입력(및 수정)하는 역할, 주로 데이터 등록에 사용
* PUT : 리소스를 대체, 해당 리소스가 없으면 생성
* PATCH : 리소스를 일부만 변경

#### Response : 서버로부터의 응답

* 응답코드 (Response 헤더 영역)
  * 200(서버 응답 잘됨), 400(Bad request), 404(Not found)

* 응답에 담긴 데이터
  * HTML / JS / CSS / image files, JSON, XML 등

![REST API model](https://user-images.githubusercontent.com/86338750/152669960-d989c446-bfa2-44f6-a77b-dcd9726023fd.png)

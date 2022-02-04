# Django



## 1. Front-end / Back-end

#### Front-end

* 실제로 보여지는 부분(뼈대, 디자인, 동작 등등)
* 시각화의 영역
* Back-end로 부터 넘어온 데이터(서버로부터 뽑혀져 넘겨져온 데이터)를 보여주는 역할
* Visualization (UI)
* 전체 골격 : HTML (ex. body, head)
* 예쁘게 디자인 or 애니메이션 : CSS
* 혼자서 or 상호작용으로 움직이거나 변하는 부분 :  JavaScript (유저가 클릭했을때 반영되는 동작을 구현할 때 주로 사용)
* React, Angular (프레임워크)

#### Back-end

* 보이지 않는 부분
* 웹/앱 서버(의 API 구현), DB 등
* 데이터 처리, 데이터 연산 등을 처리함
* Front-end로 부터 요청을 받아 데이터를 처리하고 되돌려 보내주는 역할
* Logic & Data handing (로직(=데이터처리, 데이터 연산)을 구현한다)
* Server(Server-side scripts) : 어떤 특정한 URL로 요청이 들어왔을 때,  그  URL 요청을 어떻게 처리할 지에 대한 코드를 구현
  * Java, Python, Node.js(Javascript), Ruby, PHP 등
* DBMS(DataBase Management System)
  * MySQL, OracleDB, MariaDB, SQLite, PostgreSQL, MongoDB 등
* 서버와 DB를 담는 그릇 : Local server, AWS, GCP, MS Azure

 

## 2. Mobile application(apps)

* Android OS 혹은 iOS로 개발되어 디바이스에 최적화된 전용앱들 : Native apps
* HTML/CSS/JS로 만들어진 앱들 or 이렇게 만든 후 커버를 씌운 앱들 : Webapp(ex. 당근마켓), Hybird apps
  * 네이티브 앱들은 Front-end와 Back-end를 굳이 나눠서 구분하지 않음
  * 보여지는 부분을 위한 UI code + 내부 처리 및 DB 연동을 위한 logic code
  *  Flutter(Dart 언어/구글에서 만듦), React Native
  * Hybird apps 장점 : 비용 저렴

* Android studio, kotlin(Swift 문법 숙지)


# HTML & CSS & Javascript



## HTML

* HTML = Hypertext Markup Language     
* Hypertext : 문장 중의 어구나 그것에 붙은 표제, 표제를 모은 목차 등이 서로 연결된 문자 데이터 파일
* Markup :  약속(ex. 태그)에 따라서 내용을 작성하면 결과를 눈앞에서 구조로써 보여줌
* HTML은 기본적으로 웹을 구현하는 가장 코어가 되는 기술

```
<html>
  <head>
    <title> 제목 </title>
    <CSS 파일링크>
    <Web-font 링크>
    ....
   </head>
   <body>
     <h1> 제목 </h1>
     <p> 문단 </p>
     <a href = "~"> 링크 </a>
     <javascript 파일링크>
   </body>
</html>   
```

 

## CSS

* CSS = Cascading (폭포수같은) Style Sheets
* 여러 CSS 속성들이 동일한 HTML 태그에 차례대로 위에서부터 아래로 중첩되어 적용됨
* CSS 파일을 따로 만들고 html head태그에 파일링크로 넣음

```
h1{
color:red;
text-align:center;
text-decoration: underline;
}
p{
font-size=15px;
} #p 모두를 가리킴

cf)
.main_p{
font-size=15px; 
} # main_p 라는 클래스를 가리킴
```

```
#Inner-CSS (향후 유지보수가 다소 어려울 수 있음)
<h1 style='color:red; text-align:center;'>제목</h1>

#Outer-CSS
h1{
color:red;
text-align:center;
text-decoration: underline;
}
```

* CSS 선택자 관련 참고자료

  : https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Selectors

#### CSS 적용 우선 순위

```
<html>
  <head>
    <title> 제목 </title> #Outer-CSS
    <CSS 파일링크 1>
    <CSS 파일링크 2>
    <CSS 파일링크 3>
    <Web-font 링크>
    ....
   </head>
   <body>
     <h1 style="color:red;"> 제목 </h1> #Inner-CSS
     <p> 문단 </p>
     <a href = "~"> 링크 </a>
     <javascript 파일링크>
   </body>
</html>   


cf)
h1{
 color:red;!important
}
```

* css 파일링크 1 < css 파일링크 2 < css 파일링크 3 < Inner-CSS < !important

* CSS 요소를 파악하려면 웹사이트 개발자도구 (ctrl+shift+I) 활용

​       : 개발자도구 화면의 Elements, Style 참고!



#### <참고링크>

1. Webpack 튜토리얼(with SASS & Babel) : https://heropy.blog/2017/10/18/webpack_1_start_ejs_sass/
2. Bootstrap 5 & SASS : https://www.freecodecamp.org/news/learn-bootstrap-5-and-sass-by-building-a-portfolio-website/


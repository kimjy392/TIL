소셜 로그인(OAuth - Open Authentication)

OAuth 2.0

 

auth

* authentication(인증 - 로그인)
* authorization(권한 - 로그인 이후)

[장고allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

1. pip install django-allauth
2. settings.py 설정
3. 카카오 설정(http://127.0.0.1:8000/accounts/line/login/callback/) - django 공식문서에 써져있엉
4. admin에 들어가서 소셜어플리케이션 추가  클라이언트 아이디: rest api,  비밀키 : client secret

```
1. 사용자가 카카오 링크(/accounts/kakao/login/)
2. 사용자는 카카오 사이트 로그인 페이지를 확인
3. 사용자는 로그인 정보를 카카오로 보냄
4. 카카오(service provider)는 redirect url로 django 서버(client)로 사용자 토큰을 보냄
5. 해당 토큰을 이용하여 카카오에 인증 요청
6. 카카오에서 확인
7. 로그인
-------------------------
* 토큰(access token)은 보통 유효기간이 있는데,
* refresh token을 통해서 토큰 재발급을 받을 수 있다.
```

```
카카오 - 리소스 서버/인증 서버
사용자(리소그 owner) - 유저
django - 클라이언트
```


# Git-flow

Git flow : 깃에서 제공하는 브랜칭 기능을 활용한 변경이력 관리 전략

https://techblog.woowahan.com/2553/



## Git-flow 전략

- 항상 유지되는 메인 브랜치
  - master: 제품으로 출시될 수 있는 브랜치
  - develop: 다음 출시 버전을 개발하는 브랜치
- 일정 기간 동안만 유지되는 보조 브랜치
  - feature: 기능을 개발하는 브랜치
  - release: 이번 출시 버전을 준비하는 브랜치
  - hotfix: 출시 버전에서 발생한 버그를 수정하는 브랜치



## 예시

1. upstream/feature-user 브랜치에서 작업 브랜치(bfm-100_login_layout)를 생성합니다.

   > (feature-user)]$ git fetch upstream
   > (feature-user)]$ git checkout -b bfm-100_login_layout –track upstream/feature-user

2. 작업 브랜치에서 소스코드를 수정합니다. (뚝딱뚝딱 :hammer:)

3. 작업 브랜치에서 변경사항을 커밋합니다. (보통은 vi editor에서 커밋 메세지를 작성 함)

   > (bfm-100_login_layout)]$ git commit -m "BFM-100 로그인 화면 레이아웃 생성"

4. 만약 커밋이 불필요하게 어려 개로 나뉘어져 있다면 squash를 합니다. (커밋 2개를 합쳐야 한다면)

   > (bfm-100_login_layout)]$ git rebase -i HEAD~2

5. 작업 브랜치를 upstream/feature-user에 rebase합니다.

   > (bfm-100_login_layout)]$ git pull –rebase upstream feature-user

6. 작업 브랜치를 origin에 push합니다.

   > (bfm-100_login_layout)]$ git push origin bfm-100_login_layout

7. Github에서 bfm-100_login_layout 브랜치를 feature-user에 merge하는 Pull Request를 생성합니다.

8. 같은 feature를 개발하는 동료에게 리뷰 승인을 받은 후 자신의 Pull Request를 merge합니다. 만약 혼자 feature를 개발한다면 1~2명의 동료에게 리뷰 승인을 받은 후 Pull Request를 merge합니다.
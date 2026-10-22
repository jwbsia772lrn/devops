### 4주차 | 리눅스 심화, 네트워크 기초 & Git 협업
- `ps aux`로 실행 중인 프로세스를 확인하고, `tar` 옵션을 활용해 파일을 압축·해제하며 `diff -rq`로 디렉터리 차이를 비교하는 방법을 배웠다.
- `grep`과 `find`를 활용한 로그 검색, `ss`와 `curl`을 이용한 네트워크 점검, 그리고 GitHub PR과 Merge 충돌 해결 흐름을 익혔다
5주차 | Docker 기초 & Issue 관리

### 5주차 | 도커 기초와 GitHub Issue 관리
- 가상머신(VM)과 컨테이너의 차이를 이해하고, `docker run`, `ps`, `logs`, `exec` 등 기본 CLI 명령어 사용법을 습득했다.
- GitHub Issue로 작업 목표를 정의하고, PR 작성 후 Merge해서 MainBranch를 안전을 보장하며 다른 작업을 진행하고 병합하는 방법을 익혔다.

### 6주차 | Dockerfile과 이미지 배포
- `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD` 등 핵심 지시어를 활용해 애플리케이션을 이미지로 빌드하는 Dockerfile 작성법을 배웠다.
- 레이어 캐시를 고려한 빌드 최적화 기법과 GHCR/Docker Hub 푸시, `buildx`를 이용한 멀티 아키텍처 빌드 과정을 실습했다.

### 7주차 | Docker Compose와 멀티 컨테이너 운영
- `compose.yaml`을 작성해 웹 앱과 DB 등 여러 컨테이너를 하나의 서비스로 묶어 연동하고 제어하는 방법을 배웠다.
- 데이터 보존을 위한 Volume 설정, `.env` 파일 기반 환경변수 분리, `healthcheck` 준비 상태 검사 및 Nginx 로드 밸런싱 구조를 익혔다.

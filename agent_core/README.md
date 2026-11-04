# Python 학습 및 실습 기록

## 1. 소개

SKT ALEPH 교육 과정에서 Python 기초 문법과 라이브러리 활용 방법을 학습하고 있습니다.

직접 작성한 Python 코드와 실행 결과를 GitHub에 기록하며, 학습 과정에서 이해한 내용과 발생한 오류 및 해결 과정을 날짜별로 정리합니다.

## 2. 학습 내용

### 2.1 Python 기초 문법
- Python 파일: `agent_core/main.py`
- 실행 방법: Mac 터미널에서 `python3 agent_core/main.py`
- 실행 결과: `10`
- 변수와 자료형
- 조건문(`if`, `else`)
- 반복문(`for`, `range()`)
- 조건에 맞는 값의 합계와 개수 계산

### 2.2 자료구조
- 리스트와 인덱스를 이용한 데이터 조회
- `for` 반복문을 이용한 리스트 순회
- 딕셔너리의 키(Key)와 값(Value)
- 딕셔너리의 값 조회, 수정 및 새로운 키 추가
- `get()`과 `in`을 이용한 키 조회 및 존재 여부 확인
- 리스트 안의 딕셔너리와 딕셔너리 안의 딕셔너리 구조

### 2.3 Python 실행 환경
- macOS와 VS Code에서 Python 실행
- Python 가상환경(`.venv`) 생성 및 활용
- `pip`를 이용한 외부 라이브러리 설치
- `requests` 라이브러리 설치 및 버전 확인
- VS Code에서 Python 실행 환경 설정

### 2.4 예외 처리
- `try-except`를 이용한 오류 처리
- `ValueError`: 숫자로 변환할 수 없는 값 처리
- `IndexError`: 존재하지 않는 리스트 인덱스 접근 처리
- `FileNotFoundError`: 존재하지 않는 파일 접근 처리

### 2.5 파일 입출력
- 텍스트 파일 읽기, 쓰기 및 이어 쓰기
- `with open()`을 이용한 파일 관리
- CSV 파일 생성 및 데이터 조회
- 특정 계정의 로그 검색

### 2.6 JSON
- JSON 데이터 형식과 사용 목적 이해
- 직렬화(Serialization)와 역직렬화(Deserialization)
- `json.dumps()`와 `json.loads()`를 이용한 문자열 변환 및 복원
- `json.dump()`와 `json.load()`를 이용한 JSON 파일 저장 및 읽기
- 리스트 안의 딕셔너리를 JSON으로 저장하고 복원

### 2.7 Git과 GitHub
- `git config`를 이용한 사용자 정보 확인 및 설정
- `git status`를 통한 변경된 파일 확인
- Untracked, Tracked, Staged 상태 이해
- `git add`로 커밋할 파일 선택
- `git commit`으로 변경 사항 기록
- `git push`로 GitHub 원격 저장소에 업로드
- `git add .`을 이용한 변경 파일 일괄 스테이징
- `.gitignore`를 이용한 불필요한 파일 및 민감정보 제외

### 2.8 Python 함수
- `def`를 이용한 함수 정의 및 호출
- 매개변수를 이용한 입력값 전달
- `return`을 이용한 결과 반환
- `print()`와 `return`의 차이
- 함수와 조건문을 결합한 판단 기능 구현
- 입력값 및 비교 연산자 변경을 통한 실행 결과 비교

### 2.9 네트워크·ZT 운영 기초
- Wireshark의 개념과 보안 관제에서의 활용
- 패킷(Packet)과 Npcap의 역할 이해
- macOS의 패킷 캡처 환경 및 ChmodBPF 이해
- 파이프(`|`)와 `grep`을 이용한 명령어 결과 필터링
- `network_zt` 실습 폴더 생성

## 3. 작성한 파일

### 3.1 Python 기본 실행 및 환경 설정
- `main.py`: Python 기본 코드 실행 및 결과 `10` 확인
- `check_requests.py`: requests 라이브러리 설치 및 버전 확인
- `check_environment.py`: flask, requests, schedule을 불러와 Python 실행 환경 확인

### 3.2 Network-002 · 조건 판단
- `assignment_02_f1.py`: Python 기초 조건문 실습
- `assignment_02_f2.py`: Python 기초 조건문 실습

### 3.3 Network-003 · 리스트와 반복문
- `assignment_03_f1.py`: 리스트에 저장된 계정을 순서대로 출력
- `assignment_03_f2.py`: `range(1, 4)`를 사용해 `1`, `2`, `3` 출력

### 3.4 Network-004 · 조건에 맞는 값과 합계
- `assignment_04_f1.py`: 조건문과 반복문을 이용한 값 계산
- `assignment_04_f2.py`: 조건에 맞는 값의 개수와 합계 계산, counts의 첫 번째 값을 0에서 7로 변경한 후 `3 16` 출력 확인

### 3.5 Network-005 · 예외 처리
- `assignment_05_f1.py`: 숫자로 변환할 수 없는 입력에서 발생하는 ValueError 처리
- `assignment_05_f2.py`: 숫자가 아닌 값 `bad`를 건너뛰고 합계 `5` 계산, 존재하지 않는 리스트 인덱스에 접근할 때 발생하는 IndexError 처리

### 3.6 Network-006 · 파일 입출력
- `assignment_06_ex.py`: example.txt에 `예제 실행`을 작성하고 다시 읽어 출력
- `assignment_06_f1.py`: memo.txt에 내용을 이어 쓰고 다시 읽기, sample_logs.csv에서 `park03` 로그 2건 조회, check.txt에 점검 결과 작성 및 확인
- `assignment_06_f2.py`: 파일이 없을 때 FileNotFoundError를 처리하고 `파일 위치를 확인하세요` 출력

### 3.7 Network-008 · 딕셔너리 및 JSON (2026-11-03)
- `assignment_08_f1.py`: 딕셔너리에서 `user`와 `count` 키를 이용해 값을 조회하고 `kim01 4` 출력
- `assignment_08_f2.py`: 사용자 정보가 담긴 리스트를 `logs.json` 파일로 저장한 뒤 다시 읽어 첫 번째 사용자의 이름 `kim01` 출력

### 3.8 Python 함수 실습 (2026-11-04)
- 필수 F1: `greet()` 함수를 정의하고 서로 다른 이름을 전달하여 인사 문자열 반환
- 필수 F2: `check_failures()` 함수를 정의하고 실패 횟수에 따라 판단 결과 반환

주요 학습 내용:
- 매개변수를 활용한 입력값 전달
- `return`을 이용한 함수의 결과 반환
- 함수 내부에서 조건문 활용
- 경계값 2와 3을 이용한 조건 확인
- `>=`와 `>`의 비교 연산자 변경 실험

주요 학습 내용:
- 딕셔너리의 키를 이용한 값 조회 및 수정
- 존재하지 않는 키를 조회할 때 발생하는 KeyError 이해
- `get()`으로 오류 없이 기본값 반환
- `in`을 이용한 키 존재 여부 확인
- 리스트 안의 딕셔너리와 딕셔너리 안의 딕셔너리 구분
- JSON 직렬화 및 역직렬화
- JSON 파일 저장과 복원

## 4. 실행 방법

### 4.1 Python 파일 실행

프로젝트 최상위 폴더에서 실행합니다.

```bash
python3 agent_core/main.py
```

개별 과제 실행 예시:

```bash
python3 agent_core/assignment_08_f1.py
python3 agent_core/assignment_08_f2.py
```

### 4.2 GitHub 업로드

```bash
git status
git add <파일명>
git commit -m "커밋 메시지"
git push origin main
```

변경된 파일을 확인한 후 필요한 파일을 선택하여 GitHub에 업로드합니다.

## 5. 날짜별 학습 기록

실습 과정에서 작성한 코드, 변경한 값, 실행 결과, 오류 및 해결 과정은 `docs` 폴더에 날짜별로 기록합니다.

- [2026-10-26 학습 기록](../docs/2026-10-26.md): Python 기초 실습 및 학습 기록
- [2026-10-27 학습 기록](../docs/2026-10-27.md): 조건문과 반복문, 조건에 맞는 값과 합계 계산
- [2026-10-28 학습 기록](../docs/2026-10-28.md): requests 설치 및 리스트·반복문 실습
- [2026-10-29 학습 기록](../docs/2026-10-29.md): VS Code 실행 환경 설정 및 예외 처리
- [2026-10-30 학습 기록](../docs/2026-10-30.md): 텍스트 파일 입출력, CSV 로그 조회 및 파일 오류 처리
- [2026-11-03 학습 기록](../docs/2026-11-03.md): Git 명령어 학습, 딕셔너리 및 JSON 저장·복원 실습
- [2026-11-04 학습 기록](docs/2026-11-04.md): Wireshark 및 패킷 분석 기초, Python 함수 정의와 반환값, F1·F2 실습

## 6. 학습 기록 관리

- Python 실습 코드는 `agent_core` 폴더에서 관리합니다.
- 네트워크·ZT 운영 실습 파일은 `network_zt` 폴더에서 관리합니다.
- 날짜별 학습 내용과 실행 결과는 `docs` 폴더에 기록합니다.
- README.md에는 전체 학습 내용과 작성한 파일의 역할을 요약합니다.
- 새로운 과제를 완료하면 실습 파일, 학습 기록 및 README.md를 함께 업데이트합니다.
- GitHub에 업로드하기 전에 API 키, 비밀번호, 개인정보 등 민감한 정보가 포함되어 있지 않은지 확인합니다.


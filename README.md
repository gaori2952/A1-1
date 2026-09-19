# 프롬프트 관리 프로그램

## 프로그램 설명

Python으로 제작한 콘솔 기반 프롬프트 관리 프로그램입니다. 실행 중 프롬프트를
추가, 조회, 검색하고 즐겨찾기를 관리할 수 있습니다. 프로그램을 종료하면 실행
중 추가한 데이터는 초기화됩니다.

## 개발 환경

- Visual Studio Code
- Python 3.11.3
- Git 2.55.0.windows.5

## 실행 방법

```bash
py main.py
```

또는

```bash
python main.py
```

테스트 실행:

```bash
python -m unittest test_main.py -v
```

## 주요 기능

- 전체 프롬프트 보기
- 카테고리별 조회
- 프롬프트 상세 보기
- 프롬프트 추가
- 프롬프트 검색
- 즐겨찾기 추가/해제
- 즐겨찾기 목록 보기
- 프로그램 종료

## 카테고리

- 업무
- 학습
- 글쓰기
- 아이디어
- 기타
- 사용자가 직접 입력한 카테고리

## 데이터 구조

- Python 리스트와 딕셔너리를 사용합니다.
- 각 프롬프트는 `title`, `content`, `category`, `favorite` 정보를 가집니다.

## GitHub 저장소

https://github.com/gaori2952/A1-1

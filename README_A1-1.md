# A1-1 Prompt Manager

Python 기본 문법과 Git/GitHub를 활용하여 구현한 콘솔 기반 프롬프트 관리 프로그램입니다.

## 프로젝트 구조

```text
A1-1/
├── main.py
├── test_main.py
├── README.md
└── .gitignore
```

- `main.py`: 프롬프트 관리 프로그램 본체
- `test_main.py`: 주요 기능 테스트
- `README.md`: 프로젝트 설명 및 실행 방법
- `.gitignore`: Python 캐시/가상환경 등 불필요한 파일 제외

## 개발 환경

- Windows
- Visual Studio Code
- Python 3.11.3
- Git 2.55.0.windows.5
- GitHub

## 실행 방법

프로젝트 폴더에서 다음 명령을 실행합니다.

```bash
py main.py
```

또는

```bash
python main.py
```

## 주요 기능

1. 전체 프롬프트 보기
2. 카테고리별 조회
3. 프롬프트 상세 보기
4. 프롬프트 추가
5. 프롬프트 검색
6. 즐겨찾기 추가/해제
7. 즐겨찾기 목록 보기
8. 종료

잘못된 메뉴 번호나 문자 입력 시 프로그램이 종료되지 않고 다시 입력하도록 처리합니다.

## 기본 프롬프트 데이터

프로그램 시작 시 다음 3개의 프롬프트가 기본으로 등록됩니다.

- 회의 내용 요약
- 이메일 작성
- 아이디어 브레인스토밍

각 프롬프트는 Python의 리스트와 딕셔너리를 이용하여 다음 정보를 저장합니다.

```python
{
    "title": "프롬프트 제목",
    "content": "프롬프트 내용",
    "category": "카테고리",
    "favorite": False
}
```

## 카테고리

기본 카테고리:

- 업무
- 학습
- 글쓰기
- 아이디어
- 기타

프롬프트 추가 시 기존 카테고리를 선택하거나 새로운 카테고리를 직접 입력할 수 있습니다.

## 코드 구조

기능별로 함수를 분리하여 구현했습니다.

```text
read_non_empty()
read_menu_choice()
choose_category()
display_prompt()
list_prompts()
show_by_category()
show_prompt_detail()
add_prompt()
search_prompts()
toggle_favorite()
show_favorites()
print_menu()
run_program()
```

## 테스트

Python 표준 라이브러리 `unittest`를 이용하여 주요 기능을 테스트할 수 있습니다.

```bash
python -m unittest test_main.py -v
```

## Git / GitHub 요구사항

프로젝트 과정에서 다음 Git 명령을 사용했습니다.

```text
init
add
commit
push
pull
checkout
clone
merge
```

`feature/prompt-list` 브랜치에서 프롬프트 목록 기능을 개선한 뒤 `main` 브랜치에 병합했습니다.

공개 저장소 Clone 실습:

```bash
git clone https://github.com/octocat/Spoon-Knife.git sample-clone
```

Git 로그 확인:

```bash
git log --oneline --graph --all
```

GitHub 저장소에는 10개 이상의 커밋이 기록되어 있습니다.

## Repository

https://github.com/gaori2952/A1-1

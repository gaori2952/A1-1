# A1-1 Prompt Manager

Python 기본 문법과 Git/GitHub를 활용하여 구현한 콘솔 기반 프롬프트 관리 프로그램입니다.

여러 생성형 AI 프롬프트를 한 곳에서 관리할 수 있도록 프롬프트 추가, 전체 조회, 카테고리별 조회, 검색, 상세 보기, 즐겨찾기 기능을 구현했습니다.

프로그램 실행 중 추가하거나 변경한 데이터는 유지되며, 프로그램을 종료하면 초기화됩니다.

---

## 프로젝트 구조

```text
A1-1/
├── main.py
├── test_main.py
├── README.md
├── A1-1_프롬프트관리프로그램_최종보고서.docx
└── .gitignore
```

- `main.py`: 프롬프트 관리 프로그램 본체
- `test_main.py`: 주요 기능 테스트
- `README.md`: 프로젝트 설명 및 실행 방법
- `A1-1_프롬프트관리프로그램_최종보고서.docx`: 개발 환경, 프로그램 실행 결과, Git/GitHub 수행 과정 및 증빙 자료를 정리한 최종 보고서
- `.gitignore`: Python 캐시 및 불필요한 파일 제외

---

## 개발 환경

- Windows
- Visual Studio Code
- Python 3.11.3
- Git 2.55.0.windows.5
- GitHub

Python 3.10 이상을 사용해야 하는 과제 조건을 충족합니다.

Python/Git 버전 확인, Git 사용자 설정, 기본 브랜치 설정 등 실제 개발환경 설정 결과는 별도의 최종 보고서에 캡처 자료로 첨부했습니다.

---

## 실행 방법

프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
py main.py
```

또는

```bash
python main.py
```

프로그램을 실행하면 다음 메뉴가 출력됩니다.

```text
===== 프롬프트 관리 프로그램 =====

1. 전체 프롬프트 보기
2. 카테고리별 조회
3. 프롬프트 상세 보기
4. 프롬프트 추가
5. 프롬프트 검색
6. 즐겨찾기 추가/해제
7. 즐겨찾기 목록 보기
8. 종료
```

실제 실행 화면은 별도의 최종 보고서에 첨부했습니다.

---

## 주요 기능

### 1. 전체 프롬프트 보기

현재 등록되어 있는 모든 프롬프트를 번호와 함께 출력합니다.

각 프롬프트의 제목, 카테고리, 내용, 즐겨찾기 여부를 확인할 수 있으며 목록 하단에는 현재 조회된 프롬프트의 총 개수를 표시합니다.

프롬프트가 없는 경우에는 별도의 안내 메시지를 출력합니다.

---

### 2. 카테고리별 조회

현재 등록된 프롬프트의 카테고리를 보여주고, 사용자가 원하는 카테고리를 선택하면 해당 카테고리의 프롬프트만 조회합니다.

실제 카테고리 선택 및 조회 결과는 별도의 최종 보고서에 첨부했습니다.

---

### 3. 프롬프트 상세 보기

프롬프트 번호를 입력하면 해당 프롬프트의 전체 정보를 출력합니다.

출력 정보:

- 제목
- 카테고리
- 즐겨찾기 여부
- 전체 내용

잘못된 번호를 입력하면 올바른 범위의 번호를 다시 입력하도록 처리했습니다.

---

### 4. 프롬프트 추가

새로운 프롬프트를 등록할 수 있습니다.

입력 항목:

- 제목
- 내용
- 카테고리

제목이나 내용을 입력하지 않으면 다시 입력하도록 처리했습니다.

카테고리는 기존 목록에서 선택하거나 새로운 카테고리를 직접 입력할 수 있습니다.

새로운 프롬프트의 즐겨찾기 기본값은 `False`입니다.

---

### 5. 프롬프트 검색

검색어가 프롬프트의 제목 또는 내용에 포함되어 있는지 확인하여 검색 결과를 출력합니다.

영문 검색의 경우 `.lower()`를 사용하여 대소문자를 구분하지 않습니다.

검색 결과가 없는 경우에도 안내 메시지를 출력합니다.

---

### 6. 즐겨찾기 추가/해제

프롬프트 번호를 선택하여 즐겨찾기 상태를 변경할 수 있습니다.

```text
False → True
True → False
```

새로운 프롬프트의 즐겨찾기 초기값은 `False`이며, 프로그램 실행 중에는 변경 상태가 유지됩니다.

---

### 7. 즐겨찾기 목록

즐겨찾기 상태가 `True`인 프롬프트만 별도로 조회할 수 있습니다.

실제 즐겨찾기 추가/해제 및 목록 조회 결과는 별도의 최종 보고서에 첨부했습니다.

---

## 기본 프롬프트 데이터

프로그램 시작 시 다음 3개의 프롬프트가 기본으로 등록됩니다.

- 회의 내용 요약
- 이메일 작성
- 아이디어 브레인스토밍

각 프롬프트는 다음 정보를 포함합니다.

```python
{
    "title": "프롬프트 제목",
    "content": "프롬프트 내용",
    "category": "카테고리",
    "favorite": False
}
```

---

## 데이터 구조

프롬프트 데이터는 Python의 리스트(List)와 딕셔너리(Dictionary)를 사용하여 관리합니다.

예시:

```python
prompts = [
    {
        "title": "회의 내용 요약",
        "content": "다음 회의 내용을 핵심 내용, 결정 사항, 할 일로 나누어 요약해줘.",
        "category": "업무",
        "favorite": False
    }
]
```

### List

여러 개의 프롬프트를 순서대로 저장하는 용도로 사용합니다.

장점:

- 여러 데이터를 순서대로 관리하기 쉽습니다.
- `append()`를 이용하여 새로운 데이터를 쉽게 추가할 수 있습니다.
- 반복문을 통한 전체 조회가 간단합니다.

단점:

- 데이터가 많아질 경우 검색 시 리스트 전체를 순차적으로 확인해야 합니다.

### Dictionary

프롬프트 하나의 제목, 내용, 카테고리, 즐겨찾기 여부처럼 여러 속성을 하나의 데이터로 묶는 용도로 사용합니다.

장점:

- `title`, `category`처럼 의미 있는 Key를 이용하여 데이터에 접근할 수 있습니다.
- 하나의 프롬프트에 여러 속성을 구조적으로 저장할 수 있습니다.

단점:

- Key 이름을 정확하게 관리해야 합니다.

따라서 본 프로그램에서는 여러 프롬프트를 List에 저장하고, 각 프롬프트의 세부 정보는 Dictionary로 관리합니다.

---

## 카테고리

기본 카테고리는 다음과 같습니다.

```text
업무
학습
글쓰기
아이디어
기타
```

프롬프트를 추가할 때 기존 카테고리를 선택하거나 새로운 카테고리를 직접 입력할 수 있습니다.

현재 필수 구현에서는 카테고리 수정, 삭제, 병합 기능은 포함하지 않았습니다.

해당 기능은 과제의 필수 요구사항에 포함되지 않으므로 현재 버전에서는 구현하지 않았습니다.

---

## 입력 검증

잘못된 입력으로 인해 프로그램이 종료되지 않도록 입력 검증 기능을 구현했습니다.

예:

```text
메뉴 번호: 99
→ 1부터 8 사이의 번호를 입력해 주세요.
```

```text
메뉴 번호: abc
→ 숫자로 입력해 주세요.
```

제목이나 내용이 비어 있는 경우:

```text
입력값을 비워 둘 수 없습니다.
```

메시지를 출력하고 다시 입력하도록 처리했습니다.

실제 입력 오류 처리 결과는 별도의 최종 보고서에 첨부했습니다.

---

## 검색 방식

프롬프트 검색은 사용자가 입력한 키워드가 제목 또는 내용에 포함되어 있는지를 검사합니다.

```python
if keyword in prompt["title"].lower() or keyword in prompt["content"].lower()
```

영문 검색의 경우 대소문자를 구분하지 않습니다.

현재 프로그램은 소규모 개인용 프롬프트 관리 프로그램을 대상으로 하므로 리스트를 순차적으로 검색하는 방식으로 구현했습니다.

---

## 데이터 유지 방식

현재 필수 구현에서는 별도의 데이터베이스나 JSON 파일을 사용하지 않습니다.

프로그램 실행 중에는 다음 정보가 유지됩니다.

- 새롭게 추가한 프롬프트
- 즐겨찾기 변경 상태

프로그램을 종료하면 실행 중 변경한 데이터는 초기화됩니다.

이는 과제의 필수 요구사항인 프로그램 실행 중 데이터 유지 조건을 충족합니다.

JSON 저장 및 불러오기를 이용한 영속화는 선택형 보너스 과제이므로 현재 버전에는 포함하지 않았습니다.

---

## 코드 구조

모든 코드를 하나의 함수에 몰아넣지 않고 기능별로 함수를 분리했습니다.

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

주요 함수 역할은 다음과 같습니다.

| 함수 | 역할 |
|---|---|
| `read_non_empty()` | 빈 입력 방지 |
| `read_menu_choice()` | 숫자 및 메뉴 범위 검증 |
| `choose_category()` | 카테고리 선택 및 직접 입력 |
| `display_prompt()` | 프롬프트 한 개 출력 |
| `list_prompts()` | 프롬프트 목록 출력 |
| `show_by_category()` | 카테고리별 조회 |
| `show_prompt_detail()` | 프롬프트 상세 정보 출력 |
| `add_prompt()` | 새로운 프롬프트 추가 |
| `search_prompts()` | 제목 및 내용 검색 |
| `toggle_favorite()` | 즐겨찾기 추가 및 해제 |
| `show_favorites()` | 즐겨찾기 목록 출력 |
| `print_menu()` | 메인 메뉴 출력 |
| `run_program()` | 전체 프로그램 실행 흐름 관리 |

---

## 테스트

Python 표준 라이브러리 `unittest`를 이용하여 주요 기능을 테스트할 수 있습니다.

```bash
python -m unittest test_main.py -v
```

주요 테스트 항목:

- 기본 프롬프트 개수 확인
- 필수 데이터 필드 확인
- 카테고리별 조회
- 프롬프트 검색
- 즐겨찾기 상태 변경

---

## Git 사용자 설정

Git 사용자 이름과 이메일을 설정하고 기본 브랜치를 `main`으로 지정했습니다.

```bash
git config --global user.name
git config --global user.email
git config --global init.defaultBranch
```

실제 설정 결과는 개인정보가 포함될 수 있으므로 README에 직접 노출하지 않고 별도의 최종 보고서에 캡처 자료로 첨부했습니다.

---

## Git / GitHub 사용

프로젝트 과정에서 다음 Git 명령어를 실제로 사용했습니다.

```text
git init
git add
git commit
git push
git pull
git checkout
git clone
git merge
```

각 명령어의 실제 수행 화면과 결과는 별도의 최종 보고서에 첨부했습니다.

---

## GitHub 코드 업로드

프로젝트 코드는 다음 GitHub 저장소에서 관리합니다.

https://github.com/gaori2952/A1-1

최종 저장소 구조:

```text
A1-1/
├── main.py
├── test_main.py
├── README.md
├── A1-1_프롬프트관리프로그램_최종보고서.docx
└── .gitignore
```

GitHub 저장소의 파일 목록, 커밋 상태, 원격 저장소 연결 결과는 별도의 최종 보고서에 첨부했습니다.

---

## Branch 및 Merge

프롬프트 목록 기능은 별도의 브랜치에서 작업했습니다.

```text
feature/prompt-list
```

브랜치 생성:

```bash
git checkout -b feature/prompt-list
```

해당 브랜치에서 프롬프트 목록 출력 기능을 개선했습니다.

대표 커밋:

```text
feat: 프롬프트 목록 출력 개선
```

작업 완료 후 `main` 브랜치로 이동하여 변경사항을 병합했습니다.

```bash
git checkout main
git merge feature/prompt-list
git push origin main
```

브랜치를 분리한 이유는 `main` 브랜치와 독립된 환경에서 목록 기능을 수정한 뒤, 기능이 정상적으로 동작하는 것을 확인한 후 병합하기 위해서입니다.

브랜치 및 병합 이력은 다음 명령으로 확인했습니다.

```bash
git log --oneline --graph --all
```

실제 Git 로그와 브랜치 그래프는 별도의 최종 보고서에 첨부했습니다.

---

## Commit 관리

프로젝트의 기능 구현, 테스트, 문서화 작업을 커밋 단위로 관리했습니다.

GitHub 저장소에는 10개 이상의 커밋이 존재합니다.

대표적인 커밋:

```text
feat: 프롬프트 목록 출력 개선
Add prompt category and detail views
Test category prompt lookup
Test search and favorite features
Add tests for default prompt data
Implement prompt management CLI
docs: README 프로젝트 설명 보강
chore: 프로젝트 초기 설정
```

전체 커밋 이력은 별도의 최종 보고서에 첨부한 `git log --oneline --graph --all` 결과에서 확인할 수 있습니다.

---

## Clone 실습

Git의 `clone` 명령을 이용하여 공개 GitHub 저장소를 로컬 환경으로 복제했습니다.

사용한 공개 저장소:

```text
https://github.com/octocat/Spoon-Knife
```

실행 명령:

```bash
git clone https://github.com/octocat/Spoon-Knife.git sample-clone
```

Clone 후 다음 명령을 사용하여 파일 구조와 Git 로그를 확인했습니다.

```bash
dir
git log --oneline -5
git status
```

실제 Clone 실행 결과와 파일 구조, Git 로그는 별도의 최종 보고서에 첨부했습니다.

---

## `.gitignore`

Python이 자동으로 생성하는 캐시 파일과 개발 과정에서 불필요한 파일이 GitHub에 업로드되지 않도록 설정했습니다.

```gitignore
__pycache__/
*.py[cod]

.venv/
venv/
env/

.pytest_cache/
.coverage
```

---

## 상세 보고서

프로젝트 개발 과정과 실제 실행 증빙 자료는 아래 보고서에서 확인할 수 있습니다.

[최종 개발 보고서](./A1-1_프롬프트관리프로그램_최종보고서.docx)

보고서에는 다음 내용이 포함되어 있습니다.

- VSCode 프로젝트 구성
- Python 3.11.3 버전 확인
- Git 2.55.0.windows.5 버전 확인
- Git `user.name`, `user.email` 설정
- 기본 브랜치 `main` 설정
- GitHub 원격 저장소 연결
- GitHub 코드 업로드 결과
- 프로그램 메인 메뉴
- 프롬프트 추가
- 전체 프롬프트 조회
- 카테고리별 조회
- 프롬프트 검색
- 프롬프트 상세 보기
- 즐겨찾기 추가/해제
- 즐겨찾기 목록
- 잘못된 번호 입력 처리
- 문자 입력 처리
- 프로그램 정상 종료
- `feature/prompt-list` 브랜치 생성
- 브랜치 작업 및 병합
- `git log --oneline --graph --all`
- 10개 이상의 커밋 확인
- 공개 저장소 Clone
- Clone 저장소 파일 구조
- Clone 저장소 Git 로그
- GitHub 저장소 최종 화면

---



---

## Repository

https://github.com/gaori2952/A1-1

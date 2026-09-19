"""초보자를 위한 프롬프트 관리 프로그램입니다."""


# 프로그램을 시작할 때 보여 줄 기본 카테고리입니다.
CATEGORIES = ["업무", "학습", "글쓰기", "아이디어", "기타"]

# PRD에서 정한 기본 프롬프트 3개입니다.
DEFAULT_PROMPTS = [
	{
		"title": "회의 내용 요약",
		"content": "다음 회의 내용을 핵심 내용, 결정 사항, 할 일로 나누어 요약해줘.",
		"category": "업무",
		"favorite": False,
	},
	{
		"title": "이메일 작성",
		"content": "다음 내용을 정중하고 간결한 비즈니스 이메일로 작성해줘.",
		"category": "업무",
		"favorite": False,
	},
	{
		"title": "아이디어 브레인스토밍",
		"content": "다음 주제에 대해 서로 다른 관점의 아이디어를 5개 제안해줘.",
		"category": "아이디어",
		"favorite": False,
	},
]


def read_non_empty(prompt):
	"""빈 입력을 받지 않도록 반복해서 입력받습니다."""
	while True:
		value = input(prompt).strip()
		if value:
			return value
		print("입력값을 비워 둘 수 없습니다.")


def read_menu_choice(prompt, minimum, maximum):
	"""메뉴 번호가 숫자이며 정해진 범위인지 확인합니다."""
	while True:
		value = input(prompt).strip()
		try:
			choice = int(value)
		except ValueError:
			print("숫자로 입력해 주세요.")
			continue

		if minimum <= choice <= maximum:
			return choice
		print(f"{minimum}부터 {maximum} 사이의 번호를 입력해 주세요.")


def choose_category():
	"""기본 카테고리를 선택하거나 새 카테고리를 직접 입력받습니다."""
	print("카테고리 선택")
	for index, category in enumerate(CATEGORIES, start=1):
		print(f"{index}. {category}")
	print(f"{len(CATEGORIES) + 1}. 직접 입력")

	choice = read_menu_choice("카테고리 번호: ", 1, len(CATEGORIES) + 1)
	if choice == len(CATEGORIES) + 1:
		return read_non_empty("새 카테고리: ")
	return CATEGORIES[choice - 1]


def display_prompt(prompt, number=None):
	"""프롬프트 한 개를 읽기 쉬운 형식으로 출력합니다."""
	prefix = f"{number}. " if number is not None else ""
	favorite_mark = "[즐겨찾기] " if prompt["favorite"] else ""
	print(f"{prefix}{favorite_mark}{prompt['title']} ({prompt['category']})")
	print(f"   {prompt['content']}")


def list_prompts(prompts, title="전체 프롬프트"):
	"""프롬프트 목록을 출력하고, 목록이 비어 있으면 안내합니다."""
	print(f"\n--- {title} ---")
	if not prompts:
		print("표시할 프롬프트가 없습니다.")
		return

	for number, prompt in enumerate(prompts, start=1):
		display_prompt(prompt, number)

	print(f"총 {len(prompts)}개의 프롬프트")


def show_by_category(prompts):
	"""선택한 카테고리에 속한 프롬프트만 출력합니다."""
	categories = []
	for prompt in prompts:
		if prompt["category"] not in categories:
			categories.append(prompt["category"])

	if not categories:
		print("조회할 프롬프트가 없습니다.")
		return

	print("\n--- 카테고리별 조회 ---")
	for number, category in enumerate(categories, start=1):
		print(f"{number}. {category}")
	choice = read_menu_choice("카테고리 번호: ", 1, len(categories))
	category = categories[choice - 1]
	results = [prompt for prompt in prompts if prompt["category"] == category]
	list_prompts(results, f"{category} 카테고리")


def show_prompt_detail(prompts):
	"""선택한 프롬프트의 제목, 카테고리, 내용을 자세히 출력합니다."""
	if not prompts:
		print("상세 정보를 볼 프롬프트가 없습니다.")
		return

	list_prompts(prompts, "프롬프트 상세 보기")
	number = read_menu_choice("상세히 볼 프롬프트 번호: ", 1, len(prompts))
	prompt = prompts[number - 1]
	print("\n--- 프롬프트 상세 정보 ---")
	print(f"제목: {prompt['title']}")
	print(f"카테고리: {prompt['category']}")
	print(f"즐겨찾기: {'예' if prompt['favorite'] else '아니오'}")
	print(f"내용: {prompt['content']}")


def add_prompt(prompts):
	"""제목, 내용, 카테고리를 입력받아 새 프롬프트를 추가합니다."""
	print("\n--- 프롬프트 추가 ---")
	title = read_non_empty("제목: ")
	content = read_non_empty("내용: ")
	category = choose_category()
	prompts.append(
		{
			"title": title,
			"content": content,
			"category": category,
			"favorite": False,
		}
	)
	print("프롬프트를 추가했습니다.")


def search_prompts(prompts):
	"""검색어가 제목 또는 내용에 포함된 프롬프트를 찾습니다."""
	print("\n--- 프롬프트 검색 ---")
	keyword = read_non_empty("검색어: ").lower()
	results = [
		prompt
		for prompt in prompts
		if keyword in prompt["title"].lower()
		or keyword in prompt["content"].lower()
	]
	list_prompts(results, f"'{keyword}' 검색 결과")


def toggle_favorite(prompts):
	"""선택한 프롬프트의 즐겨찾기 상태를 추가 또는 해제합니다."""
	if not prompts:
		print("즐겨찾기를 변경할 프롬프트가 없습니다.")
		return

	list_prompts(prompts, "즐겨찾기 변경")
	number = read_menu_choice("변경할 프롬프트 번호: ", 1, len(prompts))
	prompt = prompts[number - 1]
	prompt["favorite"] = not prompt["favorite"]
	state = "추가" if prompt["favorite"] else "해제"
	print(f"'{prompt['title']}' 즐겨찾기를 {state}했습니다.")


def show_favorites(prompts):
	"""즐겨찾기로 표시된 프롬프트만 출력합니다."""
	favorites = [prompt for prompt in prompts if prompt["favorite"]]
	list_prompts(favorites, "즐겨찾기 목록")


def print_menu():
	"""메인 메뉴를 출력합니다."""
	print("\n===== 프롬프트 관리 프로그램 =====")
	print("1. 전체 프롬프트 보기")
	print("2. 카테고리별 조회")
	print("3. 프롬프트 상세 보기")
	print("4. 프롬프트 추가")
	print("5. 프롬프트 검색")
	print("6. 즐겨찾기 추가/해제")
	print("7. 즐겨찾기 목록 보기")
	print("8. 종료")


def run_program():
	"""메뉴를 반복해서 보여 주고 사용자의 선택을 처리합니다."""
	prompts = [prompt.copy() for prompt in DEFAULT_PROMPTS]
	print("프롬프트 관리 프로그램을 시작합니다.")

	while True:
		print_menu()
		choice = read_menu_choice("메뉴 번호: ", 1, 8)

		if choice == 1:
			list_prompts(prompts)
		elif choice == 2:
			show_by_category(prompts)
		elif choice == 3:
			show_prompt_detail(prompts)
		elif choice == 4:
			add_prompt(prompts)
		elif choice == 5:
			search_prompts(prompts)
		elif choice == 6:
			toggle_favorite(prompts)
		elif choice == 7:
			show_favorites(prompts)
		else:
			print("프로그램을 종료합니다.")
			break


if __name__ == "__main__":
	run_program()

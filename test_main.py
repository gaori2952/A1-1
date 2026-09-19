import unittest
from unittest.mock import patch

import main


class PromptManagementTests(unittest.TestCase):
    def test_default_prompts_have_at_least_three_items(self):
        self.assertGreaterEqual(len(main.DEFAULT_PROMPTS), 3)

    def test_default_prompts_have_required_fields(self):
        for prompt in main.DEFAULT_PROMPTS:
            self.assertIn("title", prompt)
            self.assertIn("content", prompt)
            self.assertIn("category", prompt)
            self.assertIn("favorite", prompt)

    def test_category_view_shows_selected_category(self):
        prompts = [prompt.copy() for prompt in main.DEFAULT_PROMPTS]
        with patch("builtins.input", return_value="1"):
            with patch("builtins.print") as mocked_print:
                main.show_by_category(prompts)

        output = " ".join(str(call) for call in mocked_print.call_args_list)
        self.assertIn("업무 카테고리", output)

    def test_search_finds_prompt_by_title(self):
        prompts = [prompt.copy() for prompt in main.DEFAULT_PROMPTS]
        with patch("builtins.input", return_value="이메일"):
            with patch("builtins.print") as mocked_print:
                main.search_prompts(prompts)

        output = " ".join(str(call) for call in mocked_print.call_args_list)
        self.assertIn("이메일 작성", output)

    def test_toggle_favorite_changes_favorite_state(self):
        prompts = [prompt.copy() for prompt in main.DEFAULT_PROMPTS]
        with patch("builtins.input", return_value="1"):
            main.toggle_favorite(prompts)

        self.assertTrue(prompts[0]["favorite"])


if __name__ == "__main__":
    unittest.main()
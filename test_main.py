import unittest

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


if __name__ == "__main__":
    unittest.main()
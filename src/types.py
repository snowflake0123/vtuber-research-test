from typing import TypedDict

# 辞書の型定義
Category = TypedDict("Category", {"3d": list[int], "2d": list[int], "liveAction": list[int]})
Question = TypedDict("Question", {"gameplay": Category, "news": Category, "study": Category})
Questionnaire = dict[str, Question]

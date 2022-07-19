import os
import csv
from . import types
from . import freedman
from . import steelDwass


def readDirs(path: str) -> list[str]:
  """path にあるディレクトリ一覧を返す"""
  return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


def createQuestionnaireDictionary(questionnairePath: str) -> types.Questionnaire:
  results: types.Questionnaire = {}
  questionDirs = readDirs(questionnairePath)
  for question in questionDirs:
    results[question]: types.Question = {}
    questionPath = os.path.join(questionnairePath, question)
    categoryDirs = readDirs(questionPath)
    for category in categoryDirs:
      results[question][category]: types.Category = {}
      categoryPath = os.path.join(questionPath, category)
      with open(os.path.join(categoryPath, "result.csv"), encoding="utf8", newline="") as f:
        results[question][category]["3d"] = []
        results[question][category]["2d"] = []
        results[question][category]["liveAction"] = []
        csvReader = csv.reader(f)
        _header = next(csvReader)
        for row in csvReader:
          results[question][category]["3d"].append(int(row[0]))
          results[question][category]["2d"].append(int(row[1]))
          results[question][category]["liveAction"].append(int(row[2]))
  return results


def main(questionnairePath: str) -> None:
  questionnaireDictionary = createQuestionnaireDictionary(questionnairePath)
  questions = sorted(list(questionnaireDictionary.keys()))

  # 質問ごとに Friedman 検定を実施する
  for question in questions:
    print(f"Question: {question}")
    q = questionnaireDictionary[question]
    print()
    # カテゴリ（ゲーム実況、ニュース解説、学習解説）で比較
    freedman.compareByCategory(q)
    print()
    # 配信スタイル（3D, 2D, 実写）で比較
    freedman.compareByStreamingStyle(q)
    print()
    print()

  # 質問ごとに Steel-Dwass 検定を実施する
  for question in questions:
    print(f"Question: {question}")
    q = questionnaireDictionary[question]
    print()
    # カテゴリ（ゲーム実況、ニュース解説、学習解説）で比較
    steelDwass.compareByCategory(q)
    print()
    # 配信スタイル（3D, 2D, 実写）で比較
    steelDwass.compareByStreamingStyle(q)
    print()
    print()

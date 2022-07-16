import os
import csv
from typing import TypedDict
from scipy import stats


FRIEDMAN_P_THRESHOLD = 0.05


# 辞書の型定義
Category = TypedDict("Category", {"3d": list[int], "2d": list[int], "liveAction": list[int]})
Question = TypedDict("Question", {"gameplay": Category, "news": Category, "study": Category})
Questionnaire = dict[str, Question]


def readDirs(path: str) -> list[str]:
  """path にあるディレクトリ一覧を返す"""
  return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


def createQuestionnaireDictionary(questionnairePath: str) -> Questionnaire:
  results: Questionnaire = {}
  questionDirs = readDirs(questionnairePath)
  for question in questionDirs:
    results[question]: Question = {}
    questionPath = os.path.join(questionnairePath, question)
    categoryDirs = readDirs(questionPath)
    for category in categoryDirs:
      results[question][category]: Category = {}
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


def isSignificantDifference(pValue: float):
  return pValue < FRIEDMAN_P_THRESHOLD


def compareByCategory(question: Question) -> None:
  """カテゴリ（ゲーム実況、ニュース解説、学習解説）で比較する"""
  print("<< Friedman Test of Comparison by Category >>")

  styles = list(question["gameplay"].keys())
  for style in styles:
    print(f"Streaming Style: {style}")
    gameplay = question["gameplay"][style]
    news = question["news"][style]
    study = question["study"][style]
    # print(f"gameplay = {gameplay}")
    # print(f"news = {news}")
    # print(f"study = {study}")
    result = stats.friedmanchisquare(gameplay, news, study)
    print(result)
    print(f"Significant Difference: {isSignificantDifference(result.pvalue)}")


def compareByStreamingStyle(question: Question) -> None:
  """配信スタイル（3D, 2D, 実写）で比較する"""
  print("<< Friedman Test of Comparison by Streaming Style >>")

  categories = list(question.keys())
  for category in categories:
    print(f"Category: {category}")
    threeD = question[category]["3d"]
    twoD = question[category]["2d"]
    liveAction = question[category]["liveAction"]
    # print(f"3d = {threeD}")
    # print(f"2d = {twoD}")
    # print(f"liveAction = {liveAction}")
    result = stats.friedmanchisquare(threeD, twoD, liveAction)
    print(result)
    print(f"Significant Difference: {isSignificantDifference(result.pvalue)}")


def main():
  questionnairePath = "../questionnaire"
  questionnaireDictionary = createQuestionnaireDictionary(questionnairePath)
  questions = sorted(list(questionnaireDictionary.keys()))

  # 質問ごとに Friedman 検定を実施する
  for question in questions:
    print(f"Question: {question}")
    q = questionnaireDictionary[question]
    print()
    # カテゴリ（ゲーム実況、ニュース解説、学習解説）で比較
    compareByCategory(q)
    print()
    # 配信スタイル（3D, 2D, 実写）で比較
    compareByStreamingStyle(q)
    print()
    print()

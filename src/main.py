import os
import csv


def readDirs(path: str) -> list[str]:
  """path にあるディレクトリ一覧を返す"""
  return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


def createQuestionnaireDictionary(questionnairePath: str) -> dict:
  results = {};
  questionDirs = readDirs(questionnairePath)
  for question in questionDirs:
    results[question] = {}
    questionPath = os.path.join(questionnairePath, question)
    categoryDirs = readDirs(questionPath)
    for category in categoryDirs:
      results[question][category] = {}
      categoryPath = os.path.join(questionPath, category)
      with open(os.path.join(categoryPath, "result.csv"), encoding="utf8", newline="") as f:
        results[question][category]["3d"] = []
        results[question][category]["2d"] = []
        results[question][category]["liveAction"] = []
        csvReader = csv.reader(f)
        _header = next(csvReader)
        for row in csvReader:
          results[question][category]["3d"].append(row[0])
          results[question][category]["2d"].append(row[1])
          results[question][category]["liveAction"].append(row[2])
  return results


def main():
  questionnairePath = "../questionnaire"
  questionnaireDictionary = createQuestionnaireDictionary(questionnairePath)
  print(questionnaireDictionary)

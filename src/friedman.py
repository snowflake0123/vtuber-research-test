from scipy import stats
from . import types


P_THRESHOLD = 0.05


def isSignificantDifference(pValue: float):
  return pValue < P_THRESHOLD


def compareByCategory(question: types.Question) -> None:
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
    print()


def compareByStreamingStyle(question: types.Question) -> None:
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
    print()

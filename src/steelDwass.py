import pandas as pd
import scikit_posthocs as sp
from . import types


P_THRESHOLD = 0.05


def isSignificantDifference(pValue: float):
  return pValue < P_THRESHOLD


def compareByCategory(question: types.Question) -> None:
  """カテゴリ（ゲーム実況、ニュース解説、学習解説）で比較する"""
  print("<< Steel-Dwass Test of Comparison by Category >>")

  styles = list(question["gameplay"].keys())
  for style in styles:
    print(f"Streaming Style: {style}")
    gameplay = question["gameplay"][style]
    news = question["news"][style]
    study = question["study"][style]
    # print(f"gameplay = {gameplay}")
    # print(f"news = {news}")
    # print(f"study = {study}")
    # result = sp.posthoc_dscf([gameplay, news, study]);
    df = pd.DataFrame({"gameplay": gameplay, "news": news, "study": study})
    df = df.melt(var_name='groups', value_name='values')
    result = sp.posthoc_dscf(df, val_col='values', group_col='groups')
    print(result)
    print()
    print(f"gameplay - news : {isSignificantDifference(result['gameplay']['news'])}")
    print(f"news - study : {isSignificantDifference(result['news']['study'])}")
    print(f"study - gameplay : {isSignificantDifference(result['study']['gameplay'])}")
    print()
    print()


def compareByStreamingStyle(question: types.Question) -> None:
  """配信スタイル（3D, 2D, 実写）で比較する"""
  print("<< Steel-Dwass Test of Comparison by Streaming Style >>")

  categories = list(question.keys())
  for category in categories:
    print(f"Category: {category}")
    threeD = question[category]["3d"]
    twoD = question[category]["2d"]
    liveAction = question[category]["liveAction"]
    # print(f"3d = {threeD}")
    # print(f"2d = {twoD}")
    # print(f"liveAction = {liveAction}")
    # result = sp.posthoc_dscf([threeD, twoD, liveAction])
    df = pd.DataFrame({ "threeD": threeD, "twoD": twoD, "liveAction": liveAction })
    df = df.melt(var_name='groups', value_name='values')
    result = sp.posthoc_dscf(df, val_col='values', group_col='groups')
    print(result)
    print()
    print(f"threeD - twoD : {isSignificantDifference(result['threeD']['twoD'])}")
    print(f"twoD - liveAction : {isSignificantDifference(result['twoD']['liveAction'])}")
    print(f"liveAction - threeD : {isSignificantDifference(result['liveAction']['threeD'])}")
    print()
    print()


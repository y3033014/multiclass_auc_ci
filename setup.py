from setuptools import setup, find_packages
import multiclass_auc_ci

DESCRIPTION = "multiclass_auc_ci: Calculate multiclass auc confidence interval"
NAME = "multiclass_auc_ci"
AUTHOR = "Yuta INOUE"
AUTHOR_EMAIL = "inoue.yuta.d9@s.gifu-u.ac.jp"
URL = "https://github.com/" #githubURL、本番は何を書く？自分のメールアドレスのアカウント？学校のメールアドレスで新しく作る？
LICENSE = "" #ライセンスかな？本番は何になるんだろう
DOWNLOAD_URL = URL
VERSION = multiclass_auc_ci.__version__
PYTHON_REQUIRES = ">=3.6" #pythonの必要なバージョンかな。これも調べる
INSTALL_REQUIRES = [
    "pytz>=2020.1" #依存するパッケージの情報。必要なバージョンとかね。
]
PACKAGES = [
    "multiclass_auc_ci" #パッケージ情報
]
KEYWORDS = "" #検索でヒットさせたいキーワード
CLASSIFIRES = [
    "" #分類情報(ライセンス情報とプログラミング言語を記載)
    ""
]

setup(
    name="multiclass_auc_ci",
    version=VERSION,
    packages=find_packages()
)
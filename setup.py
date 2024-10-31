from setuptools import setup, find_packages

DESCRIPTION = "multiclass_auc_ci: Calculate multiclass auc confidence interval"
NAME = "multiclass_auc_ci"
AUTHOR = "Yuta INOUE"
AUTHOR_EMAIL = "inoue.yuta.d9@s.gifu-u.ac.jp"
URL = "https://github.com/y3033014/multiclass_auc_ci" #githubURL、本番は何を書く？自分のメールアドレスのアカウント？学校のメールアドレスで新しく作る？
LICENSE = "BSD 3-Clause" #ライセンス
DOWNLOAD_URL = "https://github.com/y3033014/multiclass_auc_ci"
# VERSION = multiclass_auc_ci.__version__
PYTHON_REQUIRES = ">=3.11" #pythonの必要なバージョンかな。これも調べる
INSTALL_REQUIRES = [
    "openpyxl>=3.1.2", #依存するパッケージの情報。必要なバージョンとかね。
    "numpy>=1.26.2",
    "scipy>=1.13.0",
    "scikit-learn>=1.4.2"
]
PACKAGES = [
    "multiclass_auc_ci" #パッケージ情報
]
KEYWORDS = "multiclass auc confidence interval" #検索でヒットさせたいキーワード
CLASSIFIRES = [
    "License :: OSI Approved :: BSD License", #分類情報(ライセンス情報とプログラミング言語を記載)
    "Programming Language :: Python :: 3.11"
]

with open("README.md","r") as fp:
    readme = fp.read()
long_description = readme

setup(
    name="multiclass_auc_ci",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    license=LICENSE,
    url=URL,
    # version=VERSION,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=PACKAGES,
    classifiers=CLASSIFIRES
)
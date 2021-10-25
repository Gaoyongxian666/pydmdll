import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydmdll",
    version="0.0.6",
    author="Gaoyongxian666",
    author_email="g1695698547@163.com",
    description="大漠插件dm.dll的Python接口",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gaoyongxian666/pydmdll",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pywin32"],
    include_package_data=True,
    package_data={'pydmdll': ["dm.dll"]},
    project_urls={
        'Bug Reports': 'https://github.com/Gaoyongxian666/pydmdll',
        'Source': 'https://github.com/Gaoyongxian666/pydmdll',
    },
)

# 笔记1：mkdocs.yml和项目同级在根目录，保证/docs/低一级就可以
# 在readthedocs网站上mkdocstrings安装，你提供requirements.txt就好
# 不用生成site文件夹，没有太大用
# Linux不允许导入pywin32，可以用try

# 笔记2：package_data={'pydmdll': ["dm.dll"]},包名可不是随便写的
# python setup.py sdist bdist_wheel生成文件
# twine upload dist/*

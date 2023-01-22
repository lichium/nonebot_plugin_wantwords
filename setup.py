import io
import sys

import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_wantwords",
    version="0.1.0",
    author="limnium",
    author_email="limnium@yeah.com",
    keywords=["nonebot2", "nonebot", "nonebot_plugin"],
    description="""use wantwords as a plugin of nonebot""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/limnium/nonebot_plugin_wantwords",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=['nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0', 'nonebot2>=2.0.0-beta.1,<3.0.0', 'httpx>=0.19.0']
)

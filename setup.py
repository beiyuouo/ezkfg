from setuptools import find_packages, setup
import os
import ezkfg

base_dir = os.path.dirname(os.path.abspath(__file__))
__version__ = "0.0.6a2"


setup(
    name="ezkfg",
    version=__version__,
    keywords=["configuration", "config"],
    description="Easy Configuration",
    long_description=open(os.path.join(base_dir, "README.md")).read(),
    long_description_content_type="text/markdown",
    author="Bingjie Yan",
    author_email="bj.yan.pa@qq.com",
    url="http://github.com/beiyuouo/ezkfg",
    license="Apache-2.0 License",
    packages=find_packages(include=["ezkfg", "ezkfg.*", "LICENSE", "README.md"]),
    install_requires=["PyYAML"],
    python_requires=">=3.6",
)

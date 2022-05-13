from setuptools import find_packages, setup
import os
import ezkfg

base_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name="ezkfg",
    version=ezkfg.__version__,
    keywords=["configuration", "config"],
    description="Easy Configuration",
    long_description=open(os.path.join(base_dir, "README.md")).read(),
    long_description_content_type="text/markdown",
    author="Bingjie Yan",
    author_email="bj.yan.pa@qq.com",
    url="http://github.com/beiyuouo/ezkfg",
    license="Apache-2.0 License",
    packages=find_packages(),
)

#!/usr/bin/env python
import io
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


def read(*names, **kwargs):
    return io.open(
        path.join(here, *names), encoding=kwargs.get("encoding", "utf8")
    ).read()


requirements = [r for r in read("requirements.txt").split("\n") if r]

setup(
    name="sphinx-test",
    version="0.0.0",
    install_requires=requirements,
    packages=find_packages(),
)

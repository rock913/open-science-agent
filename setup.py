from setuptools import setup, find_packages

setup(
    name="open_science_agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "open-science-agent=open_science_agent.cli.main:main",
        ],
    },
)

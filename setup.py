import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    more_description = f.read()

setuptools.setup(
    name="com",
    version="0.0.1",
    author="Thareq",
    author_email="realryangames@gmail.com",
    description= "com library for bca banking",
    more_description = more_description,
    more_description_content_type="text/markdown"
    url="https://github.com/catdogman/banking_package",
    license = "MIT",
    packages = ["com"],
)
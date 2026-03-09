from setuptools import setup, find_packages

# Minimal dependencies — torch/torchvision/torchaudio/pytorchvideo
# are provided by the parent project to avoid version conflicts.
setup(
    name="imagebind",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        "imagebind": ["bpe/bpe_simple_vocab_16e6.txt.gz"],
    },
    description="ImageBind: One Embedding Space To Bind Them All",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/facebookresearch/ImageBind",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "timm",
        "ftfy",
        "regex",
        "einops",
        "iopath",
        "types-regex",
    ],
)

from setuptools import setup, find_packages

setup(
    name="beansframework",
    version="0.1.0",
    author="Beans the Lightkeeper",
    description="Recursive agent framework for glyph-based AI infrastructure",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'beans = beansframework.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        # If you have any special packages you need (like numpy, click, etc), list here
    ],
    python_requires='>=3.8',
)

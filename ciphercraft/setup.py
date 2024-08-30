from setuptools import setup, find_packages

setup(
    name="cipher-craftt",
    version="0.1.11",
    description="A simple password generator tool.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Mayur Tembhare",
    author_email="tembharemayur@gmail.com",
    url="https://github.com/jarvismayur/ciphercraft",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cipher_craftt = cipher_craftt.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.6',
)

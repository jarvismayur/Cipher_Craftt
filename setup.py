from setuptools import setup, find_packages

setup(
    name="cipher-craftt",
    version="0.1.18",
    description="A comprehensive tool for password management including generation, strength checking, expiry tracking, and secure sharing.",
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
    install_requires=[
        'cryptography',  # Add cryptography here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Adjusted to Beta to reflect a more stable version
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',  # Added for clarity on compatibility
    ],
    python_requires='>=3.6',
    package_data={
        'cipher_craftt': ['wordlist/languages/*.txt'],  # Include wordlists in the package
    },
)

from setuptools import setup, find_packages

setup(
    name='LectureAid',
    version='1.0.0',
    packages=find_packages(),
    description='Upload lecture PDFs and get relevant URLs to helpful websites',
    tests_require=['pytest'],
    author='CSC510 - Group 21',
    author_email='',
    url='https://github.com/mtkumar123/CSC510_Project_LectureAid',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Topic :: LectureAid",
    ],
    license='MIT',
    install_requires=[
        'pytest',
    ]
)

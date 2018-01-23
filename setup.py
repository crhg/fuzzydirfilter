from setuptools import setup, find_packages

setup(
    name='fuzzydirfilter',
    version='1.0',
    packages=find_packages(),
    install_requires=['fuzzywuzzy'],
    entry_points={
        'console_scripts':
            'fuzzydirfilter = fuzzydirfilter.main:fuzzydirfilter_main'
    },
    zip_safe=False,
    classifiers=[
          'Environment :: Console',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
    ],
)

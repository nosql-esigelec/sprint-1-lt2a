from setuptools import setup, find_packages

setup(
    name='sprint-1-lt2a',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi',
        'python-dotenv',
        'pytest',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'sprint-1-lt2a = api.main:app',
        ],
    },
)
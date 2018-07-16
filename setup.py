from distutils.core import setup

setup(
    name='record-manager',
    version='0.1.0',
    packages=['record_manager'],
    entry_points={
        'console_scripts': ['record-manager=record_manager.cli:main']
    }
)
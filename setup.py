from distutils.core import setup

setup(
    name='record-manager',
    version='0.2.0',
    packages=['record_manager'],
    entry_points={
        'console_scripts': [
            'record-manager=record_manager.cli:main',
            'record-manager-rest=record_manager.rest:main'
        ]
    },
    install_requires=['Flask']
)
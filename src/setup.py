from setuptools import setup

requires=[
    'pyramid==2.0',
    'pyramid_mako',
    'pyramid_tm',
    'sqlalchemy',
    'graphene-sqlalchemy>=2.0',
    'waitress',
    'zope.sqlalchemy'

]

dev_requires=[
    'pyramid_debugtoolbar',
    'webtest',
    'pytest',
]

setup(
    name='simple_server',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory':[
            'main = simple_server:main'
        ],
    },
)
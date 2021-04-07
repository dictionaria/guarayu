from setuptools import setup


setup(
    name='cldfbench_guarayu',
    py_modules=['cldfbench_guarayu'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'guarayu=cldfbench_guarayu:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'pydictionaria>=2.0',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)

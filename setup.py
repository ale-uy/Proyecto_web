from setuptools import setup, find_packages

setup(
    name='mi_web',
    version='1.0.0',
    description='Mi aplicación web con Flask',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'mi_web=mi_web.app:main',
        ],
    },
)

from distutils.core import setup

setup(
    name="AoE2_API",
    version="0.0.1",
    install_requires = [
        'requests',
        'pydantic',
        'aenum',
    ]
)

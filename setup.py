from setuptools import setup

setup(
    name="restaurant_orders",
    description="Projeto Restaurant Orders",
    install_requires=["pypubsub==4.0.3"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)

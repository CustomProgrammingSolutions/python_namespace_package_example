from setuptools import setup

setup(
    name='example_base',

    version='1.0.0',

    description='The base package',
    long_description='''An example of namespace packages, this is the base package.

The idea is that there's some greetings in plugins that are installed separetely.
This base package loads them and prints them out''',

    author='Janis Lesinskis',

    packages=['greeter_example'],
    zip_safe=False,
)

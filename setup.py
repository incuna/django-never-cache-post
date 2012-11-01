from setuptools import setup, find_packages


setup(
    name='django-never-cache-post',
    packages=find_packages(),
    include_package_data=True,
    version=0.1,
    description='Ensure that (iOS 6) never caches the result of an ajax POST again.',
    long_description=open('README.md').read(),
    author='Incuna Ltd.',
    author_email='admin@incuna.com',
    url='http://github.com/incuna/django-never-cache-post/',
    install_requires=[],
    zip_safe=False,
)

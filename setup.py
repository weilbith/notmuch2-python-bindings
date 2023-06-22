import setuptools

setuptools.setup(
    name='notmuch2',
    version='0.31.3',
    description='Pythonic bindings for the notmuch mail database using CFFI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Floris Bruynooghe, Thore Weilbier',
    author_email='flub@devork.be, thore@weilbier.net',
    url='https://github.com/weilbith/notmuch2-python-bindings.git',
    license='GPL-3.0',
    setup_requires=['cffi>=1.0.0'],
    install_requires=['cffi>=1.0.0'],
    packages=setuptools.find_packages(exclude=['tests']),
    cffi_modules=['notmuch2/_build.py:ffibuilder'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries',
    ],
)

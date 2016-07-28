from setuptools import setup

setup(
    name='simple-nose-selenium',
    version='0.01',
    author='Felix Descoteaux',
	author_email = 'flx.descoteaux@gmail.com',
	description = 'Run your TestCase\'s in multiple browsers',
	py_modules = ['simple_nose_selenium'],
	entry_points = {
		'nose.plugins.0.10': [
			'simple-nose-selenium = simple_nose_selenium:SimpleNoseSelenium'
		]
	},
    url='http://github.com/felix-d/simple-nose-selenium',
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='nose selenium webdriver',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=['selenium', 'nose', 'unittest2'],
)

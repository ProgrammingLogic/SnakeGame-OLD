from setuptools import setup, find_packages

setup(
	name = "SnakeGame",
	version = "0.0.1",
	install_requires = [
	    "pygame"
	],
	packages = ['SnakeGame'],
	entry_points = {
		'console_scripts': [
			'SnakeGame = SnakeGame.__main__:main'
		]
	},
)

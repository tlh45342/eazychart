.DEFAULT_GOAL := oldstyle

oldstyle:
	python setup.py bdist_wheel

ink:
	python -m pip wheel --wheel-dir=dist eazychart
	
dist:
	python3 -m build --sdist

wheel:
	python3 -m build --wheel eazychart
	
clean:
	rm -rf dist
	rm -rf build
	rm -rf eazychart.egg-info
	pip uninstall eazychart -y

install:
	pip install dist\eazychart-0.1.0-py3-none-any.whl
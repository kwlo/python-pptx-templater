upload:
	rm -rf build/ dist/
	./versioning.sh
	mv VERSION.new VERSION
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: dist

develop:
	python setup.py develop

dist:
	python setup.py sdist

clean:
	rm -rf *egg* dist


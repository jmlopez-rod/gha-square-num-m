mypy:
	mypy src

action:
	m github actions src/pkg/actions.py

tests:
	./src/tests/run.sh
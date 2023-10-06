mypy:
	mypy src

action:
	m github actions src/pkg/actions.py

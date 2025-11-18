.PHONY: format lint check test help

help:
	@echo "Available commands:"
	@echo "  make format    - Format all Python files"
	@echo "  make lint      - Lint all Python files"
	@echo "  make check     - Run both format and lint"
	@echo "  make test      - Run Django tests"

format:
	@echo "Formatting Python files..."
	cd source && python3 -m ruff format .
	@echo "✓ Formatting complete"

lint:
	@echo "Linting Python files..."
	cd source && python3 -m ruff check --fix .
	@echo "✓ Linting complete"

check: format lint
	@echo "✓ All checks complete"

test:
	cd source && python3 manage.py test


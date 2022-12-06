# testing-with-pytest

Install package: pip install -e .

Run tests: pytest

Run tests with coverage: pytest --cov=<package>, e.g.: pytest --cov=numeric.numbers

Run tests and collect HTML coverage output: pytest --cov-report=html --cov=numeric.numbers 

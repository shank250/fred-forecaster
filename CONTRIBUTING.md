# Contributing to fred-forecaster

Thanks for your interest in contributing to fred-forecaster! This document provides guidelines and workflows for contributing.

## Development Workflow

1. **Fork and Clone**
   ```bash
   git clone https://github.com/your-username/fred-forecaster.git
   cd fred-forecaster
   ```

2. **Set up Development Environment**
   ```bash
   # Create and activate virtual environment (optional but recommended)
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   .\venv\Scripts\activate  # Windows

   # Install development dependencies
   pip install -e ".[dev]"
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature-name
   ```

4. **Make Changes and Test**
   ```bash
   # Format code
   black .
   isort .

   # Run linters
   flake8 fred_forecaster
   mypy fred_forecaster

   # Run tests
   pytest  # Regular tests
   pytest --run-slow  # Include slow tests
   pytest --cov=fred_forecaster  # Test coverage
   ```

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

6. **Push and Create Pull Request**
   ```bash
   git push origin feature-name
   ```
   Then create a pull request on GitHub.

## Code Style Guidelines

- Follow PEP 8 style guide
- Use [Black](https://black.readthedocs.io/) for code formatting (line length = 79)
- Sort imports with isort
- Add type hints to all function parameters and return values
- Write docstrings for all public functions, classes, and modules (NumPy style)
- Include unit tests for new functionality

## Pull Request Process

1. Ensure all tests pass and code is formatted
2. Update documentation if needed
3. Add your changes to CHANGELOG.md
4. Link any related issues
5. Request review from maintainers

## Running CI/CD Locally

The repository uses GitHub Actions for CI/CD. You can test these workflows locally:

```bash
# Install act (https://github.com/nektos/act)
# Then run:
act -n  # Dry run
act pull_request  # Test PR workflow
```

## Release Process

1. Update version in:
   - fred_forecaster/__init__.py
   - pyproject.toml
   - setup.cfg

2. Create and push tag:
   ```bash
   git tag -a vX.Y.Z -m "Version X.Y.Z"
   git push origin vX.Y.Z
   ```

3. CI will automatically:
   - Build package
   - Run tests
   - Publish to PyPI
   - Create GitHub release

## Getting Help

- Open an issue for bugs or feature requests
- Start a discussion for questions
- Tag @MaxGhenis for urgent matters

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

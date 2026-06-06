# Simple Sum App

A simple Python 3.12 program that calculates the sum of numeric values.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Testing

```bash
# Run tests
python -m pytest test_main.py -v
```

## CI/CD

This project includes a complete GitHub Actions CI/CD pipeline with:
- Build
- Unit Tests
- Integration Tests
- Non-regression Tests
- SonarCloud Code Analysis
- Deployment to Preprod

## Secrets needed in GitHub repo:
- `SONAR_TOKEN` (for SonarCloud)
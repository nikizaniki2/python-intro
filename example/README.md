# Python virtualenvs
- Create with `python -m venv venv`
- Option to specify python version (`--python=<path to specific python>`)
- Activate `.\venv\Scripts\activate`
- Organize dependencies/ requirements - `pip freeze > 'requirements.txt'`
- Always install dependencies only in python environment
- Close env - `deactivate`

# Pytest
- `pip install pytest`
- In console (`Ctrl + J`) -> `pytest`. Executest files with `test_` prefix.
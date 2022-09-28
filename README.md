# Pytest-bdd
This repository contains example code for the
*Behavior-Driven Python with pytest-bdd* 

## Setup
This project requires an up-to-date version of Python 3.
It also uses [pipenv](https://pipenv.readthedocs.io/) to manage packages.

To set up this project on your local machine:
1. Clone it from this GitHub repository and open the project in the terminal.
2. Run `pipenv install` from the command line in the project's root directory (it will create virtual env with all dependencies available in the PipFile).
3. After virtual env created, select it on your IDE.
4. For Web UI tests, install the appropriate browser and WebDriver executable.
   * These tests use Firefox and [geckodriver](https://github.com/mozilla/geckodriver/releases).

## Running Tests
Run tests simply using the `pytest` command.

Depending upon your environment, it may be better to use `python -m pytest`.
If you are using `pipenv`, then run `pipenv run python -m pytest`.

To Run parallel test install pytest xdist using command `pip install pytest-xdist`
To run parallel tests run command `pipenv run python -m pytest -n 2`

Run the following command to generate pytest html reports `pipenv run python -m pytest -v -rs --html=Reports/PytestHtmlReport/report.html --self-contained-html`

## More Info




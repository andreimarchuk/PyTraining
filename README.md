# PyTraining

Repository


2. Install and activate virtual environment
3. Run -->  python -m pip install allure-pytest
4. Run -->  python -m pip install -r requirements.txt
5. Run -->  python -m pytest bdd/ --alluredir=bdd/reports -vvv --gherkin-terminal-reporter
6. Run -->  allure serve bdd/reports
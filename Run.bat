
pytest -- browser edge

pytest -rA  --browser edge testCases/test_Login.py
pytest -rA  --browser chrome testCases/test_Login.py
pytest -rA -n=4  --browser chrome testCases/test_login_param.py
pytest -rA -n=4  --browser chrome --html=Reports/report_param.html  testCases/test_login_param.py


rem nidaq_scope invocation script

set PYTHONPATH=.\\WPy64-39100\\python-3.9.10.amd64
set PATH=%PATH%;.\\WPy64-39100\python-3.9.10.amd64\Scripts
%PYTHONPATH%\\python -X tracemalloc .\nidaq_scope_gui.py
pause

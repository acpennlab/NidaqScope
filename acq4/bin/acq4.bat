rem ACQ4 invocation script  (www.acq4.org)

rem :::: Some possible additions to this file. Uncomment and edit as needed. ::::

rem :::: Activate a conda environment? ::::
call C:\ProgramData\Miniconda3\Scripts\activate.bat acq4

rem :::: Start in a specific directory? ::::
call cd C:\Users\Public\Programs\acq4\acq4

set PYTHONPATH=C:\ProgramData\Miniconda3\Lib\site-packages

python -m acq4
pause

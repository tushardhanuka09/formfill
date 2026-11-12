@echo off
title AcSIR Societal Program Survey App
echo ======================================================================
echo Starting AcSIR Survey Web Application & PDF Form Generator...
echo ======================================================================
echo.
echo The survey application will open in your default web browser.
echo Press Ctrl+C in this window when you wish to stop the application.
echo.

start "" http://localhost:5000/
python app.py
pause


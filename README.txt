File Renaming Tool
Overview

This project is a lightweight, browser-based tool for batch renaming image files using configurable naming rules. It was built to automate a repetitive file-organisation task that was time-consuming and error-prone when done manually.

The tool focuses on rapid usability: visual previews, drag-and-drop assignment, and rule-based renaming, rather than manual scripting.

Features

Load images directly from a local directory

Drag-and-drop files into rename rule groups

Rule-based naming with pattern placeholders

Live filename previews before applying changes

Batch renaming with conflict checks

Simple web UI with no external dependencies

Tech Stack

Backend: Python (Flask)

Frontend: HTML, CSS, Vanilla JavaScript

Architecture: Local web app (Flask API + static frontend)

Development style: AI-assisted, rapid prototyping

The motivation was to remove repetitive manual work involved in renaming large numbers of files that needed to follow strict naming conventions. Instead of repeatedly renaming files by hand or writing one-off scripts, this tool provides a reusable, visual workflow that reduces mistakes and speeds up the process.

How It Works

A Flask backend exposes simple APIs to list files, generate thumbnails, and perform renaming.

The frontend allows users to define naming rules and assign files visually.

Before renaming, the tool generates previews so users can verify results.

Renaming is applied in bulk, with safeguards against overwriting existing files.

Running the Project Locally
pip install flask flask-cors
python app.py

Then open a browser and navigate to:

http://localhost:5000

(Alternatively, run run_flask.bat on Windows.)

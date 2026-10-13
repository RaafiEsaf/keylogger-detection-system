\# System Architecture



\## Overview



The Keylogger Detection System is a Python-based defensive prototype that analyzes simulated activity events and produces a risk assessment.



\## Components



1\. \*\*Main application (`main.py`)\*\* — Coordinates the analysis workflow.

2\. \*\*Detection engine (`detector.py`)\*\* — Calculates a risk score from predefined indicators.

3\. \*\*Behavioral analysis (`behavioral\_analysis.py`)\*\* — Counts events and identifies selected suspicious patterns.

4\. \*\*Statistical analysis (`statistical\_analysis.py`)\*\* — Calculates event frequencies and identifies repeated events.

5\. \*\*Process monitor (`process\_monitor.py`)\*\* — Reports basic operating-system and process information.

6\. \*\*Report generator (`report\_generator.py`)\*\* — Saves results as timestamped JSON files.



\## Workflow



1\. Load predefined simulated events.

2\. Analyze event patterns and frequencies.

3\. Identify recognized suspicious indicators.

4\. Calculate the risk score and risk level.

5\. Generate a JSON report.

6\. Display a summary in the terminal.



\## Data Flow



`Simulated Events → Behavioral Analysis → Statistical Analysis → Risk Scoring → JSON Report`



\## Current Scope



The prototype does not capture keystrokes or currently perform real-world keylogger detection. Its results demonstrate the analysis workflow using predefined events.




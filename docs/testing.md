\# Testing Documentation



\## Testing Framework



The project uses Python's built-in `unittest` framework.



\## Test Modules



\### Behavioral Analysis

Tests event counting, suspicious event identification, and empty input handling.



\### Statistical Analysis

Tests total event counting, average frequency calculation, repeated event identification, and empty input handling.



\### Detection Engine

Tests high-risk scoring, low-risk scoring, score limits, and unknown indicator handling.



\## Run All Tests



From the project root directory, execute:



```powershell

py -m unittest discover -s tests -v

```



\## Current Results



The initial test suite contains 11 automated unit tests. All 11 passed during the latest recorded test run.



Run the test command again before publishing to verify the current code.



\## Limitations



These tests verify the behavior of the implemented functions using controlled inputs. They do not establish real-world keylogger detection accuracy.






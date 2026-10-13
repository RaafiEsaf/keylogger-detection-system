\# Detection Methodology



\## Objective



Demonstrate a defensive approach to identifying potentially suspicious activity indicators without recording keystrokes or collecting user input.



\## Test Data



The current prototype uses predefined simulated events, including:



\- `normal\_activity`

\- `suspicious\_process`

\- `unexpected\_persistence`

\- `unusual\_resource\_usage`

\- `suspicious\_network\_activity`



These labels represent test scenarios, not confirmed malicious behavior.



\## Risk Scoring



Each recognized indicator has a predefined weight. The system adds the weights of the supplied indicators and caps the result at 100.



Risk levels are assigned as follows:



\- \*\*LOW:\*\* Score below 35

\- \*\*MEDIUM:\*\* Score from 35 to 69

\- \*\*HIGH:\*\* Score of 70 or above



\## Behavioral Analysis



The behavioral module counts event occurrences and reports selected suspicious event types.



\## Statistical Analysis



The statistical module calculates total events, average occurrences per distinct event type, and repeated event counts.



\## Limitations



The weights and thresholds are illustrative. They have not been validated against a real-world dataset, and a high score does not establish that a system is infected.




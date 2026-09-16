"""
Keylogger Detection System
Main detection engine.

This module evaluates system and behavioral indicators
to identify potentially suspicious keylogging activity.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class DetectionResult:
    """Represents the result of a detection analysis."""

    risk_score: int
    indicators: List[str]
    status: str


class KeyloggerDetector:
    """Defensive detector for suspicious keylogging behavior."""

    def __init__(self):
        self.indicators = []

    def analyze_indicators(self, indicators: List[str]) -> DetectionResult:
        """
        Analyze a list of observed behavioral indicators.

        The detector uses a simple scoring model for the
        initial version of the project.
        """

        risk_score = 0
        detected_indicators = []

        indicator_weights = {
            "suspicious_process": 30,
            "keyboard_monitoring": 30,
            "unusual_activity": 20,
            "abnormal_frequency": 20,
        }

        for indicator in indicators:
            if indicator in indicator_weights:
                risk_score += indicator_weights[indicator]
                detected_indicators.append(indicator)

        risk_score = min(risk_score, 100)

        if risk_score >= 70:
            status = "HIGH RISK"
        elif risk_score >= 40:
            status = "MEDIUM RISK"
        else:
            status = "LOW RISK"

        return DetectionResult(
            risk_score=risk_score,
            indicators=detected_indicators,
            status=status,
        )


if __name__ == "__main__":
    detector = KeyloggerDetector()

    sample_indicators = [
        "suspicious_process",
        "keyboard_monitoring",
        "abnormal_frequency",
    ]

    result = detector.analyze_indicators(sample_indicators)

    print("=== Keylogger Detection Result ===")
    print(f"Risk Score : {result.risk_score}/100")
    print(f"Status     : {result.status}")
    print("Indicators :")

    for indicator in result.indicators:
        print(f"  - {indicator}")

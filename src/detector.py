"""Core detection engine for the Keylogger Detection System."""

from dataclasses import dataclass


@dataclass
class DetectionResult:
    risk_score: int
    risk_level: str
    indicators: list[str]


def analyze_activity(indicators: list[str]) -> DetectionResult:
    """Calculate a simple risk score from simulated activity indicators."""
    weights = {
        "suspicious_process": 40,
        "unexpected_persistence": 30,
        "unusual_resource_usage": 20,
        "suspicious_network_activity": 25,
    }

    score = min(100, sum(weights.get(item, 0) for item in indicators))

    if score >= 70:
        level = "HIGH"
    elif score >= 35:
        level = "MEDIUM"
    else:
        level = "LOW"

    return DetectionResult(
        risk_score=score,
        risk_level=level,
        indicators=indicators.copy(),
    )


if __name__ == "__main__":
    sample_indicators = [
        "suspicious_process",
        "unexpected_persistence",
    ]

    result = analyze_activity(sample_indicators)

    print("KEYLOGGER DETECTION SYSTEM")
    print("-" * 30)
    print(f"Risk score: {result.risk_score}/100")
    print(f"Risk level: {result.risk_level}")
    print("Indicators:")
    for indicator in result.indicators:
        print(f"- {indicator}")
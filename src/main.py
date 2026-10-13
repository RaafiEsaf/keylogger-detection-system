"""Run the detection workflow using simulated activity."""

from src.detector import analyze_activity
from src.behavioral_analysis import analyze_behavior
from src.statistical_analysis import analyze_statistics
from src.report_generator import generate_report


def main():
    events = [
        "normal_activity",
        "suspicious_process",
        "unexpected_persistence",
        "suspicious_process",
        "unusual_resource_usage",
    ]

    behavior = analyze_behavior(events)
    statistics = analyze_statistics(events)

    known_indicators = {
        "suspicious_process",
        "unexpected_persistence",
        "unusual_resource_usage",
        "suspicious_network_activity",
    }

    indicators = list(dict.fromkeys(
        event for event in events if event in known_indicators
    ))

    result = analyze_activity(indicators)

    print("=" * 40)
    print("KEYLOGGER DETECTION SYSTEM")
    print("=" * 40)
    print(f"Events analyzed: {behavior['total_events']}")
    print(f"Unique event types: {behavior['unique_events']}")
    print(f"Average event frequency: {statistics['average_frequency']}")
    print(f"Risk score: {result.risk_score}/100")
    print(f"Risk level: {result.risk_level}")

    print("\nDetected indicators:")
    for indicator in result.indicators:
        print(f"- {indicator}")

    report_data = {
        "events_analyzed": behavior["total_events"],
        "unique_event_types": behavior["unique_events"],
        "average_event_frequency": statistics["average_frequency"],
        "risk_score": result.risk_score,
        "risk_level": result.risk_level,
        "indicators": result.indicators,
    }

    report_path = generate_report(report_data)

    print(f"\nReport saved to: {report_path}")
    print("Note: Results use simulated activity data.")


if __name__ == "__main__":
    main()
"""Behavioral analysis for suspicious activity indicators."""

from collections import Counter


def analyze_behavior(events: list[str]) -> dict:
    """Analyze simulated events and identify repeated suspicious activity."""

    counts = Counter(events)

    suspicious_events = {
        "unexpected_persistence",
        "suspicious_network_activity",
        "unusual_resource_usage",
    }

    findings = []

    for event, count in counts.items():
        if event in suspicious_events:
            findings.append({
                "event": event,
                "count": count,
                "suspicious": True,
            })

    return {
        "total_events": len(events),
        "unique_events": len(counts),
        "findings": findings,
    }


if __name__ == "__main__":
    sample_events = [
        "normal_activity",
        "unexpected_persistence",
        "normal_activity",
        "unexpected_persistence",
        "unusual_resource_usage",
    ]

    result = analyze_behavior(sample_events)

    print("BEHAVIORAL ANALYSIS")
    print("-" * 30)
    print(f"Total events: {result['total_events']}")
    print(f"Unique events: {result['unique_events']}")
    print("Findings:")

    for finding in result["findings"]:
        print(
            f"- {finding['event']}: "
            f"{finding['count']} occurrence(s)"
        )

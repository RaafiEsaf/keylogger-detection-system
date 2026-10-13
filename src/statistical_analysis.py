"""Statistical analysis of simulated activity events."""

from collections import Counter
from statistics import mean


def analyze_statistics(events: list[str]) -> dict:
    """Summarize event frequency and estimate activity risk."""

    if not events:
        return {
            "total_events": 0,
            "average_frequency": 0,
            "repeated_events": {},
        }

    counts = Counter(events)

    return {
        "total_events": len(events),
        "average_frequency": round(mean(counts.values()), 2),
        "repeated_events": {
            event: count
            for event, count in counts.items()
            if count > 1
        },
    }


if __name__ == "__main__":
    sample_events = [
        "normal_activity",
        "suspicious_process",
        "normal_activity",
        "suspicious_process",
        "suspicious_process",
    ]

    result = analyze_statistics(sample_events)

    print("STATISTICAL ANALYSIS")
    print("-" * 30)
    print(f"Total events: {result['total_events']}")
    print(f"Average frequency: {result['average_frequency']}")
    print("Repeated events:")

    for event, count in result["repeated_events"].items():
        print(f"- {event}: {count} occurrences")

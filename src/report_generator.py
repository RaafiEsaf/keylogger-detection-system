"""Generate JSON reports for detection results."""

import json
from datetime import datetime
from pathlib import Path


def generate_report(results: dict, output_dir: str = "reports") -> str:
    """Save detection results as a timestamped JSON report."""

    report_dir = Path(output_dir)
    report_dir.mkdir(parents=True, exist_ok=True)

    report = {
        "project": "Keylogger Detection System",
        "generated_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "results": results,
        "data_source": "simulated_activity",
    }

    filename = (
        "detection-report-"
        + datetime.now().strftime("%Y%m%d-%H%M%S")
        + ".json"
    )
    report_path = report_dir / filename

    report_path.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )

    return str(report_path)


if __name__ == "__main__":
    sample_results = {
        "risk_score": 90,
        "risk_level": "HIGH",
        "indicators": [
            "suspicious_process",
            "unexpected_persistence",
            "unusual_resource_usage",
        ],
    }

    path = generate_report(sample_results)
    print("Detection report generated successfully.")
    print(f"Report location: {path}")
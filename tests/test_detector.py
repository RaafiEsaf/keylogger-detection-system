import unittest

from src.detector import analyze_activity


class TestDetector(unittest.TestCase):

    def test_high_risk_detection(self):
        result = analyze_activity([
            "suspicious_process",
            "unexpected_persistence",
        ])

        self.assertEqual(result.risk_score, 70)
        self.assertEqual(result.risk_level, "HIGH")

    def test_low_risk_detection(self):
        result = analyze_activity([])

        self.assertEqual(result.risk_score, 0)
        self.assertEqual(result.risk_level, "LOW")

    def test_score_does_not_exceed_100(self):
        result = analyze_activity([
            "suspicious_process",
            "unexpected_persistence",
            "unusual_resource_usage",
            "suspicious_network_activity",
        ])

        self.assertEqual(result.risk_score, 100)

    def test_unknown_indicator_is_ignored(self):
        result = analyze_activity(["unknown_event"])

        self.assertEqual(result.risk_score, 0)
        self.assertEqual(result.risk_level, "LOW")


if __name__ == "__main__":
    unittest.main()
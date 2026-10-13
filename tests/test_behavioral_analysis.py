import unittest

from src.behavioral_analysis import analyze_behavior


class TestBehavioralAnalysis(unittest.TestCase):

    def test_counts_events(self):
        events = ["normal_activity", "normal_activity", "suspicious_process"]
        result = analyze_behavior(events)

        self.assertEqual(result["total_events"], 3)
        self.assertEqual(result["unique_events"], 2)

    def test_detects_suspicious_events(self):
        events = ["unexpected_persistence", "normal_activity"]
        result = analyze_behavior(events)

        self.assertEqual(len(result["findings"]), 1)
        self.assertEqual(
            result["findings"][0]["event"],
            "unexpected_persistence",
        )

    def test_empty_events(self):
        result = analyze_behavior([])

        self.assertEqual(result["total_events"], 0)
        self.assertEqual(result["unique_events"], 0)
        self.assertEqual(result["findings"], [])


if __name__ == "__main__":
    unittest.main()
import unittest

from src.statistical_analysis import analyze_statistics


class TestStatisticalAnalysis(unittest.TestCase):

    def test_counts_total_events(self):
        events = ["normal_activity", "suspicious_process", "normal_activity"]
        result = analyze_statistics(events)

        self.assertEqual(result["total_events"], 3)

    def test_calculates_average_frequency(self):
        events = ["normal_activity", "normal_activity", "suspicious_process"]
        result = analyze_statistics(events)

        self.assertEqual(result["average_frequency"], 1.5)

    def test_identifies_repeated_events(self):
        events = ["normal_activity", "normal_activity", "suspicious_process"]
        result = analyze_statistics(events)

        self.assertEqual(
            result["repeated_events"]["normal_activity"],
            2,
        )
        self.assertNotIn(
            "suspicious_process",
            result["repeated_events"],
        )

    def test_empty_events(self):
        result = analyze_statistics([])

        self.assertEqual(result["total_events"], 0)
        self.assertEqual(result["average_frequency"], 0)
        self.assertEqual(result["repeated_events"], {})


if __name__ == "__main__":
    unittest.main()
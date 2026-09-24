"""Arithmetic and policy implementation checks, not validation of UCF."""
import unittest
from booking_model import Case, assess, choose, feasible, report

class BookingTests(unittest.TestCase):
    def test_local_target(self):
        self.assertEqual(choose(Case(), 'max_completions'), (8, 0))

    def test_explicit_constraint(self):
        self.assertEqual(choose(Case(), 'min_one_each'), (5, 1))

    def test_arrival_order(self):
        self.assertEqual(choose(Case(), 'arrival_order'), (2, 2))

    def test_conservation(self):
        for item in report()['sensitivity']:
            c = Case(**item['case'])
            demand = c.short_count * c.short_minutes + c.long_count * c.long_minutes
            for r in item['results']:
                if r['feasible']:
                    self.assertLessEqual(r['used_minutes'], c.capacity)
                    self.assertEqual(r['used_minutes'] + r['unmet_service_minutes'], demand)
                    self.assertEqual(r['completed'] + r['unmet_requests'], c.short_count + c.long_count)

    def test_objective_is_maximal(self):
        for item in report()['sensitivity']:
            c = Case(**item['case'])
            self.assertEqual(sum(choose(c, 'max_completions')), max(map(sum, feasible(c))))

    def test_infeasible_constraint(self):
        self.assertFalse(assess(Case(capacity=30), 'min_one_each')['feasible'])

    def test_no_exclusion_when_all_demand_fits(self):
        c = Case(capacity=210)
        for p in ('arrival_order', 'max_completions', 'min_one_each'):
            self.assertEqual(choose(c, p), (8, 2))

    def test_input_and_policy_validation(self):
        for args in ({'capacity': -1}, {'short_minutes': 0}, {'long_count': True}):
            with self.assertRaises(ValueError):
                Case(**args)
        with self.assertRaises(ValueError):
            choose(Case(), 'unknown')

if __name__ == '__main__':
    unittest.main()

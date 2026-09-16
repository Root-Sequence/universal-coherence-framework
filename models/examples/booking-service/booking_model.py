"""Synthetic, deterministic capacity example. No people or live services.

Run: python booking_model.py --output /tmp/booking-results.json
Uses only Python's standard library; refuses to overwrite an existing output.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict, dataclass
from itertools import product
import json
from pathlib import Path

@dataclass(frozen=True)
class Case:
    capacity: int = 120
    short_count: int = 8
    long_count: int = 2
    short_minutes: int = 15
    long_minutes: int = 45

    def __post_init__(self) -> None:
        for key, value in asdict(self).items():
            if type(value) is not int or value < 0:
                raise ValueError(f'{key} must be a non-negative integer')
        if min(self.short_minutes, self.long_minutes) == 0:
            raise ValueError('Appointment durations must be positive')


def feasible(case: Case) -> list[tuple[int, int]]:
    return [(s, l) for s, l in product(range(case.short_count + 1),
                                      range(case.long_count + 1))
            if s * case.short_minutes + l * case.long_minutes <= case.capacity]


def choose(case: Case, policy: str) -> tuple[int, int] | None:
    if policy == 'arrival_order':
        # Fixed queue: all long requests, then all short requests. No skipping.
        s = l = used = 0
        queue = [('long', case.long_minutes)] * case.long_count
        queue += [('short', case.short_minutes)] * case.short_count
        for kind, duration in queue:
            if used + duration > case.capacity:
                break
            used += duration
            s += kind == 'short'
            l += kind == 'long'
        return s, l
    if policy not in ('max_completions', 'min_one_each'):
        raise ValueError(f'Unknown policy: {policy}')
    candidates = feasible(case)
    if policy == 'min_one_each':
        candidates = [(s, l) for s, l in candidates if s >= 1 and l >= 1]
    if not candidates:
        return None
    # Deterministic tie break: more long requests, then more short requests.
    return max(candidates, key=lambda pair: (sum(pair), pair[1], pair[0]))


def assess(case: Case, policy: str) -> dict:
    selected = choose(case, policy)
    if selected is None:
        return {'policy': policy, 'feasible': False}
    s, l = selected
    used = s * case.short_minutes + l * case.long_minutes
    return {'policy': policy, 'feasible': True,
            'short_served': s, 'long_served': l, 'completed': s + l,
            'used_minutes': used, 'idle_minutes': case.capacity - used,
            'unmet_requests': case.short_count + case.long_count - s - l,
            'unmet_service_minutes': ((case.short_count - s) * case.short_minutes
                                      + (case.long_count - l) * case.long_minutes)}


def report() -> dict:
    policies = ('arrival_order', 'max_completions', 'min_one_each')
    base = Case()
    return {'kind': 'synthetic enumeration, not empirical validation',
            'base_case': asdict(base),
            'base_results': [assess(base, p) for p in policies],
            'sensitivity': [dict(case=asdict(c), results=[assess(c, p) for p in policies])
                            for c in (Case(capacity=b, long_minutes=d)
                                      for b, d in product((30, 60, 90, 120, 180, 240),
                                                          (15, 30, 45, 60)))]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        with args.output.open('x', encoding='utf-8') as handle:
            json.dump(report(), handle, indent=2, sort_keys=True)
            handle.write('\n')
    except OSError as exc:
        parser.exit(2, f'Cannot create output: {exc}\n')

if __name__ == '__main__':
    main()

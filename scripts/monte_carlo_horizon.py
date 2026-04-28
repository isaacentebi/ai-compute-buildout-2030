#!/usr/bin/env python3
"""Package-root wrapper for monte_carlo_horizon.py."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
runpy.run_path(str(ROOT / "monte_carlo_horizon.py"), run_name="__main__")

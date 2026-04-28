#!/usr/bin/env python3
"""Compatibility wrapper for the Rev-4.1 stale-number/file-reference gate."""

from __future__ import annotations

import sys

import regression_checks


if __name__ == "__main__":
    sys.exit(regression_checks.main())

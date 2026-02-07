"""
Shared fixtures for ActualPrice Gemini 3 agent test suite.

All tests in this suite are designed to run WITHOUT a Gemini API key.
They test pure helper methods: JSON parsing, confidence scoring,
anomaly detection, thought classification, and data preparation.
"""

import pytest
from datetime import datetime, timedelta

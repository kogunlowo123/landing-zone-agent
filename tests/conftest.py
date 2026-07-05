"""Test configuration for Landing Zone Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "landing-zone-agent", "category": "Cloud Engineering"}

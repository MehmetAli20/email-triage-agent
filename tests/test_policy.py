"""Policy tests.

`import anthropic` must never appear here. If it does, the boundary has slipped.
"""
import pytest


@pytest.mark.skip(reason="policy not implemented yet")
def test_financial_always_blocks():
    ...


@pytest.mark.skip(reason="policy not implemented yet")
def test_external_recipient_always_blocks():
    ...

from unittest.mock import MagicMock

import click
from click.testing import CliRunner
import requests

import prefect
from prefect.cli.execute import execute


def test_execute_init():
    runner = CliRunner()
    result = runner.invoke(execute)
    assert result.exit_code == 0
    assert "Execute flow environments." in result.output


def test_execute_help():
    runner = CliRunner()
    result = runner.invoke(execute, ["--help"])
    assert result.exit_code == 0
    assert "Execute flow environments." in result.output


def test_execute_cloud_flow_fails():
    runner = CliRunner()
    result = runner.invoke(execute, "cloud-flow")
    assert result.exit_code == 1
    assert "Not currently executing a flow within a cloud context." in result.output
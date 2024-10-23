'''
This module contains tests for the App class's REPL functionality.
The tests check:
- The behavior of the REPL when it receives the 'exit' command.
- The handling of unknown commands before exiting the REPL.
'''
import pytest
from app import App
from app.plugins.menu import MenuCommand
from app.plugins.exit import ExitCommand

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_menu_command(capfd):
    """Tests the menu command"""
    menu_command = MenuCommand()
    menu_command.execute()
    captured = capfd.readouterr()
    expected_output = ("Welcome to the Basic Calculator.\n"
                       "Select the operation to be performed\n"
                       "Add\nSubtract\nMultiply\nDivide\n")
    assert captured.out == expected_output


def test_exit_command_execute():
    """Test the exit command in plugins"""
    exit_command = ExitCommand()
    with pytest.raises(SystemExit) as e:
        exit_command.execute()
    assert str(e.value) == "Exiting..."

"""
Test custom django menegement commands
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management import call_command
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Tests for wait_for_db command."""
    
    def test_wait_for_db_ready(self, patched_check):
        """Test wait_for_db commanf if databae ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

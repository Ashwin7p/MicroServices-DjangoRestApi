# mock database behaviour
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OpError


#simulate calling of custom command
from django.core.management import call_command
#Db errors encountered
from django.db.utils import OperationalError
#Basic test class for testing, we dont need any migartion and simple database simulation of startup
from django.test import SimpleTestCase

#patch decorator is something we're trying to mock
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready.-> positive"""
        patched_check.return_value = True #This is the check default database in custom command, positive connection in 1 go

        call_command('wait_for_db')
        # line is an assertion used in unit testing to verify that the check method of the command class has been called exactly once with the specified arguments.
        patched_check.assert_called_once_with(databases=['default']) #if method is not defined then its not called zero times

    
    @patch('time.sleep') #only for this method unlike class, mock sleep
    def test_wait_for_db(self, patched_sleep, patched_check):
        """Test waiting for db .-> negative"""
        #side effect handles exception error raised
        patched_check.side_effect = [Psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]
        # 2 times Psycopg2, 3 times OperationalError the success
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
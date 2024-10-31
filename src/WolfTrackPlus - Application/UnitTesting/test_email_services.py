import unittest
from unittest.mock import patch, MagicMock
import os 
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Controller.email_framework import (s_email, send_registration_email, 
                         status_change_email, password_reset_email, 
                         successful_reset_email)


class TestEmailService(unittest.TestCase):

    @patch('smtplib.SMTP_SSL')
    def test_application_email_success(self, mock_smtp):
        """Test successful application email sending"""
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        
        result = s_email(
            company_name="Google",
            location="Mountain View",
            job_Profile="Software Engineer",
            salary="120000",
            email="test@example.com",
            status="Applied"
        )
        
        self.assertTrue(result)
        mock_server.login.assert_called_once()
        mock_server.sendmail.assert_called_once()

    @patch('smtplib.SMTP_SSL')
    def test_registration_email_success(self, mock_smtp):
        """Test successful registration email sending"""
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        
        result = send_registration_email(
            name="John Doe",
            email="test@example.com"
        )
        
        self.assertTrue(result)
        mock_server.login.assert_called_once()
        mock_server.sendmail.assert_called_once()

    @patch('smtplib.SMTP_SSL')
    def test_status_change_email_success(self, mock_smtp):
        """Test successful status change email sending"""
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        
        result = status_change_email(
            application_id="123",
            email="test@example.com",
            status="Interview Scheduled"
        )
        
        self.assertTrue(result)
        mock_server.login.assert_called_once()
        mock_server.sendmail.assert_called_once()

    @patch('smtplib.SMTP_SSL')
    def test_password_reset_email_success(self, mock_smtp):
        """Test successful password reset email sending"""
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        
        result = password_reset_email(
            email="test@example.com",
            code="123456"
        )
        
        self.assertTrue(result)
        mock_server.login.assert_called_once()
        mock_server.sendmail.assert_called_once()

    

if __name__ == '__main__':
    unittest.main()
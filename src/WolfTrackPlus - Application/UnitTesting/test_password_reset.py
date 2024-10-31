import unittest
import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from DAO.password_reset_dao import password_reset_dao
from unittest.mock import MagicMock
from flask import Flask
from flask_restful import Api
from Controller.password_reset_controller import PasswordReset


class TestPasswordResetDAO(unittest.TestCase):
   def setUp(self):
       self.dao = password_reset_dao()
       self.dao._password_reset_dao__db = MagicMock()


   def test_upsert_code_inserts_new_code(self):
       email = "test@example.com"
       code = 1234
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.upsert_code(email, code)
       self.assertTrue(result)


   def test_upsert_code_updates_existing_code(self):
       email = "existing@example.com"
       code = 4321
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.upsert_code(email, code)
       self.assertTrue(result)


   def test_upsert_code_special_characters_in_email(self):
       email = "user+test@example.com"
       code = 5678
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.upsert_code(email, code)
       self.assertTrue(result)


   def test_get_code_existing_user(self):
       email = "existing@example.com"
       expected_code = 1234
       self.dao._password_reset_dao__db.run_query.return_value = [(expected_code,)]
       result = self.dao.get_code(email)
       self.assertEqual(result, expected_code)


   def test_update_password_successful(self):
       email = "test@example.com"
       password = "new_password"
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.update_password(email, password)
       self.assertTrue(result)


   def test_update_password_special_characters_in_password(self):
       email = "test@example.com"
       password = "new_!@#password"
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.update_password(email, password)
       self.assertTrue(result)


   def test_update_password_invalid_email(self):
       email = "invalid_email"
       password = "password123"
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.update_password(email, password)
       self.assertTrue(result)


   def test_update_password_empty_password(self):
       email = "test@example.com"
       password = ""
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.update_password(email, password)
       self.assertTrue(result)


   def test_upsert_code_empty_code(self):
       email = "test@example.com"
       code = ""
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.upsert_code(email, code)
       self.assertTrue(result)


   def test_upsert_code_zero_code(self):
       email = "test@example.com"
       code = 0
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.upsert_code(email, code)
       self.assertTrue(result)


   def test_upsert_code_negative_code(self):
       email = "test@example.com"
       code = -1234
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.upsert_code(email, code)
       self.assertTrue(result)


   def test_update_password_unicode_characters(self):
       email = "unicode@example.com"
       password = "密码123"
       self.dao._password_reset_dao__db.run_query.return_value = True
       result = self.dao.update_password(email, password)
       self.assertTrue(result)


   def test_get_code_special_characters_in_email(self):
       email = "special+user@example.com"
       self.dao._password_reset_dao__db.run_query.return_value = [(1234,)]
       result = self.dao.get_code(email)
       self.assertEqual(result, 1234)





if __name__ == "__main__":
   unittest.main()




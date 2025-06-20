# models/user_data.py

from pydantic import BaseModel, EmailStr, RootModel, ValidationError
from typing import List


class UserData(BaseModel):
    """Represents a single user's form data."""
    name: str
    email: EmailStr
    address: str
    perm_address: str


class UsersList(RootModel[List[UserData]]):
    """Wrapper for list of UserData models."""

    def __iter__(self):
        return iter(self.root)

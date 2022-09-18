from typing import Union
from pydantic import BaseModel

from datetime import datetime




class ToDoItem(BaseModel):
    message: str
    done: bool
    created_at: datetime
    date: Union[datetime, None] = None
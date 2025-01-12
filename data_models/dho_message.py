from datetime import datetime

from pydantic import BaseModel
from pydantic import validator

from data_models.categories import DhOCategory


class DhOMessage(BaseModel):
    msg_id: int
    thread_id: int
    date: datetime
    is_first_in_thread: bool
    category: DhOCategory
    author: str
    title: str
    msg: str

    @validator("date", pre=True)
    def dho_date_to_datetime(cls, dt) -> datetime:

        if type(dt) is datetime:
            return dt

        try:
            return datetime.fromisoformat(dt)
        except ValueError:
            pass

        return datetime.strptime(dt, "%a, %d %b %Y %H:%M:%S %Z")

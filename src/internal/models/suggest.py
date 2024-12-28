from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List

from .user import User as BaseUser


class Check(BaseModel):
    telegram_id: Optional[int] = None
    telegram_username: Optional[str] = None
    comment: Optional[str] = None
    checked_at: Optional[datetime] = None

    # def __init__(self, user: BaseUser, comment: str):
    #     self.telegram_id = user.telegram_id
    #     self.telegram_username = user.telegram_username
    #     self.comment = comment
    #     self.checked_at = datetime.now()


class ProposingUser(BaseModel):
    uuid: Optional[str] = None
    telegram_id: Optional[int] = None
    telegram_username: Optional[str] = None
    role: Optional[str] = None


class Suggest(BaseModel):
    uuid: Optional[str] = None
    question: Optional[str] = None
    answers: Optional[List[str]] = None
    correct_id: Optional[int] = None  # id of correct answer
    proposing: Optional[ProposingUser] = None  # uuid of user, who suggested question
    difficulty: Optional[int] = None
    check_need_count: Optional[int] = None
    marked_as_correct: Optional[List[Check]] = None  # correct checks
    marked_as_erroneous: Optional[List[Check]] = None  # error checks
    marked_as_improve: Optional[List[Check]] = None  # improve checks
    created_at: Optional[datetime] = None

    def set_proposing_user(self, user: BaseUser):
        self.proposing = ProposingUser(
            uuid=str(user.uuid),
            telegram_id=user.telegram_id,
            telegram_username=user.telegram_username,
            role=user.role,
        )


class SuggestRequest(BaseModel):
    question: Optional[str] = None
    answers: Optional[List[str]] = None
    correctAnswer: Optional[str] = None

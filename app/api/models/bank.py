from pydantic import BaseModel


class BankAccountCreate(BaseModel):
    account_number: str
    balance: float


class BankAccountUpdate(BaseModel):
    balance: float


class BankAccountResponse(BankAccountCreate):
    id: int


class ErrorResponse(BaseModel):
    detail: str

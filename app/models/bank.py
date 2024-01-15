from sqlalchemy import Column, Float, Integer, String

from app.db import Base


class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, index=True)
    balance = Column(Float, default=0.0)

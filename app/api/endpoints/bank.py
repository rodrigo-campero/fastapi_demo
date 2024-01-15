from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.models.bank import (
    BankAccountCreate,
    BankAccountResponse,
    BankAccountUpdate,
)
from app.core.security import pwd_context
from app.db import SessionLocal, engine
from app.models.bank import BankAccount

router = APIRouter()


def get_db():
    """
    Get a database session.

    Returns:
        SessionLocal: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/accounts/", response_model=BankAccountResponse)
def create_account(account: BankAccountCreate, db: Session = Depends(get_db)):
    """
    Create a new bank account.

    Args:
        account (BankAccountCreate): The account details.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        BankAccount: The created bank account.
    """
    db_account = BankAccount(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


@router.get("/accounts/{account_id}", response_model=BankAccountResponse)
def read_account(account_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a bank account by its ID.

    Args:
        account_id (int): The ID of the bank account to retrieve.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        BankAccount: The bank account object.

    Raises:
        HTTPException: If the account is not found.
    """
    db_account = db.query(BankAccount).filter(BankAccount.id == account_id).first()
    if db_account:
        return db_account
    raise HTTPException(status_code=404, detail="Account not found")


@router.put("/accounts/{account_id}", response_model=BankAccountResponse)
def update_account(
    account_id: int, account: BankAccountUpdate, db: Session = Depends(get_db)
):
    """
    Update a bank account with the given account_id using the provided account data.

    Args:
        account_id (int): The ID of the account to be updated.
        account (BankAccountUpdate): The updated account data.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        BankAccount: The updated bank account.

    Raises:
        HTTPException: If the account with the given account_id is not found.
    """
    db_account = db.query(BankAccount).filter(BankAccount.id == account_id).first()
    if db_account:
        for key, value in account.dict(exclude_unset=True).items():
            setattr(db_account, key, value)
        db.commit()
        db.refresh(db_account)
        return db_account
    raise HTTPException(status_code=404, detail="Account not found")


@router.delete("/accounts/{account_id}", response_model=dict)
def delete_account(account_id: int, db: Session = Depends(get_db)):
    """
    Delete a bank account from the database.

    Args:
        account_id (int): The ID of the account to be deleted.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary with a message indicating the success of the deletion.

    Raises:
        HTTPException: If the account with the given ID is not found.
    """
    db_account = db.query(BankAccount).filter(BankAccount.id == account_id).first()
    if db_account:
        db.delete(db_account)
        db.commit()
        return {"message": "Account deleted successfully"}
    raise HTTPException(status_code=404, detail="Account not found")

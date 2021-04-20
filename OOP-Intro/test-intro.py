from intro import *

def test_get_balance():
    rado = BankAccount("Rado", 0, "BGN")
    assert rado.get_balance() == 0

def test_deposit():
    rado = BankAccount("Rado", 0, "BGN")
    rado.deposit(100)
    assert rado.get_balance() == 100

def test_withdraw():
    rado = BankAccount("Rado", 100, "BGN")
    rado.withdraw(5)
    assert rado.get_balance() == 95

def test_str():
    rado = BankAccount("Rado", 15, "BGN")
    assert str(rado) == "Bank account for Rado with balance of 15BGN"

def test_int():
    rado = BankAccount("Rado", 20, "BGN")
    assert int(rado) == 20

def test_transfer_to():
    rado = BankAccount("Rado", 1000, "BGN")
    ivo = BankAccount("Ivo", 0, "BGN")
    assert rado.transfer_to(ivo, 500) == True
    assert rado.transfer_to(ivo, 501) == False

def test_history():
    rado = BankAccount("Rado", 1000, "BGN")
    assert rado.get_history() == ['Account was created']
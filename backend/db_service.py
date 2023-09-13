from sqlmodel import select, update, desc
from database.models.currency import Currency
from database.models.exchange_rate import ExchangeRate
from database.config import setup_db

class DBService:
    def __init__(self):
        self.session = setup_db()

    def get_currencies(self):
        return self.session.exec(select(Currency).order_by(desc(Currency.enabled))).all()

    def get_enabled_currencies(self):
        return self.session.exec(select(Currency).where(Currency.enabled == True)).all()
        
    def update_currency(self, currency_id: int, enabled: bool):
        self.session.exec(update(Currency).where(Currency.id == currency_id).values(enabled=enabled))

    def get_exchange_rates(self):
        return self.session.exec(select(ExchangeRate).order_by(desc(ExchangeRate.date))).all()

    def save_exchange_rate(self, exchange_rate: ExchangeRate):
        self.session.add(exchange_rate)
        self.session.commit()
        self.session.refresh(exchange_rate)
        return exchange_rate
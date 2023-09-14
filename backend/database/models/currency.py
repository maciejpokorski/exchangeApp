from sqlmodel import SQLModel, Field, select
from sqlalchemy import  event

class Currency(SQLModel, table=True):
    """
    Represents a currency.

    Attributes:
        id (int): The unique identifier for the currency.
        code (str): The currency code, which is uniqe.
        enabled (bool): Indicates whether the currency is enabled (default is False).
    """
    id: int = Field(primary_key=True, index=True)
    code: str = Field(unique=True, index=True)
    enabled: bool = False

INITIAL_DATA = [
   { 
    'code': "EUR",
    'enabled': True, 
   },
   { 
    'code': "USD",
    'enabled': True,
   },
   { 
    'code': "JPY",
    'enabled': True, 
   },
   { 
    'code': "GBP", 
    'enabled': True, 
   },
   { 
     'code': "AED",
     'enabled': False
   },
   { 
     'code': "AFN",
     'enabled': False,
   },
   { 
     'code': "ALL",
     'enabled': False,
   },
   { 
     'code': "AMD",
     'enabled': False,
   },
   { 
     'code': "ANG",
     'enabled': False,
   },
   { 
     'code': "AOA",
     'enabled': False,
   },
   { 
     'code': "ARS",
     'enabled': False,
   },
   { 
     'code': "AUD",
     'enabled': False,
   },
   { 
     'code': "AWG",
     'enabled': False,
   },
   { 
     'code': "AZN",
     'enabled': False,
   },
   { 
     'code': "BAM",
     'enabled': False,
   },
   { 
     'code': "BBD",
     'enabled': False,
   },
   { 
     'code': "BDT",
     'enabled': False,
   },
   { 
     'code': "BGN",
     'enabled': False,
   },
   { 
     'code': "BHD",
     'enabled': False,
   },
   { 
     'code': "BIF",
     'enabled': False,
   },
   { 
     'code': "BMD",
     'enabled': False,
   },
   { 
     'code': "BND",
     'enabled': False,
   },
   { 
     'code': "BOB",
     'enabled': False,
   },
   { 
     'code': "BRL",
     'enabled': False,
   },
   { 
     'code': "BSD",
     'enabled': False,
   },
   { 
     'code': "BTC",
     'enabled': False,
   },
   { 
     'code': "BTN",
     'enabled': False,
   },
   { 
     'code': "BWP",
     'enabled': False,
   },
   { 
     'code': "BYN",
     'enabled': False,
   },
   { 
     'code': "BZD",
     'enabled': False,
   },
   { 
     'code': "CAD",
     'enabled': False,
   },
   { 
     'code': "CDF",
     'enabled': False,
   },
   { 
     'code': "CHF",
     'enabled': False,
   },
   { 
     'code': "CLF",
     'enabled': False,
   },
   { 
     'code': "CLP",
     'enabled': False,
   },
   { 
     'code': "CNH",
     'enabled': False,
   },
   { 
     'code': "CNY",
     'enabled': False,
   },
   { 
     'code': "COP",
     'enabled': False,
   },
   { 
     'code': "CRC",
     'enabled': False,
   },
   { 
     'code': "CUC",
     'enabled': False,
   },
   { 
     'code': "CUP",
     'enabled': False,
   },
   { 
     'code': "CVE",
     'enabled': False,
   },
   { 
     'code': "CZK",
     'enabled': False,
   },
   { 
     'code': "DJF",
     'enabled': False,
   },
   { 
     'code': "DKK",
     'enabled': False,
   },
   { 
     'code': "DOP",
     'enabled': False,
   },
   { 
     'code': "DZD",
     'enabled': False,
   },
   { 
     'code': "EGP",
     'enabled': False,
   },
   { 
     'code': "ERN",
     'enabled': False,
   },
   { 
     'code': "ETB",
     'enabled': False,
   },
   { 
     'code': "FJD",
     'enabled': False,
   },
   { 
     'code': "FKP",
     'enabled': False,
   },
   { 
     'code': "GEL",
     'enabled': False,
   },
   { 
     'code': "GGP",
     'enabled': False,
   },
   { 
     'code': "GHS",
     'enabled': False,
   },
   { 
     'code': "GIP",
     'enabled': False,
   },
   { 
     'code': "GMD",
     'enabled': False,
   },
   { 
     'code': "GNF",
     'enabled': False,
   },
   { 
     'code': "GTQ",
     'enabled': False,
   },
   { 
     'code': "GYD",
     'enabled': False,
   },
   { 
     'code': "HKD",
     'enabled': False,
   },
   { 
     'code': "HNL",
     'enabled': False,
   },
   { 
     'code': "HRK",
     'enabled': False,
   },
   { 
     'code': "HTG",
     'enabled': False,
   },
   { 
     'code': "HUF",
     'enabled': False,
   },
   { 
     'code': "IDR",
     'enabled': False,
   },
   { 
     'code': "ILS",
     'enabled': False,
   },
   { 
     'code': "IMP",
     'enabled': False,
   },
   { 
     'code': "INR",
     'enabled': False,
   },
   { 
     'code': "IQD",
     'enabled': False,
   },
   { 
     'code': "IRR",
     'enabled': False,
   },
   { 
     'code': "ISK",
     'enabled': False,
   },
   { 
     'code': "JEP",
     'enabled': False,
   },
   { 
     'code': "JMD",
     'enabled': False,
   },
   { 
     'code': "JOD",
     'enabled': False,
   },
   { 
     'code': "KES",
     'enabled': False,
   },
   { 
     'code': "KGS",
     'enabled': False,
   },
   { 
     'code': "KHR",
     'enabled': False,
   },
   { 
     'code': "KMF",
     'enabled': False,
   },
   { 
     'code': "KPW",
     'enabled': False,
   },
   { 
     'code': "KRW",
     'enabled': False,
   },
   { 
     'code': "KWD",
     'enabled': False,
   },
   { 
     'code': "KYD",
     'enabled': False,
   },
   { 
     'code': "KZT",
     'enabled': False,
   },
   { 
     'code': "LAK",
     'enabled': False,
   },
   { 
     'code': "LBP",
     'enabled': False,
   },
   { 
     'code': "LKR",
     'enabled': False,
   },
   { 
     'code': "LRD",
     'enabled': False,
   },
   { 
     'code': "LSL",
     'enabled': False,
   },
   { 
     'code': "LYD",
     'enabled': False,
   },
   { 
     'code': "MAD",
     'enabled': False,
   },
   { 
     'code': "MDL",
     'enabled': False,
   },
   { 
     'code': "MGA",
     'enabled': False,
   },
   { 
     'code': "MKD",
     'enabled': False,
   },
   { 
     'code': "MMK",
     'enabled': False,
   },
   { 
     'code': "MNT",
     'enabled': False,
   },
   { 
     'code': "MOP",
     'enabled': False,
   },
   { 
     'code': "MRU",
     'enabled': False,
   },
   { 
     'code': "MUR",
     'enabled': False,
   },
   { 
     'code': "MVR",
     'enabled': False,
   },
   { 
     'code': "MWK",
     'enabled': False,
   },
   { 
     'code': "MXN",
     'enabled': False,
   },
   { 
     'code': "MYR",
     'enabled': False,
   },
   { 
     'code': "MZN",
     'enabled': False,
   },
   { 
     'code': "NAD",
     'enabled': False,
   },
   { 
     'code': "NGN",
     'enabled': False,
   },
   { 
     'code': "NIO",
     'enabled': False,
   },
   { 
     'code': "NOK",
     'enabled': False,
   },
   { 
     'code': "NPR",
     'enabled': False,
   },
   { 
     'code': "NZD",
     'enabled': False,
   },
   { 
     'code': "OMR",
     'enabled': False,
   },
   { 
     'code': "PAB",
     'enabled': False,
   },
   { 
     'code': "PEN",
     'enabled': False,
   },
   { 
     'code': "PGK",
     'enabled': False,
   },
   { 
     'code': "PHP",
     'enabled': False,
   },
   { 
     'code': "PKR",
     'enabled': False,
   },
   { 
     'code': "PLN",
     'enabled': False,
   },
   { 
     'code': "PYG",
     'enabled': False,
   },
   { 
     'code': "QAR",
     'enabled': False,
   },
   { 
     'code': "RON",
     'enabled': False,
   },
   { 
     'code': "RSD",
     'enabled': False,
   },
   { 
     'code': "RUB",
     'enabled': False,
   },
   { 
     'code': "RWF",
     'enabled': False,
   },
   { 
     'code': "SAR",
     'enabled': False,
   },
   { 
     'code': "SBD",
     'enabled': False,
   },
   { 
     'code': "SCR",
     'enabled': False,
   },
   { 
     'code': "SDG",
     'enabled': False,
   },
   { 
     'code': "SEK",
     'enabled': False,
   },
   { 
     'code': "SGD",
     'enabled': False,
   },
   { 
     'code': "SHP",
     'enabled': False,
   },
   { 
     'code': "SLL",
     'enabled': False,
   },
   { 
     'code': "SOS",
     'enabled': False,
   },
   { 
     'code': "SRD",
     'enabled': False,
   },
   { 
     'code': "SSP",
     'enabled': False,
   },
   { 
     'code': "STD",
     'enabled': False,
   },
   { 
     'code': "STN",
     'enabled': False,
   },
   { 
     'code': "SVC",
     'enabled': False,
   },
   { 
     'code': "SYP",
     'enabled': False,
   },
   { 
     'code': "SZL",
     'enabled': False,
   },
   { 
     'code': "THB",
     'enabled': False,
   },
   { 
     'code': "TJS",
     'enabled': False,
   },
   { 
     'code': "TMT",
     'enabled': False,
   },
   { 
     'code': "TND",
     'enabled': False,
   },
   { 
     'code': "TOP",
     'enabled': False,
   },
   { 
     'code': "TRY",
     'enabled': False,
   },
   { 
     'code': "TTD",
     'enabled': False,
   },
   { 
     'code': "TWD",
     'enabled': False,
   },
   { 
     'code': "TZS",
     'enabled': False,
   },
   { 
     'code': "UAH",
     'enabled': False,
   },
   { 
     'code': "UGX",
     'enabled': False,
   },
   { 
     'code': "UYU",
     'enabled': False,
   },
   { 
     'code': "UZS",
     'enabled': False,
   },
   { 
     'code': "VES",
     'enabled': False,
   },
   { 
     'code': "VND",
     'enabled': False,
   },
   { 
     'code': "VUV",
     'enabled': False,
   },
   { 
     'code': "WST",
     'enabled': False,
   },
   { 
     'code': "XAF",
     'enabled': False,
   },
   { 
     'code': "XAG",
     'enabled': False,
   },
   { 
     'code': "XAU",
     'enabled': False,
   },
   { 
     'code': "XCD",
     'enabled': False,
   },
   { 
     'code': "XDR",
     'enabled': False,
   },
   { 
     'code': "XOF",
     'enabled': False,
   },
   { 
     'code': "XPD",
     'enabled': False,
   },
   { 
     'code': "XPF",
     'enabled': False,
   },
   { 
     'code': "XPT",
     'enabled': False,
   },
   { 
     'code': "YER",
     'enabled': False,
   },
   { 
     'code': "ZAR",
     'enabled': False,
   },
   { 
     'code': "ZMW",
     'enabled': False,
   },
   { 
     'code': "ZWL",
     'enabled': False,
   },
]

def seed_currency(target, connection, **kw):
    connection.execute(target.insert(), INITIAL_DATA)

event.listen(Currency.__table__, 'after_create', seed_currency)
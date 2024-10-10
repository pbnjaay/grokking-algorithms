USD = 'USD'
EUR = 'EUR'
XOF = 'XOF'

EXCHANGE_RATES = {
    EUR: {USD: 1.10, XOF: 654.83},
    USD: {XOF: 597.27, EUR: 0.9},
    XOF: {EUR: 0.0015, USD: 0.0017}
}

CURRENCIES = list(EXCHANGE_RATES.keys())


def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount >= 0:
                return amount
            raise ValueError()
        except ValueError:
            print('Invalid amount')


def _get_currency(name):
    currency = input(f'Enter the {name} currency (USD/EUR/XOF): ').upper()
    while currency not in CURRENCIES:
        print('Invalid currency')
        currency = input('Enter the source currency (USD/EUR/XOF): ').upper()
    return currency


def get_currency():
    return _get_currency('source'), _get_currency('target')


def convert(amount, source_currency, target_currency):
    if source_currency == target_currency:
        return amount
    return round(amount * EXCHANGE_RATES[source_currency][target_currency], 2)


def run():
    amount = get_amount()
    source_currency, target_currency = get_currency()
    converted_amount = convert(amount, source_currency, target_currency)
    print(f'{amount} {source_currency} is equal to {converted_amount} {target_currency}')


if __name__ == '__main__':
    run()

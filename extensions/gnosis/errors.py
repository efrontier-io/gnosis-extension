# Custom exceptions

class NotEnoughOffersOrderbookException(Exception):
    def __init__(self, amount):
        msg = "Amount of %d is missing in orderbook" % amount
        super(NotEnoughOffersOrderbookException, self).__init__(msg)
        self.missing_amount = amount


class TokenNotFoundException(Exception):
    def __init__(self, message):
        self.message = message


class UnknownTokenException(Exception):
    def __init__(self, message):
        super(UnknownTokenException, self).__init__(f"One or more of the tokens are unknown {message}")

class OrderWontBeTaken(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class GasTooHigh(Exception):
    pass


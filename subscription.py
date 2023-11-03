class Subscription:
    def __init__(self, subscription_id, name, price, trial_period):
        self.__subscription_id = subscription_id
        self._name = name
        self.price = price
        self.trial_period = trial_period

    def get_info(self):
        return (f"Subscription ID: {self.__subscription_id}\n"
                f"Name: {self._name}\n"
                f"Price: £{self.price}\n"
                f"Trial Period: {self.trial_period} days.")


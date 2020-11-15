class Location:
    def __init__(self, cost_of_sale, cost_of_rent):
        self.cost_of_sale = cost_of_sale
        self.cost_of_rent = cost_of_rent
        self.owner = None

    def update_owner(self, owner):
        self.owner = owner

    def remove_owner(self):
        self.ownser = None

    def __repr__(self):
        return f'{self.owner} - {self.cost_of_sale} - {self.cost_of_rent}'

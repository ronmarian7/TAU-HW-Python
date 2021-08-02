""" Exercise #7. Python for Engineers."""


#########################################
# Question 1 - do not delete this comment
#########################################


class Beverage:

    def __init__(self, name, price, is_diet):
        self.name = name
        self.price = price
        self.is_diet = is_diet
        if price < 0:
            raise ValueError('Price must be greater the 0')

    def get_final_price(self, size='Large'):
        if size == 'XL':
            return self.price * 1.25
        elif size == 'Normal':
            return self.price * 0.75
        elif size == 'Large':
            return self.price
        else:
            raise ValueError("We don't have your beverage size")
#########################################
# Question 2 - do not delete this comment
#########################################


class Pizza:

    def __init__(self, name, price, calories, toppings):
        self.name = name
        self.price = price
        self.calories = calories
        self.toppings = toppings
        if self.price <= 0:
            raise ValueError('Price must be greater then 0')
        if self.calories <= 0:
            raise ValueError('Calories must be greater then 0')

    def get_final_price(self, size='Family'):
        if size == 'XL':
            return self.price * 1.15
        elif size == 'Personal':
            return self.price * 0.60
        elif size == 'Family':
            return self.price
        else:
            raise ValueError("We don't have your pizza size")

    def add_topping(self, topping, calories, price):
        if topping not in self.toppings:
            self.toppings.append(topping)
            self.price = self.price + price
            self.calories = self.calories + calories
        else:
            raise ValueError(f'{self.name} already contains {topping}')

    def remove_topping(self, topping, calories, price):
        if topping in self.toppings:
            self.toppings.remove(topping)
            self.price = self.price - price
            self.calories = self.calories - calories
            if self.price <= 0:
                raise ValueError("Price can't be negative ")
            if self.calories <= 0:
                raise ValueError("remaining calories must be greater the 0")
        else:
            raise ValueError(f'{self.name} does not contain {topping}')

#########################################
# Question 3 - do not delete this comment
#########################################


class Meal:

    def __init__(self, beverage, pizza):
        self.beverage, self.pizza = beverage, pizza

    def get_final_price(self, beverage_size, pizza_size):
        return self.beverage.get_final_price(beverage_size) + self.pizza.get_final_price(pizza_size)

    def is_healthy(self):
        return self.beverage.is_diet == True and self.pizza.calories < 1000



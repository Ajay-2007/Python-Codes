# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:19:20 2019

@author: d33ps3curity
"""

class Pants:
    """The pants class represents an article of clothing sold in a store
    """
    
    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object
        
        Args:
            color (str)
            waist_size (int)
            length (int)
            price (float)
            
        Attributes:
            color (str): color of a pants object
            waist_size (int): waist size of a pants object
            length (int): length of a pants object
            price (float): price of a pants object
        """
        
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
        
    def change_price(self, new_price):
        """The change_price method changes the price attribute of pants object
        
        Args:
            new_price (float): the new price of the pants object
            
        Returns: None
        
        """
        self.price = new_price
        
    def discount(self, percentage):
        """The discount method outputs a discounted price of a pants object
        
        Args:
            percentage (float): a decimal representing the amount to discount
        
        Returns:
            float: the discounted price
        """
        return self.price * (1 - percentage)
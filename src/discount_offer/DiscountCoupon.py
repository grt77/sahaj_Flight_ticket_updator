from ..ConfigEnv import load_env_variables
import re



class DiscountCoupon:

    def __init__(self):
        self.env_var=load_env_variables()
        self.offer_code_dict=eval(self.env_var['DISCOUNT_CODES'])

    '''
    
    This is going to use for the applying the discount code based on Fare class , where we passing passenger object 
    
    '''

    def get_discount_code_FareClass(self,passenger):
        for fare_class in self.offer_code_dict:
            discount_offer=self.offer_code_dict[fare_class]
            if re.match("^["+fare_class+"]{1}$",passenger.Fare_class):
                return discount_offer
        return ''



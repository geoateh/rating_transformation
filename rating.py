from scipy.stats import truncnorm
import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt



def transform(rating, origin, myclip_a=None, myclip_b=None ,ev=None, std=None): # Rating is the rating score // origin is the Platform where the rating is from
    # --- ArgCheck ---
    
    if not isinstance(rating, float): raise Exception("Rating has to be floating point number.")
    
    # --- Airbnb ---

    if origin == "airbnb": 

        if ev == None: ev = 4.910833333
        if std == None: std = 0.3040923932
        if myclip_a == None: myclip_a = 0
        if myclip_b == None: myclip_b = 5

        a, b = (myclip_a - ev) / std, (myclip_b - ev) / std # myclip_a and myclip_b are clip values in the sample space and need to be converted to standart deviations

        return round(truncnorm.cdf(rating, a, b, loc = ev, scale = std)*10,2)
        
    # --- Booking ---

    if origin == "booking": 

        if ev == None: ev = 7.876516774
        if std == None: std = 0.9590163867
        if myclip_a == None: myclip_a = 0
        if myclip_b == None: myclip_b = 10

        a, b = (myclip_a - ev) / std, (myclip_b - ev) / std # myclip_a and myclip_b are clip values in the sample space and need to be converted to standart deviations

        return round(truncnorm.cdf(rating, a, b, loc = ev, scale = std)*10,2)

    if origin == "other":
        # TODO: If Arg Arg Check: 
        #   raise Exception("EV, STD, A and B must not be None.") 

        a, b = (myclip_a - ev) / std, (myclip_b - ev) / std # myclip_a and myclip_b are clip values in the sample space and need to be converted to standart deviations

        return round(truncnorm.cdf(rating, a, b, loc = ev, scale = std)*10,2)



def turn_booking_into_airbnb(rating):
   
    if rating > 10: raise Exception("Booking Rating has to be smaller than 10.")
   
    myclip_a_booking, myclip_a_airbnb = 0,0
    myclip_b_booking, myclip_b_airbnb = 10,5
    ev_booking, ev_airbnb = 7.876516774, 4.910833333
    std_booking, std_airbnb = 0.9590163867, 0.3040923932

    a_booking, b_booking = (myclip_a_booking - ev_booking) / std_booking, (myclip_b_booking - ev_booking) / std_booking
    a_airbnb, b_airbnb = (myclip_a_airbnb - ev_airbnb) / std_airbnb, (myclip_b_airbnb - ev_airbnb) / std_airbnb

    booking_cdf = truncnorm.cdf(rating, a_booking, b_booking, loc = ev_booking, scale = std_booking)
    return round(truncnorm.ppf(booking_cdf, a_airbnb, b_airbnb, loc = ev_airbnb, scale = std_airbnb),2)



def turn_airbnb_into_booking(rating):

    if rating > 5: raise Exception("Airbnb Rating has to be smaller than 5.")
    
    myclip_a_booking, myclip_a_airbnb = 0,0
    myclip_b_booking, myclip_b_airbnb = 10,5
    ev_booking, ev_airbnb = 7.876516774, 4.910833333
    std_booking, std_airbnb = 0.9590163867, 0.3040923932

    a_booking, b_booking = (myclip_a_booking - ev_booking) / std_booking, (myclip_b_booking - ev_booking) / std_booking
    a_airbnb, b_airbnb = (myclip_a_airbnb - ev_airbnb) / std_airbnb, (myclip_b_airbnb - ev_airbnb) / std_airbnb

    airbnb_cdf = truncnorm.cdf(rating, a_airbnb, b_airbnb, loc = ev_airbnb, scale = std_airbnb)
    return round(truncnorm.ppf(airbnb_cdf, a_booking, b_booking, loc = ev_booking, scale = std_booking),2)






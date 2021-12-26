# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
 
def take_attendance(classroom,  who_is_here): 
    """
    

   
    classroom, tuple
        
    who_is_here, tuple
            
    Checks if every item in classrooom is in who_is_here
    And prints their name if so.
    Returns "finished taking attendance "

.

    """
    
    for kid in classroom:
        if kid in who_is_here: 
            print(kid)
    return "finished taking attendance"










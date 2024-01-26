def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # min, max, quantity: int, betven 1 to 1000.
    
    import random
    
    get_num_ticket = []
    
    if ((type(min) == int) and (type(max) == int) and (type (quantity) == int)):
        
        if (1 <= min <= 1000) and (1 <= max <= 1000):
            
            if max >= min:
                
                if quantity <= (max - min + 1):
                                        
                    for i in range(min, max + 1):
                        get_num_ticket.append(i)
                                            
                    get_num_ticket = random.sample(get_num_ticket,quantity)
                    
                    return get_num_ticket
            
                else:
                    # ("Incorrect quantity. Quantity must be inside min and max")
                    return get_num_ticket
            
            else:
                # ("Incorrect values. Value min must be less then max")
                return get_num_ticket
    
        else:
            # ("Incorrect values. Value min, max must be between 1 and 1000")
            return get_num_ticket

    else:
        # ("Incorrect type values. Type min, max, quantity must be 'int'")
        return get_num_ticket


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

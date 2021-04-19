
START_SUM = 400000
NDS = 0.13
RATE = 0.07

nds = START_SUM * NDS



def invest(start_sum, years):
    if (years >= 1):
        return start_sum + start_sum*RATE + invest(start_sum + start_sum*RATE, years - 1)
    else:
        return 0 


print(invest(400000,30))

# Buliding a simple control system for nuclear reactor

# check for criticality
# temp < 800k
# neutrons > 500
# product of temp and neutrons is < 500000

from pickle import TRUE


def is_critically_balanced(temparature, neutrons_emitted):
    critical = False
    product = temparature * neutrons_emitted 
    while critical == False:
        if temparature < 800:
            if neutrons_emitted > 500:
                if product < 500000:
                    return True
                
        else:
            return  False



# Determine the power output range

# green = efficiency of 80% or more
# orange -> efficiency of less than 80% but at least 60%,
#red -> efficiency below 60%, but still 30% or more,
# black -> less than 30% efficient.

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = ((generated_power / theoretical_max_power) * 100)

    if efficiency == 80:
        return 'green'
    elif efficiency <= 80:
        return 'orange'
    elif efficiency <= 60:
        return 'red'
    elif efficiency <= 30:
        return 'black'
    else:
        return 'invalid'





new =reactor_efficiency(200,50,15000)
print(new)
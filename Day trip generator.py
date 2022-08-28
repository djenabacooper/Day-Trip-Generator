vacay_destination = ['Chicago', 'New York', 'Miami', 'LA', 'Vegas', 'DC']
restaurants = ['Giordanos', 'Leonas', 'The Purple Pig','Gramercy Tavern', 'La Grande Boucherie', 'Raouls','Red Rooster', 'Cvi.che 105']
transportation = ['Car', 'Train', 'Plane', 'Ferry', 'Bike']
entertainment = ['A play', 'A concert', 'Netflix and chill', 'Museum']

from asyncio.windows_events import NULL
import random

def restaurant_selection_loop(vacay_rest):
    rest_notSatisfied = True
    print(f"Hungry? Here is a restaurant for your consideration.")  
    while rest_notSatisfied:
        rand_rest = random.choices(restaurants, k=1)
        print(rand_rest)
        user_choice_rest = input("Whatcha think? ").lower()
        if user_choice_rest == 'no':
            print("How does this one sound?")
        else: 
            rest_notSatisfied = False
    print("Great, dinner sorted!")
    return rand_rest
  
chosen_rest = restaurant_selection_loop(restaurants)


def destination_selection_loop(destination):
    dest_notSatisfied = True
    print("Ready to travel? Here's a destination for your consideration.")  
    while dest_notSatisfied:
        rand_dest = random.choices(vacay_destination, k=1)
        print(rand_dest)
        user_choice_dest = input("Whatcha think? ").lower()
        if user_choice_dest == 'no':
            print("How does this place sound?")
        else: 
            dest_notSatisfied = False
    print("Great, we have a destination!")
    return rand_dest
  
chosen_dest = destination_selection_loop(vacay_destination)

def transportation_selection_loop(transport):
    notSatisfied = True
    print("Now that we know where we're going, how do you feel about this mode of transport?")  
    while notSatisfied: 
        rand_trans = random.choices(transportation, k=1)
        print(rand_trans)
        user_choice_trans = input("Whatcha think? ").lower()
        if user_choice_trans == 'no':
            print("How about this instead?")
        else: 
            notSatisfied = False
    print("Mode of transport selected!")
    return rand_trans
chosen_trans = transportation_selection_loop(transportation)
def entertainment_selection_loop(vacay_fun):
    fun_notSatisfied = True
    print(f"How shall you amuse yourself? How does this sound?")  
    while fun_notSatisfied:
        rand_fun = random.choices(entertainment, k=1)
        print(rand_fun)
        user_choice_fun = input("Whatcha think? ").lower()
        if user_choice_fun == 'no':
            print("Maybe this?")
        else: 
            fun_notSatisfied = False
    print("Excellent choice, amusement commence!")
    return rand_fun
  
chosen_fun = entertainment_selection_loop(entertainment)    

print(f"All selections have been made! here is your itinerary: \n Location: {chosen_dest} \n Transportation: {chosen_trans} \n Dinner: {chosen_rest} \n Entertainment: {chosen_fun}")
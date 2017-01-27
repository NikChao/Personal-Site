# each day you either make or serve food
# you need 8 making and 10 serving per day


days = {'Saturday':([],[]), 'Sunday':([],[]), 'Monday':([],[])}


# I assume day is a string
# Session is an integer {0,1}
# Session 0 is afternoon, Session 1 is Evening
def is_full(day, session):
    if session == 0:
        if len(days[day][session]) >= 8:
            return True
    else:
        if len(days[day][session]) >= 10:
            return True
    return False


def add_to_roster(name, day, session):
    days[day][session].append(name)
    print(days)


# add line where it tells user about alternatives
def check_input(name, day, session):
    if not is_full(day, session):
        if day not in ['Monday', 'Sunday', 'Saturday']:
            print("invalid day!")
        else:
            add_to_roster(name, day, session)
    else:
        print("session " + str(session) + " on " + day + " is full!")
        
def take_input():

    while(1):
        name = input("Who?")
        day = input("What day?")
        session = int(input("Which session? (0 for afternoon, 1 for evening, 2 for both)"))
        #session = set_session(session)

        if session == 1 or session == 0:
            check_input(name, day, session)    
        elif session == 2:
            check_input(name, day, 0)
            check_input(name, day, 1)
        


def add_a_man():
   man=1

def load_days():
    a = 1

def main():
    load_days()

main()

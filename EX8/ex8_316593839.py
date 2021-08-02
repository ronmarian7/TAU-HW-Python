''' Exercise #8. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################
class RoomError(Exception):
    #A subclass of Exception that defines a new error type
    #DO NOT change this class
    pass

class Room:
    def  __init__(self, floor, number, guests, clean_level, rank, satisfaction = 1.0):
        try:
            self.floor = floor
            self.number = number
            self.guests = [x.lower() for x in guests]
            if type(clean_level) != int:
                raise TypeError('It is not the correct type')
            self.clean_level = clean_level
            if type(rank) != int:
                raise TypeError('It is not the correct type')
            self.rank = rank
            if satisfaction % satisfaction != 0:
                raise TypeError('It is not the correct type')
            self.satisfaction = float(satisfaction)
        except Exception as e:
            raise TypeError('It is not the correct type')

        if self.clean_level < 1 or self.clean_level > 10 or self.rank < 1 or self.rank > 3 or self.satisfaction < 1 \
                or self.satisfaction > 5:
            raise ValueError('You are not in range')


    def __repr__(self):
        if len(self.guests) == 0:
            return f'floor: {self.floor} \nnumber: {self.number} \nguests: empty \nclean_level: ' \
                   f'{self.clean_level} \nrank: {self.rank} \nsatisfaction: {self.satisfaction}'
        return f'floor: {self.floor} \nnumber: {self.number} \nguests: {", ".join(self.guests)} \nclean_level: ' \
               f'{self.clean_level} \nrank: {self.rank} \nsatisfaction: {self.satisfaction}'

    def is_occupied(self):
        return len(self.guests) > 0

    def can_clean(self):
        return True

    def clean(self):
        if self.can_clean():
            self.clean_level = min(10, self.clean_level + self.rank)
        else:
            raise RoomError('Room cannot be cleaned')

    def better_than(self, other):
        if isinstance(other, Room):
            return (self.rank, self.floor, self.clean_level) > (other.rank, other.floor, other.clean_level)
        else:
            raise ValueError('Other must be an instance of Room')

    def check_in(self, guests):
        if len(self.guests) == 0:
            self.guests = [x.lower() for x in guests]
            self.satisfaction = 1.0
        else:
            raise RoomError('Cannot check-in new guests to an occupied room')

    def check_out(self):
        if len(self.guests) != 0:
            self.guests = []
        else:
            raise RoomError('Cannot check-out an empty room')
    
    def move_to(self, other):
        if len(self.guests) == 0:
            raise RoomError('Cannot move guests from an empty room')
        elif len(other.guests) != 0:
            raise RoomError('Cannot move guests into an occupied room')
        else:
            other.guests = self.guests
            if not self.better_than(other):
                other.satisfaction = min(5.0, self.satisfaction + 1.0)
            else:
                other.satisfaction = self.satisfaction
            self.guests = []


#########################################
# Question 2 - do not delete this comment
#########################################
class BudgetRoom(Room):
    def  __init__(self, floor, number, guests, clean_level,\
                  rank=1, satisfaction=1.0, clean_stock=0):
        Room.__init__(self, floor, number, guests, clean_level, rank, satisfaction)
        self.clean_stock = clean_stock

    def __repr__(self):
        str_room = Room.__repr__(self)
        return f'{str_room} \ntype: BudgetRoom\nclean_stock: {self.clean_stock}'

    def can_clean(self):
        if self.clean_stock > 0:
            return True
        else:
            raise RoomError('Room cannot be cleaned')

    def clean(self):
        if super().can_clean():
            super().clean()
            self.clean_stock -= 1

    def check_in(self, guests):
        self.clean_stock = 0
        super().check_in(guests)

    def move_to(self, other):
        super().move_to(other)
        if isinstance(other, Room):
            other.clean_stock = self.clean_stock

    def grant_clean(self):
        if len(self.guests) != 0:
            self.clean_stock += 1
            self.satisfaction = min(5.0, self.satisfaction + 0.5)
        else:
            raise RoomError('Cannot grant an empth room')

    def grant_snack(self):
        if len(self.guests) != 0:
            self.satisfaction = min(5.0, self.satisfaction + 0.8)
            self.clean_level = max(1, self.clean_level -1)
        else:
            raise RoomError('Cannot grant an empth room')



class LegacyRoom(Room):
    def  __init__(self, floor, number, guests, clean_level,\
                  rank=2, satisfaction=1.0,\
                  minibar_drinks = 2, minibar_snacks = 2):
        Room.__init__(self, floor, number, guests, clean_level, rank, satisfaction)
        self.minibar_drinks = minibar_drinks
        self.minibar_snacks = minibar_snacks

    def __repr__(self):
        str_room = Room.__repr__(self)
        return f'{str_room}\ntype: LegacyRoom\nminibar_drinks: {self.minibar_drinks}\nminibar_snacks:' \
               f' {self.minibar_snacks}'

    def check_in(self, guests):
        if len(self.guests) == 0:
            super().check_in(guests)
            self.minibar_snacks = 2
            self.minibar_drinks = 2

    def add_drinks(self, quantity):
        self.minibar_drinks += quantity
        self.satisfaction = min(5.0, self.satisfaction + 0.2*quantity)

    def add_snacks(self, quantity):
        self.minibar_snacks += quantity
        self.satisfaction = min(5.0, self.satisfaction + 0.3 * quantity)
        self.clean_level = max(1, self.clean_level -1)

    # Replace this comment with your methods' implementation


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
    def __repr__(self):
        count_budget = sum(isinstance(x, BudgetRoom) for x in self.rooms)
        count_legacy = sum(isinstance(x, LegacyRoom) for x in self.rooms)
        count_other = len(self.rooms) - count_legacy - count_budget
        count_occupied = sum(len(x.guests)!=0 for x in self.rooms)
        return f"{self.name} hotel has:\n{count_budget} BudgetRooms\n{count_legacy} LegacyRooms\n{count_other} " \
               f"other room types\n{count_occupied} occupied rooms"

    def check_in(self, guests, rank):
        for x in self.rooms:
            if len(x.guests) == 0 and x.rank == rank:
                x.check_in(guests)
                return x
        return None

    def check_out(self, guest):
        for x in self.rooms:
            for y in x.guests:
                if guest.lower() in y:
                    x.check_out()
                    return x
        return None

    def upgrade(self, guest):
        for x in self.rooms:
            if guest.lower() in x.guests:
                for room in self.rooms:
                    if room.better_than(x) and len(room.guests) ==0:
                        x.move_to(room)
                        return room
        return None


#########################################
# Question 3 supplement - do not delete this comment
#########################################
def test_hotel():
    rooms = [BudgetRoom(15, 140, [], 5), LegacyRoom(12, 101, ["Ronen", "Shir"], 6),\
             BudgetRoom(1, 2, ["Liat"], 7), Room(2, 23, [], 6, 3)]
    h = Hotel("Dan",rooms)
    test_sep = '\n------------------'
    print ('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
    print ('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep,  sep="")
    print ('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print ('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(["Alice", "Wonder"], 2), test_sep, sep="")
    print ('CALL: h.check_in(["Alex"], 3)\n', h.check_in(["Alex"], 3), test_sep, sep="")
    print ('PRINT h:\n', h, test_sep, sep="")
    print ('CALL: h.check_in(["Oded", "Shani"], 3)\n', h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
    print ('CALL: h.check_in(["Oded", "Shani"], 1)\n', h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
    print ('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print ('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print ('PRINT h:\n', h, test_sep, sep="")


#########################################
# Main code - do not delete this comment
# You can add more validation cases below
#########################################

##test_hotel()
## After you are done implenting all classes and methods, you may comment-in the call to test_hotel() and compare the results with the content of test_hotel_output.txt
'''
Name: Shubham Mohole
Program Description: Below are the tests for Max Flow
'''


from MaxFlow import *


#Excersise 1:

print("General Max Flow Test:")
def generalMaxFlowTest():
    test = Network()
    test.add_node("v1")
    test.add_node("v2")
    test.add_node("v3")
    test.add_node("v4")
    test.add_edge("S", "v1", 16)
    test.add_edge("S", "v2", 13)
    test.add_edge("v1", "v3", 12)
    test.add_edge("v2", "v1", 4)
    test.add_edge("v2", "v4", 14)
    test.add_edge("v4", "v3", 7)
    test.add_edge("v3", "T", 20)
    test.add_edge("v3", "v2", 9)

    test.add_edge("v4", "T", 4)
    test.solve_network()
generalMaxFlowTest()
print("------")

#Excersise 2:

print("Snack Test:")
def snackTest():
    snackNetwork = Network()
    snackNetwork.add_node("Alice")
    snackNetwork.add_node("Bob")
    snackNetwork.add_node("Chris")
    snackNetwork.add_node("Dawn")
    snackNetwork.add_node("Edward")
    snackNetwork.add_node("Thin Mints")
    snackNetwork.add_node("Snickers")
    snackNetwork.add_node("Reese's Pieces")
    snackNetwork.add_node("KitKat")
    snackNetwork.add_node("Pocky")
    snackNetwork.add_node("Chex Mix")
    snackNetwork.add_edge("Alice", "Thin Mints", 1)
    snackNetwork.add_edge("Alice", "Reese's Pieces", 1)
    snackNetwork.add_edge("Bob", "Snickers", 1)
    snackNetwork.add_edge("Bob", "Reese's Pieces", 1)
    snackNetwork.add_edge("Bob", "KitKat", 1)
    snackNetwork.add_edge("Chris", "Chex Mix", 1)
    snackNetwork.add_edge("Chris", "Pocky", 1)
    snackNetwork.add_edge("Chris", "Snickers", 1)
    snackNetwork.add_edge("Dawn", "Chex Mix", 1)
    snackNetwork.add_edge("Edward", "Thin Mints", 1)
    snackNetwork.add_edge("Edward", "Reese's Pieces", 1)
    snackNetwork.add_edge("Edward", "KitKat", 1)
    snackNetwork.add_edge("Edward", "Pocky", 1)
    snackNetwork.add_edge("Edward", "Snickers", 1)
    snackNetwork.add_edge("Edward", "Chex Mix", 1)
    snackNetwork.add_edge("S", "Alice", 1)
    snackNetwork.add_edge("S", "Bob", 1)
    snackNetwork.add_edge("S", "Chris", 1)
    snackNetwork.add_edge("S", "Dawn", 1)
    snackNetwork.add_edge("S", "Edward", 1)
    snackNetwork.add_edge("Thin Mints", "T", 1)
    snackNetwork.add_edge("Reese's Pieces", "T", 1)
    snackNetwork.add_edge("KitKat", "T", 1)
    snackNetwork.add_edge("Pocky", "T", 1)
    snackNetwork.add_edge("Snickers", "T", 1)
    snackNetwork.add_edge("Chex Mix", "T", 1)

    # we can also reverse how our graph looks if have the snacks connected to the source and the people connected
    # to the people. This makes more logical sense since we distribute the snacks to the people.


    snackNetwork.solve_network()
snackTest()
print("------")

#Excersise 3:

print("Debt Test:")
def debtTest():
    debtNetwork = Network()

    debtNetwork.add_node("A")
    debtNetwork.add_node("B")
    debtNetwork.add_node("C")
    debtNetwork.add_node("D")

    # node C since is not net giver but recipient although there is available funds we do not connect C to source but connect it to target
    debtNetwork.add_edge("S", "A", 4)
    debtNetwork.add_edge("A", "B", math.inf)
    debtNetwork.add_edge("A", "C", math.inf)
    debtNetwork.add_edge("B", "C", math.inf)
    debtNetwork.add_edge("C", "D", math.inf)

    debtNetwork.add_edge("B", "T", 1)
    debtNetwork.add_edge("C", "T", 2)
    debtNetwork.add_edge("D", "T", 1)

    debtNetwork.solve_network()

    counterCase = Network()

    counterCase.add_node("A")
    counterCase.add_node("B")
    counterCase.add_node("C")
    counterCase.add_node("D")

    counterCase.add_edge("S", "A", 2)


    counterCase.add_edge("A", "B", math.inf)
    counterCase.add_edge("A", "C", math.inf)

    counterCase.add_edge("B", "D", math.inf)

    counterCase.add_edge("C", "D", math.inf)

    counterCase.add_edge("B", "T", 0)
    counterCase.add_edge("C", "T", 0)
    counterCase.add_edge("D", "T", 2)

    counterCase.solve_network()

debtTest()

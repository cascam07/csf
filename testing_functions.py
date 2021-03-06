# Name: Cameron Casey
# Evergreen Login: cascam07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 8

import networkx as nx
import matplotlib.pyplot as plt
import operator
import random


###
### Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_node("A")
practice_graph.add_node("B")
practice_graph.add_node("C")
practice_graph.add_node("D")
practice_graph.add_node("E")
practice_graph.add_node("F")


practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")


assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

def draw_practice_graph():
    """Draw practice_graph to the screen."""
    nx.draw(practice_graph)
    plt.show()

#draw_practice_graph()


###
### Problem 1b
###

rj = nx.Graph()

people = ['Nurse','Juliet','Tybalt','Capulet','Friar Laurence','Romeo','Benvolio','Montague',
        'Escalus','Mercutio','Paris']
rj.add_nodes_from(people)

rj.add_edge('Nurse','Juliet')
rj.add_edge('Juliet','Tybalt')
rj.add_edge('Juliet','Friar Laurence')
rj.add_edge('Juliet','Romeo')
rj.add_edge('Juliet','Capulet')
rj.add_edge('Friar Laurence','Romeo')
rj.add_edge('Capulet','Tybalt')
rj.add_edge('Capulet','Escalus')
rj.add_edge('Capulet','Paris')
rj.add_edge('Romeo','Benvolio')
rj.add_edge('Romeo','Montague')
rj.add_edge('Romeo','Mercutio')
rj.add_edge('Montague','Benvolio')
rj.add_edge('Montague','Escalus')
rj.add_edge('Escalus','Mercutio')
rj.add_edge('Escalus','Paris')
rj.add_edge('Paris','Mercutio')

assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

def draw_rj():
    """Draw the rj graph to the screen and to a file."""
    nx.draw(rj)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

#draw_rj()


###
### Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    The parameter 'user' is the string name of a person in the graph.
    """
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given graph.
    The result does not include the given user nor any of that user's friends.
    """
    f_of_f = {user}
    for friend in friends(graph, user):
        f_of_f.update(friends(graph, friend))
    for friend in friends(graph, user):
        if friend in f_of_f:
            f_of_f.remove(friend)
        else: continue
    f_of_f.remove(user)    
    return f_of_f
    
def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common."""
    user1_friends = friends(graph, user1)
    user2_friends = friends(graph, user2)
    return user1_friends.intersection(user2_friends)
    
def number_of_common_friends_map(graph, user):
    """Returns a map from each user U to the number of friends U has in common with the given user.
    The map keys are the users who have at least one friend in common with the
    given user, and are neither the given user nor one of the given user's friends.
    Take a graph G for example:
        - A and B have two friends in common
        - A and C have one friend in common
        - A and D have one friend in common
        - A and E have no friends in common
        - A is friends with D
    number_of_common_friends_map(G, "A")  =>   { 'B':2, 'C':1 }
    """
    user_friends = friends(graph, user)
    users = graph.nodes()
    users.remove(user)
    users_copy=users[:]
    for i in users_copy:
        if i in user_friends:
            users.remove(i)
        else:pass 
    friends_in_common = {person:len(common_friends(graph,user,person)) for person in users
    if len(common_friends(graph,user,person)) > 0}
    return friends_in_common

def number_map_to_sorted_list(map1):
    """Given a map whose values are numbers, return a list of the keys.
    The keys are sorted by the number they map to, from greatest to least.
    When two keys map to the same number, the keys are sorted by their
    natural sort order, from least to greatest."""

    tuples = []
    sorted_list = []
    for i in map1:
        tuples.append((i,map1[i]))
    sort = 1
    while sort > 0:
        sort = 0
        for x in range(len(tuples)-1,0,-1):
            if tuples[x][1]>tuples[x-1][1]:
                temp = tuples[x]
                tuples[x] = tuples[x-1]
                tuples[x-1] = temp
                sort += 1
            else: pass
    sort = 1
    while sort > 0:
        sort = 0
        for x in range(len(tuples)-1,0,-1):
            if tuples[x][1]==tuples[x-1][1]:
                if tuples[x][0]<tuples[x-1][0]:
                    temp = tuples[x]
                    tuples[x] = tuples[x-1]
                    tuples[x-1] = temp
                    sort += 1
                else:pass
            else: pass
    for y in tuples:
        sorted_list.append(y[0])
    return sorted_list     
        
    

    
result = number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5})
print result


def state_edges(election_result_rows):
    """
    Given a list of election result rows, returns state edges.
    The input list does has no duplicate states;
    that is, each state is represented at most once in the input list.
    """
    dict_edge = {}
    for state in election_result_rows:
        edge = float(state['Dem']) - float(state['Rep'])
        dict_edge[str(state['State'])] = edge
    print dict_edge == test_row
    return dict_edge
    
rows2 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1'},
               {'State': 'CA', 'Dem': '0.2', 'Rep': '1.3'},]
test_row = {'WA':0.9, 'CA':-1.1}               
result = state_edges(rows2)
print result

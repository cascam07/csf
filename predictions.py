import time

def row_to_edge(row):
    """
    Given an election result row or poll data row, returns the Democratic edge
    in that state.
    """
    return float(row["Dem"]) - float(row["Rep"]) 

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
    return dict_edge

def earlier_date(date1, date2):
    """
    Given two da
    tes as strings (formatted like "Oct 06 2012"), returns True if 
    date1 is after date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of poll data rows, returns the most recent row with the
    specified pollster and state. If no such row exists, returns None.
    """
    temp_poll = poll_rows[:]
    i=0
    for poll in temp_poll[:]: #removes all polls with pollsters other than input
        if poll['Pollster'] != pollster:
            del temp_poll[i]
            i -=1
        i +=1
    i=0
    for poll in temp_poll[:]: #removes all polls with states other than input
        if poll['State'] != state:
            del temp_poll[i]
            i -=1
        i +=1
    if len(temp_poll) == 0: #returns none if no polls meet criteria
        return None
    else:
        temp_max = "Jan 01 1000" #arbitrary starting comparison date
        for n in temp_poll: #checks temp_max for most recent date
            if earlier_date(temp_max, n['Date'])==True:
                temp_max = n['Date']  #temp_max becomes most recent date
            else: pass
        for n in temp_poll:
            if n['Date'] == temp_max:
                most_recent_poll = n
                return most_recent_poll
            else: continue
            
def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string), returns a set
    containing all values in that column.
    """
    result = set()
    for poll in rows:
        result.add(poll[column_name])
    return result  


def pollster_predictions(poll_rows):
    
    #Given a list of poll data rows, returns pollster predictions.
    
    pollster_keys = [] #unique pollster types "PPP" "IPSOS"
    sub_pollster=[]
    pollsters = [] #list of lists. Each sublist represents a pollster with states
    unique_state = []
    recent_polls = []
    for row in poll_rows:
        pollster_elements = unique_column_values(poll_rows,'Pollster')
    for i in range(len(pollster_elements)):
        pollster_keys.append(pollster_elements.pop())
        
    for poll in pollster_keys:
        pollsters.append(sub_pollster)
        sub_pollster=[]
        for row in poll_rows:
            if row["Pollster"]==poll:
                sub_pollster.append(row)
            else: continue
    del(pollsters[0])
    pollsters.append(sub_pollster)
            
    for row in poll_rows:
        state_elements = unique_column_values(poll_rows,'State')
    for i in range(len(state_elements)):
        unique_state.append(state_elements.pop())
        
    
    for row in range(len(pollsters)): #Filters out all but the most recent polls for each
        for poll in pollster_keys:    #pollster and state
            for state in unique_state:
                if most_recent_poll_row(pollsters[row], poll, state) != None:
                    recent_polls.append(most_recent_poll_row(pollsters[row], poll, state))
                else: continue    
    
   
    
    #dict_inner = {row['State']:row_to_edge(row) for row in recent_polls}
    inner_dicts = []
    dict_outter = {}
    for pollster in pollster_keys:
        dict_inner = {}
        for row in recent_polls:
            if row['Pollster']==pollster:
                dict_inner = {row['State']:row_to_edge(row)}
                inner_dicts.append(dict_inner)
            else: continue
        dict_outter[row['Pollster']]=dict_inner
        #dict_outter = {row['Pollster']:inner_dicts for row in recent_polls}
    
    return dict_outter, recent_polls
    
    
"""
def pollster_predictions(poll_rows):
    
    #Given a list of poll data rows, returns pollster predictions.
    
    dict_inner = {row['State']:row_to_edge(row) for row in poll_rows}
    
    dict_outter = {row['Pollster']:dict_inner for row in poll_rows}
    return dict_inner, dict_outter
"""

rows1 = [{'State': 'WA', 
                'Dem': '1.0', 
                'Rep': '0.1', 
                'Date': 'Nov 04 2008', 
                'Pollster': 'PPP'}]
#assert pollster_predictions(rows1) == {'PPP': {'WA': 0.9}}                

rows2 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]                
#assert pollster_predictions(rows2) == {'PPP': {'WA': 0.9, 'CA': -9.3}}

rows3 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},
      {'State': 'WA', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'},
      {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'IPSOS'}]
    #assert pollster_predictions(rows3) == {'PPP': {'WA': 0.9, 'CA': -1.1}, 
                                             #'IPSOS': {'WA': 2.0, 'CA': -9.3}}
                                             
rows4 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'WA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]
    #assert pollster_predictions(rows4) == {'PPP': {'WA': 0.9}}                                            
                                                                                                
result = pollster_predictions(rows3)
print result
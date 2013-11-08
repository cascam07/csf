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


def pollster_predictions(poll_rows):
    """
    Given a list of poll data rows, returns pollster predictions.
    """
    temp = []
    for i in poll_rows
    for pollster in poll_rows['Pollster']:
        for state in poll_rows['State']:
            temp.append(most_recent_poll_row(poll_rows, pollster, state))
    return temp

rows1 = [{'State': 'WA', 
                'Dem': '1.0', 
                'Rep': '0.1', 
                'Date': 'Nov 04 2008', 
                'Pollster': 'PPP'}]
                
result = pollster_predictions(rows1)
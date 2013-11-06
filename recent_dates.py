def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of poll data rows, returns the most recent row with the
    specified pollster and state. If no such row exists, returns None.
    """
    temp_poll = poll_rows
    i=0
    for poll in temp_poll[:]:
        if poll['Pollster'] != pollster:
            del temp_poll[i]
            i -=1
        i +=1
    i=0
    for poll in temp_poll[:]:
        if poll['State'] != state:
            del temp_poll[i]
            i -=1
        i +=1
    return temp_poll

poll_rows1 = [{"ID":1, "State":"WA", "Pollster":"A", "Date":"Jan 07 2010"},
              {"ID":2, "State":"WA", "Pollster":"B", "Date":"Mar 21 2010"},
              {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"},
              {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"},
              {"ID":5, "State":"WA", "Pollster":"B", "Date":"Feb 10 2010"},
              {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"}]

result = most_recent_poll_row(poll_rows1, "A", "WA")
print result
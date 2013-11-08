def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string), returns a set
    containing all values in that column.
    """
    result = set()
    for poll in rows:
        result.add(poll[column_name])
    return result    
        
poll_rows1 = [{"ID":1, "State":"WA", "Pollster":"A", "Date":"Jan 07 2010"},
              {"ID":2, "State":"WA", "Pollster":"B", "Date":"Mar 21 2010"},
              {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"},
              {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"},
              {"ID":5, "State":"WA", "Pollster":"B", "Date":"Feb 10 2010"},
              {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"}]
              
answer1 = unique_column_values(poll_rows1, "ID")
answer2 = unique_column_values(poll_rows1, "State")
answer3 = unique_column_values(poll_rows1, "Pollster")
answer4 = unique_column_values(poll_rows1, "Date")

def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted state edges and actual state edges, returns
    the average error of the prediction.
    """
    states = [] #list of states that appear in the predicted and actual edges
    state_pairs = [(i, j) for i in state_edges_predicted for j in state_edges_actual]
    summation = 0
    for pairs in state_pairs:
        if pairs[0] == pairs[1]:
            states.append(pairs[0])
        else: continue
    for state in states:
        summation += abs(state_edges_predicted[state] - state_edges_actual[state])
    average = summation/float(len(states))
    return average
    
def pollster_errors(pollster_predictions, state_edges_actual):
    """
    Given pollster predictions and actual state edges, retuns pollster errors.
    """
    error = {}
    for pollster in pollster_predictions:
        for state in pollster_predictions[pollster]:
            error[pollster]=average_error(pollster_predictions[pollster], state_edges_actual)
    return error


state_edges_pred_1 = {'WA': 1.0, 'CA': -2.3, 'ID': -20.1}
state_edges_act_1 = {'WA': 2.1, 'CA': -1.4, 'ID': -19.1}
#assert average_error(state_edges_pred_1, state_edges_act_1) == 1.0

state_edges_pred_3 = {'WA': 1.0, 'CA': 2.0}
state_edges_act_3 = {'WA': 2.0, 'CA': 1.0, 'MA': 2.4, 'OR': -3.9}
#assert average_error(state_edges_pred_3, state_edges_act_3) == 1.0 

predictions = {
'PPP': {'WA': 1.0, 'CA': -2.0, 'ID': -20.0}, 
'ISPOP': {'WA': 2.0, 'ID': -19.0} 
}
actual = {'WA': 2.0, 'CA': -1.0, 'ID': -19.0, 'OR': 2.2, 'DC': 0.1}
#assert pollster_errors(predictions, actual) == {'PPP': 1.0, 'ISPOP': 0.0}       

result = pollster_errors(predictions, actual)
print result
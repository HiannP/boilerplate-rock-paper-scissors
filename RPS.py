def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'R'
        opponent_history.clear()
        play_order.clear()
        
    opponent_history.append(prev_play)
    
    n = 4
    guess = "R" 
    
    if len(opponent_history) >= n:
        if len(opponent_history) > n:
            pattern = "".join(opponent_history[-(n+1):])
            play_order[pattern] = play_order.get(pattern, 0) + 1
        
        last_moves = "".join(opponent_history[-n:])
        
        potential_plays = [
            last_moves + "R",
            last_moves + "P",
            last_moves + "S",
        ]
        
        sub_order = {
            k: play_order[k] for k in potential_plays if k in play_order
        }
        
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]
            ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
            guess = ideal_response[prediction]
            
    return guess
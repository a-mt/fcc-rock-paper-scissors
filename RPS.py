
def player(prev_play, opponent_history=[], sequences={}):
  stride = 3

  # Keep track of the opponent history
  if prev_play != '':
    opponent_history.append(prev_play)

  # Not enough data to predict anything
  if len(opponent_history) <= stride:
    return "R"

  # Cap opponent_history
  if len(opponent_history) > stride + 1:
    opponent_history.pop(0)

  # Increment last sequence of 4
  seq = "".join(opponent_history)
  sequences[seq] = sequences.get(seq, 0) + 1

  # Predict next move based on previous sequences
  seq     = "".join(opponent_history[-stride:])
  predict = max([seq+"R", seq+"P", seq+"S"],
                  key=lambda key: sequences.get(key,0))[-1]

  if predict == "R": return "P"
  if predict == "P": return "S"
  return "R"
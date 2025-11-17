import random
from typing import TypeVar, List, Tuple

X = TypeVar('X') # generic type to represent a data point

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
  """Split data into fractions [prob, 1-prob]"""
  data = data[:]                  # make a shallow copy?
  random.shuffle(data)            # because shuffle modifies the list
  cut = int(len(data) * prob)     # use prob to find a cutoff
  return data[:cut], data[cut:]   # and split the shuffled list there.

data = [n for n in range(1000)]
train, test = split_data(data, 0.75)

assert len(train) == 750         # assert doesn't log/output anything 
assert len(test) == 250          # but will terminate code

assert sorted(train + test) == data

#if __name__ == "__main__":
#  main()
size_list = 6

def hash_func(value):
  return value % size_list

def map_hash2index(hash_return_value):
  return hash_return_value

def create_hash_table(list_values, main_list):
  for value in list_values:
    hash_return_value = hash_func(value)
    list_index = map_hash2index(hash_return_value)
    if main_list[list_index] is not None:
       print(f'Collision detected for value {value} at index {list_index}. Adding to the chain.')
       main_list[list_index].append(value)
    else:
       main_list[list_index] = [value]

list_values = [1, 3, 4, 8, 3, 5]

main_list = [None for _ in range(size_list)]
print("Initial hash table:", main_list)

create_hash_table(list_values, main_list)
print("Hash table after insertion:", main_list)

input_list:list[int] = list(map(int,input('標準入力 : ').split()))

exec_count:int = 0

def bubble_sort(input_list:list[int]) -> list[int]:
  global exec_count
  count:int = 0
  elm_count:int = len(input_list)
  max_index:int = elm_count - 1 
  while max_index > 0: 
    index:int = 0
    for val in input_list[0:max_index]:
      left_val:int = input_list[index]
      right_index:int = index + 1

      if input_list[index] >  input_list[index + 1]:
        right_val:int = input_list[right_index]
        input_list[right_index] = left_val 
        input_list[index] = right_val 

      index += 1 
      exec_count += 1
    count += 1
    max_index -= 1
  return input_list
print(bubble_sort(input_list))
print('実行回数 : ' + str(exec_count) + '回')

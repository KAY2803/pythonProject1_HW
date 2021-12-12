def list_sort(lst):
  new_lst = sorted([d for d in lst])
  new_lst.reverse()
  return new_lst

lst = [101, 5, 77, 7, 8, 12, 16, 98]
print(list_sort(lst))


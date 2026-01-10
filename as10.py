a={1,2,3,3,4,5}
def list_to_set(lst):
    return set(lst)
def set_to_list(st):
    return list(st)
converted_set=list_to_set(converted_list)
converted_list=set_to_list(converted_set)
print(converted_set)
print(converted_list)

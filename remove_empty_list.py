
def remove_nested_list(listt):
    for val in listt:
        if not isinstance(val,list):
            yield val
        else:
            yield from remove_nested_list(val)
  

a = [[1,2,3,[]],[],[[]],[],[4,5,6,7]]
print(f"before-->{a}")
print(list(remove_nested_list(a)))

# to remove all occurance of an  element in a list
def removeall_replace(element, lst):
    t = [y for y in lst if y != element]
    del lst[:]
    lst.extend(t)
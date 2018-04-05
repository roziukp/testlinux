"""
  Given list with tuples of intervals in any order.
  Function should merge overlapping intervals into one and
  return a list of tuples which should have only mutually exclusive intervals
"""


'''First version of the task, Please uncomment to run the function!'''
def merge_intervals(intervals: list):
    sort_=sorted(intervals)                                                 # сортируем список
    intervals_arr = [(sort_[0])]                                            # заполняем список первым кортежом
    for interv in sort_:                                                    # делаем обход по сортированому списку кортежей
        if interv[1] > intervals_arr[-1][1] > intervals_arr[-1][0]:         # делаем проверку если первый элемент кортежа в очереди больше первго и второго элем. кортежа в списке
            if intervals_arr[-1][0] == interv[0]:                           # если первый елем. котежей одинаковый, заменяем кортеж в списке
                intervals_arr[-1] = (interv)
            else:
                intervals_arr.append(interv)                                # иначе, добавляем кортеж в список
    return intervals_arr



print(merge_intervals([(1, 3), (4, 6), (1, 7), (9, 10)]))  # [(1, 7), (9, 10)]
print(merge_intervals([(1, 2), (4, 6), (1, 3)]))  # [(1, 3), (4, 6)]
print(merge_intervals([(9, 10), (8, 10), (0, 1)]))  # [(0, 1), (8, 10)]

"""
  Given string with parentheses expression.
  Function should examine whether the pairs and order of parentheses are correct.
  Possible input characters in string are: `(){}[]`
  """

'''В принципе была еще задумка, попробовать сделать эту задачку через ф-и split() и reversed()'''


'''First version of the task, Please uncomment to run the function!'''
# Не работае когда str('{}()[]')
def is_valid_parentheses(parentheses: str):
    bool = False                                                          # делаем флаг
    if len(parentheses)%2 == 0:                                           # чтобы отношение было правильным надо парное количество скобок, делаем проверку
        probably_combination = [("(", ")"), ("{", "}"), ("[", "]")]       # создаем массив возможных комбинацый скобок

        current_combination = []                                          # формируем пустой массив для записи

        for i in range(int(len(parentheses)/2)):
            current_combination.append((parentheses[i],parentheses[-i-1])) # заполняем массив комбинациями скобок, с даной строки

        for i in current_combination:
            if i in probably_combination:                                   # проверяем наличие комбинаций скобок в кортежах в константном массиве
                bool=True                                                   # меняем флаг
            else:
                return False                                                # при неудачи возвращаем False
    return bool                                                             # возвращаем результат


'''Second version of the task, Please uncomment to run the function!'''
# def is_valid_parentheses(parentheses: str):
#     opend = ("(" , "{" , "[")                                     # формируем два константных массива из откр. и закр. скобок
#     locked = (")" , "}" , "]")                                    #
#     bool=False                                                    # ставим флаг
#     if len(parentheses)%2 !=0:                                    # проверяем парность скобок
#         return False                                              # при неудачи - False
#     else:
#         for i in range(int(len(parentheses)/2)):
#             if opend.index(parentheses[i]) == locked.index(parentheses[-i-1]):       # сравниваем индексы откр. и закр. скобок
#                 bool = True                                                          # меняем флаг
#             else:
#                 return False                                                         # при неудачи - False
#         return bool                                                                  # возвращаем результат


'''JavaScript
                решение'''
# var
# balancedParens = function(str)
# {
#     var
# stack = [];
# var
# open = {'{': '}', '[': ']', '(': ')'};
# var
# closed = {'}': true, ']': true, ')': true};
#
# for (var i = 0; i < str.length; i ++)
# {
#     var
# chr = str[i];
# if (open[chr])
# {
#     stack.push(chr);
# } else if (closed[chr]) {
# if (open[stack.pop()] != = chr)
# return false;
# }
# }
#
# return stack.length === 0;
# };



print(is_valid_parentheses("()"))  # True
print(is_valid_parentheses("())"))  # False
print(is_valid_parentheses("({})"))  # True
print(is_valid_parentheses("({)}"))  # False
print(is_valid_parentheses("{(({)}))}"))  # False
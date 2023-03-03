def arithmetic_arranger(lst, viz=False):

  def check_operator(simbol):
    if simbol == '+' or simbol == '-':
      return True

  def check_operand(number):
    if number.isdigit():
      return True
      
  def check_number_len(num):
    if len(num) < 5:
      return True
  
  def get_result(num_1, simbol, num_2):
    return eval(f'{num_1} {simbol} {num_2}')

  if len(lst) > 5:
    return "Error: Too many problems."

  top_row = ""
  bottom_row = ""
  dash_line = ""
  res_line = ""
  
  for l in lst:
    l = l.split()
    num_1 = l[0]
    simbol = l[1]
    num_2 = l[2]

    if not check_operator(simbol):
      return "Error: Operator must be '+' or '-'."

    if not check_operand(num_1) or not check_operand(num_2):
      return "Error: Numbers must only contain digits."

    if not check_number_len(num_1) or not check_number_len(num_2):
      return "Error: Numbers cannot be more than four digits."

    max_len = max(len(num_1), len(num_2))
    res = get_result(num_1, simbol, num_2)

    top_row += num_1.rjust(max_len + 2)
    top_row += ' ' * 4
    
    bottom_row = bottom_row + simbol + " " * (1 + max_len - len(num_2)) + num_2
    bottom_row += ' ' * 4 

    dash_line += "-" * (max_len + 2)
    dash_line += ' ' * 4

    res_line += " " * (2 + max_len - len(str(res))) + str(res)
    res_line += ' ' * 4
     
  if viz:
    return "\n".join((top_row, bottom_row, dash_line, res_line))  

'''
LC: https://leetcode.com/problems/remove-invalid-parentheses/

We will utilize a DFS approach. The problem is fairly involved/complex, so no explanation is provided with the code.
Refer to the following explanation:
https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution/113024

# TODO: discuss space/time complexity analysis
'''

def removeInvalidParentheses(self, s):
  results = []
  self.remove(s, 0, 0, results)
  return results


def remove(self, str_to_check, start_to_count, start_to_remove, results, pair = ['(', ')']):
  count = 0
  for count_i in range(start_to_count, len(str_to_check)):
    if str_to_check[count_i] == pair[0]: count += 1
    elif str_to_check[count_i] == pair[1]: count -= 1

    if count >= 0: continue

    for remove_i in range(start_to_remove, count_i + 1):

      if str_to_check[remove_i] == pair[1] and (remove_i == start_to_remove or str_to_check[remove_i-1] != str_to_check[remove_i]):
        new_str_to_check = str_to_check[:remove_i] + str_to_check[remove_i + 1:]
        new_start_to_count = count_i
        new_start_to_remove = remove_i

        self.remove(new_str_to_check, new_start_to_count, new_start_to_remove, results, pair)

    return

  reversed_str_to_check = str_to_check[::-1]
  if pair[0] == '(':
    self.remove(reversed_str_to_check, 0, 0, results, pair = [')', '('])
  else:
    results.append(reversed_str_to_check)
    
# all leetcode tests pass as of 11th Nov 2019

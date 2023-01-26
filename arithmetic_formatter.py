def arithmetic_arranger(problems, answers = False):
    if len(problems) > 5:
          return ('Error: Too many problems.')
      
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    for problem in problems:
        s = problem.split()
        if s[1] == '/' or s[1] == '*':
            return "Error: Operator must be '+' or '-'."
        if s[0].isdigit() == False or s[2].isdigit() == False:
            return ("Error: Numbers must only contain digits.")
        if len(s[0]) > 4 or len(s[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if len(s[0]) > len(s[2]):
            l = (len(s[0])+1) - len(s[2])
            line1 = line1 + (' '*2 + s[0]) + ' '*4
            line2= line2+ (s[1] + ' '*l + s[2]) + ' '*4
            line3= line3+ ('-'*(len(s[0])+2)) + ' '*4
            if s[1] == '+':
                cal = str(int(s[0]) + int(s[2]))
                line4= line4+ (' '*((len(s[0])+2) - len(cal))) + cal + ' '*4
            else:
                cal = str(int(s[0]) - int(s[2]))
                line4= line4+ (' '*((len(s[0])+2) - len(cal))) + cal + ' '*4
                    
           
        elif len(s[0]) < len(s[2]):
            l = (len(s[2])+2) - len(s[0])
            line1 = line1 + (' '*l + s[0]) + ' '*4 
            line2= line2+ (s[1] + ' ' + s[2]) + ' '*4
            line3= line3+ ('-'*(len(s[2])+2)) + ' '*4
            if s[1] == '+':
                cal = str(int(s[0]) + int(s[2]))
                line4= line4+ (' '*((len(s[2])+2)-len(cal))) + cal + ' '*4
            else:
                cal = str(int(s[0]) - int(s[2]))
                line4= line4+ (' '*((len(s[2])+2)-len(cal))) + cal + ' '*4
                
        else:
            line1 = line1 + (' '*2 + s[0]) + ' '*4
            line2= line2+ (s[1] + ' ' + s[2]) + ' '*4
            line3= line3+ ('-'*(len(s[2])+2)) + ' '*4
            if s[1] == '+':
                cal = str(int(s[0]) + int(s[2]))
                line4= line4+ (' '*((len(s[2])+2) - len(cal))) + cal + ' '*4    
            else:
                cal == str(int(s[0]) - int(s[2]))
                line4= line4+ (' '*((len(s[2])+2) - len(cal))) + cal + ' '*4
    

    if answers == False:
        arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip()
    else:
        arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() + '\n' + line4.rstrip()


    return arranged_problems
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))

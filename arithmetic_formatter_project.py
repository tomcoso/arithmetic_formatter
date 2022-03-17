# 12_03_22 /16_03_22  T Dessy

def arithmetic_arranger(problems, solved = False):
    if len(problems) > 5 : 
        return "Error: Too many problems."                         #Error flag 1
        exit()
    prblm = list()
    solved_prblm = 0
    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for iter in problems :
        prblm = iter.split("+") #tries splitting by operator "+"
        if len(prblm) == 2 :
            try:
                solved_prblm = int(prblm[0]) + int(prblm[1])    #solves, if splitted
                op = "+"
            except:
                return "Error: Numbers must only contain digits."   #Error flag 2
        elif len(prblm) != 2 :
            prblm = iter.split("-") #tries splitting by operator "-"
            if len(prblm) == 2:
                try:
                    solved_prblm = int(prblm[0]) - int(prblm[1])    #solves, if splitted
                    op = "-"
                except:
                    return "Error: Numbers must only contain digits."
            else :
                return "Error: Operator must be '+' or '-'."        #Error flag 3
        for each_term in prblm :
            each_term = each_term.strip()
            if len(each_term) > 4 :
                return "Error: Numbers cannot be more than four digits."    #Error flag 4
        if len(prblm[0]) > len(prblm[1]) :  #creates lenght of each problem
            lenght = len(prblm[0]) + 1
        else:
            lenght = len(prblm[1]) + 1

        if iter != problems[-1] :
            line1 += prblm[0].rjust(lenght) + "    "           #creates each line as a string
            line2 += op + prblm[1].rjust(lenght-1) + "    "
            line3 += "-"*lenght + "    "
            line4 += f"{str(solved_prblm).rjust(lenght)}    "
        else:
            line1 += prblm[0].rjust(lenght)          #on the last problem it doesnt add the tab
            line2 += op + prblm[1].rjust(lenght - 1)
            line3 += "-"*lenght
            line4 += str(solved_prblm).rjust(lenght)
    arranged_problems = f""" {line1.rstrip()}
{line2.strip()}
{line3.strip()}"""
    if solved == True :                         #creates the "optional" from optional argument
        arranged_problems = f""" {line1.rstrip()}
{line2.strip()}
{line3.strip()}
{line4.rstrip()}"""  #arranges each line

    return arranged_problems
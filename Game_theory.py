
from numpy import random

def amsh(opp_move = None):
     global flag_amsh
     global counter_amsh
     global op_moves_amsh
     global my_moves_amsh

     if (opp_move == None):
          counter_amsh = 1
          op_moves_amsh = []
          flag_amsh = False
          my_moves_amsh = ["D"]
          return "D"
     
     counter_amsh += 1
     op_moves_amsh.append(opp_move)
     
     if (counter_amsh == 2):
          my_moves_amsh.append("C")
          return "C"

     if ((counter_amsh > 6) and (flag_amsh == False) and (score(my_moves_amsh, op_moves_amsh) < 60)):
          flag_amsh = True
     
     if (flag_amsh):
          return "D"

     if (opp_move == "C"):
          return "C"
     else:
          return "D"
     
    
def dn(opp_move = None):
     global counter_dn

     if (opp_move == None):
          counter_dn = 0

     counter_dn += 1
     if(counter_dn==3):
          counter_dn=0
          if (opp_move == "C"):
               return "D"
          else:
               return "C"
     return "D"
    
def pankaj(opp_move = None):
     global flag_pankaj
     global counter_pankaj

     if (opp_move == None):
          counter_pankaj = 0
          flag_pankaj = False
          return "C"

     if (counter_pankaj == 2):
          flag_pankaj = True
     
     if (flag_pankaj):
          return "D"

     if (opp_move == "C"):
          counter_pankaj = 0
          return "C"
     else:
          counter_pankaj += 1
          return "D"
   
def ash(opp_move = None):
  global flag_ash
  global counter_ash
  global op_moves

  if (opp_move == None):
    op_moves = []
    flag_ash = False
    counter_ash = -1
    return "D"
  else:
    op_moves.append(opp_move)
    if(len(op_moves) < 5):
            return "D"
    else:
      if((op_moves.count("C") > op_moves.count("D")) and (counter_ash==-1)):
        flag_ash=True
      

      if(flag_ash==True):
        #print("in True")
        counter_ash+=1
        if(counter_ash == 0):
          return "C"
        else:
          counter_ash=-1
          flag_ash=False
          return "D"
      else:
        #print("in False")
        counter_ash+=1
        if(counter_ash==1):
          counter_ash=-1
        return "D"    
def ar(opp_move = None):
     global counter_ar_init
     global counter_ar_D

     if (opp_move == None):
          counter_ar_init = 0
          counter_ar_D = 0

     counter_ar_init += 1
     if (counter_ar_init==1 or counter_ar_init ==2):
          return "D"
     if (counter_ar_init == 3):
          return "C"
     if (opp_move == "C" and counter_ar_D == 0):
          return "C"
     counter_ar_D += 1
     if (counter_ar_D == 3):
          counter_ar_D = 0
     return "D"
     
def TFT1(opponents_input = None):
     if (opponents_input == "D"):
         return "C"
     else:
         return "D"

def TFT2(opponents_input = None):
     if (opponents_input == "C"):
         return "D"
     else:
         return "C"

def allC(opponents_input = None):
     return "C"

def allD(opponents_input = None):
     return "D"

def storeOpAb(a = []):
     def closure():
         return (a)
     return closure

def storeOpAbI(a = []):
     def closure():
         return (a)
     return closure

def counterAb(i = [0]):
     def closure():
         return (i)
     return closure

def counterAbI(i = [0]):
     def closure():
         return (i)
     return closure

def Trunal(oppIn = None):
         i = counterAb()
         temp_list = i()
         lastEle = temp_list[len(temp_list)-1]
         temp_list.append((lastEle)+1)
         cnt = counterAb(temp_list)
         currCn = cnt()
         curCnt = currCn[len(currCn)-1]

         oppResponse = storeOpAb()
         if (oppIn != None):
                 tempOppResponse = oppResponse()
                 tempOppResponse.append(oppIn)
                 opResp = storeOpAb(tempOppResponse)
                 curOverallResp = opResp()
         else:
                 curOverallResp = []
         if (curCnt < 3):
                 return "D"
         else:
                 if "D" in curOverallResp[curCnt-3:curCnt]:
                         return "D"
                 else:
                         return "C"

def abhishekI(oppIn = None):
         i = counterAbI()
         tempCnt = i()
         lastEle = tempCnt[len(tempCnt)-1]
         tempCnt.append((lastEle)+1)
         cnt = counterAbI(tempCnt)
         currCn = cnt()
         curCnt = currCn[len(currCn)-1]

         oppResponse = storeOpAbI()
         if (oppIn != None):
                 tempOppResponse = oppResponse()
                 tempOppResponse.append(oppIn)
                 opResp = storeOpAbI(tempOppResponse)
                 curOverallResp = opResp()
         else:
                 curOverallResp = []
         if (curCnt < 3):
                 return "C"
         else:
                 if "C" in curOverallResp[curCnt-3:curCnt]:
                         return "C"
                 else:
                         return "D"

def random1(oppIn = None):
     return random.choice(["C", "D"])

def counter(i=[0]):
     def closure():
         return (i)
     return closure

def score_p(i=[]):
     def closure():
         return (i)
     return closure

def score_o(i=[]):
     def closure():
         return (i)
     return closure


def score(my_input=None,op_input=None):
     my_counter = 0
     op_counter = 0
     for my_inp, op_inp in zip(my_input, op_input):
         if (my_inp == "C" and op_inp =="C"):
             my_counter = my_counter + 20
             op_counter = op_counter + 20
         elif (my_inp == "C" and op_inp =="D"):
             my_counter = my_counter + 0
             op_counter = op_counter + 30
         elif (my_inp == "D" and op_inp =="C"):
             my_counter = my_counter + 30
             op_counter = op_counter + 0
         elif (my_inp == "D" and op_inp =="D"):
             my_counter = my_counter + 10
             op_counter = op_counter + 10
     return(my_counter-op_counter)



def roshan(opponent_move = None):
     cn = counter()
     cn_temp = cn()
     i = cn_temp[len(cn_temp)-1]
     cn_temp.append(i+1)
     ct = counter(cn_temp)

     if  i == 0:
             my_move = "C"
             score_p([my_move])

     elif i > 0:

             my_moves = score_p()
             op_moves = score_o()

             my_moves_list = my_moves()
             op_moves_list = op_moves()

             if (i == 1):
                 score_cal = score(my_moves_list, [opponent_move])
             else:
                 score_cal = score(my_moves_list, op_moves_list)

             if opponent_move == "C":
                 if  score_cal >0:
                     my_move = "C"
                 elif score_cal == 0:
                         my_move = "D"
                 else:
                         my_move = "D"
             else :
                     my_move = "D"

             my_moves_list.append(my_move)
             op_moves_list.append(opponent_move)
             my_m = score_p(my_moves_list)
             op_m = score_o(op_moves_list)

     return my_move


############ Main Code ############
A=[]
for i in range(1,10):
     dispatcher = {'TFT1' : TFT1, 'TFT2' : TFT2, 'allC' : allC, 'allD' : allD,'Trunal' : Trunal, 'abhishekI' : abhishekI, 'roshan' : roshan, 'random1' : random1,'amsh':amsh,'pankaj':pankaj,'ash':ash,'ar':ar,'dn':dn}
     function_list = ['TFT1', 'TFT2', 'allC', 'allD', 'Trunal', 'abhishekI','roshan', 'random1','amsh','pankaj','ash','ar','dn']

     def dispatch(name, *args, **kwargs):
          return dispatcher[name](*args, **kwargs)

     match_count = [0] * len(function_list)
     total_score = [0] * len(function_list)
     total_wins = [0] * len(function_list)
     total_tie =  [0] * len(function_list)

     match_counter = 0
     max_matches = i+1
     total_rounds = i+1
     total_matches = int((max_matches / 2) * len(function_list))
     max_matches = int(round((2 * total_matches) / len(function_list), 0))
     ind_max_match_count_reached = set()

     while(match_counter < total_matches):
              i = 0 #counter total rounds

              ind_max_match_count_reached.update([k for k in range(len(match_count)) if match_count[k] >= max_matches])

              if len(ind_max_match_count_reached) == len(function_list):
                  break

              functions_for_rand_selection = []
              functions_for_rand_selection.extend(function_list)
              if len(ind_max_match_count_reached) > 0:
                  for ind in ind_max_match_count_reached:
                      functions_for_rand_selection.remove(function_list[ind])
              flagCounter = 0
              while(True):
                   flagCounter += 1
                   randomly_selected_functions = random.choice(functions_for_rand_selection, size = (2))
                   if ((randomly_selected_functions[0] != randomly_selected_functions[1]) and not(('allD' in randomly_selected_functions) and ('abhishek' in randomly_selected_functions))):
                        break
                   elif ((match_counter > (total_matches * 0.98)) and flagCounter > 10):
                        break
                   elif (flagCounter > 10):
                        break
              if (flagCounter > 10):
                   break

              index_fun1 = function_list.index(randomly_selected_functions[0])
              index_fun2 = function_list.index(randomly_selected_functions[1])

              match_count[index_fun1] += 1
              match_count[index_fun2] += 1

              out1 = dispatch(randomly_selected_functions[0])
              out2 = dispatch(randomly_selected_functions[1])
              p1 = 0
              p2 = 0
              while(i < total_rounds):
                      if(out1 == out2 and out1 == "C"):
                              p1 = p1 + 20
                              p2 = p2 + 20
                      elif(out1 == out2 and out1 == "D"):
                              p1 = p1 + 10
                              p2 = p2 + 10
                      elif(out1 != out2 and out1 == "D"):
                              p1 = p1 + 30
                      else:
                              p2 = p2 + 30
                      out1T = dispatch(randomly_selected_functions[0], out2)
                      out2 = dispatch(randomly_selected_functions[1], out1)
                      out1 = out1T
                      i+=1

              total_score[index_fun1] += p1
              total_score[index_fun2] += p2
              if (p1 > p2):
                  total_wins[index_fun1] += 1
              elif (p2 > p1):
                  total_wins[index_fun2] += 1
              elif (p1 == p2):
                   total_tie[index_fun1] += 1
                   total_tie[index_fun2] += 1

              match_counter += 1

     avg_score = [x / y for x, y in zip(total_score, match_count)]

     print("Winner function is :", function_list[avg_score.index(max(avg_score))], "!!! and score of winner is :", round(max(avg_score), 3))

     print("\nAll scores:")
     print("Matches Played - Average Score - Total Wins - % wins - Total Tie - Function - Score")
     for a, b, c, d, e in sorted(zip(function_list, match_count, avg_score, total_wins, total_tie), key = lambda x: x[2], reverse = True):
              print(b, " - ", round(c, 2), " - ", d, " - ", (round(d/b * 100, 2)) , " - ", e, " - ", a, " - ", (3*(d) + (e) + 2*(100-b)))
     A.append(avg_score)
     print("A",A)   
#######################################
import matplotlib.pyplot as plt
for i in range(1,11):
     plt.plot(A[i])
     plt.xlabel("No.of Matches")
     plt.ylabel("Avg_score")
     plt.title("No.of matches vs Avg_score")
     plt.show()


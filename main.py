# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
makerEersteGoal = 'Ruud Gullit'
makerTweedeGoal = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = makerEersteGoal + " " + \
    str(goal_0) + ", " + makerTweedeGoal + " " + str(goal_1)

print(scorers)

report = f"{makerEersteGoal} scored in the {goal_0}nd minute" '\n' f"{makerTweedeGoal} scored in the {goal_1}th minute"
print(report)

player = "Ronald Koeman"
splitter = player.find(" ")
first_name = player[:splitter]
last_name_len = len(player[splitter + 1:])
name_short = player[0] + "." + player[splitter:]
chant = f"{first_name}! " * int(len(first_name)-1) + f"{first_name}!"
good_chant = chant[-1] != " "

print(player)
print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)

def mark_starting_point_and_move():
    put("token")
    while not front_is_clear():
        turn_left()
    move()



def follow_right_wall():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()



#  Program execution below

while not at_goal():
    follow_right_wall()




# attempting to convert code below to Javascript
num_test_cases = int(input())

for i in range(num_test_cases):
    test_string = input()
    even_indexed_characters = ''
    odd_indexed_characters = ''
    for j in range(len(test_string)):
        if j % 2 == 0:
            even_indexed_characters += test_string[j]
        else:
            odd_indexed_characters += test_string[j]

    print('{} {}'.format(even_indexed_characters, odd_indexed_characters))
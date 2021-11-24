print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  ------|
 \_/__________________________________________________________________/
''')

print('Welcome to the city of Atlanta!')
print('Your mission is to find the treasure hidden somewhere in the city!')

print('You\'re at Centennial Olympic Park')
direction = input('Which direction do you want to go? Type \'north\', \'south\', \'west\', or \'east\'? ')
if direction == 'north':
    print('You\'re in Midtown Atlanta')
    print('You\'ve arrived at three different buildings: the Fox Theater, Georgia Tech, and the North Avenue Marta Station')
    building = input('Please select a building (Fox Theater, Georgia Tech, or North Avenue Marta Station): ')
    if building == 'Fox Theater':
        print('You were eaten by a dragon. Game Over!')
    elif building == 'Georgia Tech':
        print('You were arrested by a security guard for trespassing on school grounds. Game Over!')
    elif building == 'North Avenue MARTA Station' or building == 'MARTA Station' or building == 'Marta Station':
        print('You\'re inside the MARTA train station. A train is on the way to take you to Buckhead.')
        action = input('Type \'walk\' to walk to Buckhead on the tracks. Otherwise, type \'wait\' to wait on the train. ')
        if action == 'walk':
            print('You were electrocuted by the rail. Game Over!')
        elif action == 'wait':
            print('You\'ve arrived in Buckhead unharmed.')
            print('You\'re on Peachtree Road in front of two shopping centers: Lenox Square Mall and Phipps Plaza')
            shopping_center = input('Which shopping center do you want to go to, Lenox Square Mall or Phipps Plaza? ')
            if shopping_center == 'Lenox Square Mall' or shopping_center == 'Lenox Square' or shopping_center == 'Lenox':
                print('You have a choice between three different stores: Apple, Macy\'s, or Foot Locker.')
                store = input('Please choose any of the three stores above: ')
                if store == 'Macy\'s':
                    print('You found the treasure! You Win!')
                elif store == 'Apple':
                    print('You got attacked by an angry customer. Game Over!')
                elif store == 'Foot Locker':
                    print('You entered a room full of beasts. Game Over!')
                else:
                    print('You chose a store that doesn\'t exist. Game Over!')
            elif shopping_center == 'Phipps Plaza' or shopping_center == 'Phipps':
                print('You were rampaged by angry teens. Game Over!')
            else:
                print('You chose a shopping center that doesn\'t exist. Game Over!')
        else:
            print('Invalid option! Game Over!')
    else:
        print('You chose a building that doesn\'t exist. Game Over!')
elif direction == 'south':
    print('You were robbed by a gang of thieves. Game Over!')
elif direction == 'west':
    print('You fell into a hole. Game Over!')
elif direction == 'east':
    print('You were attacked by an angry wolf. Game Over!')
else:
    print('You entered a direction that doesn\'t exist. Game Over!')
import sys
import pip
from time import sleep
from random import randint, shuffle

big_exit_msg = """"It's called CSA Big Finder, not CSA Little Finder. If you don't remember who your little is,
you might have more serious issues at hand. Anyways, go troll your little(s) or something."""

heads_picked_taunt = ["Ooof tails? Unlucky. ¯\_(:o)_/¯", "Shouldn't have picked heads... ¯\_(0^0)_/¯",
                      "You're really good at picking the wrong outcome, huh? :P", "Maybe next time? ¯\_('V ')-",
                      "How unlucky can you be? (>_<)",
                      "Imagine losing to a silly program made by a bad cs student (._.)"]

tails_picked_taunt = ["Told you not to pick tails XD", "Shoulda gone with heads OwO",
                      "I didn't know someone could be this bad at guessing (*o* )",
                      "Losing? Wouldn't be me... @<@", "I think my cat could do better than you (.O_0.)",
                      "You better hope Heads or Tails isn't in your Squid Game... (´;_;`)"]

shuffle(tails_picked_taunt)
shuffle(heads_picked_taunt)

inflammatory = "Don't go to Vegas - you'll lose all your money if you're this bad. (U._ U)"
inflammatory_two = "You still haven't won yet? Maybe you should give up...  X.X"
tails_picked_taunt.insert(randint(1, 4), inflammatory)
heads_picked_taunt.insert(randint(1, 4), inflammatory_two)

coin_anims = "-\|/\\"


def sl_print(msg):
    sleep(1.5)
    print('\n' + msg)


def install(package):
    pip.main(['install', package])


def print_intro():
    termcolor.cprint(pyfiglet.figlet_format('CSA BIG FINDER!', font='univers'), 'yellow', attrs=['bold'])


def flip_coin(style):
    def red(anim):
        return termcolor.colored(anim, 'red')

    def blue(anim):
        return termcolor.colored(anim, 'blue')

    def green(anim):
        return termcolor.colored(anim, 'green')

    opposite = {"Heads": blue("It's Tails!"), "Tails": red("It's Heads!")}
    rigged = {"Tails": red('-'), "Heads": blue('-')}

    initial_coins = [
        {
            'type': 'list',
            'message': 'Heads or Tails?',
            'name': 'flip',
            'choices': [
                {
                    'name': 'Heads'
                },
                {
                    'name': 'Tails'
                }
            ],
        }
    ]
    anims = [red(char) for char in coin_anims] + [blue(char) for char in coin_anims]
    for i in range(6):
        print("Number of Tries Left: ", green(str(7 - i)), flush=True)
        print('\n')
        coin_guess = prompt(initial_coins, style=style)
        guess = coin_guess['flip']
        m_spins = randint(2, 5)
        spaces = []
        for x in range(m_spins):
            for frame in anims:
                sleep(.1)
                if spaces and randint(0, 3) > 2:
                    spaces.pop()
                elif randint(0, 1) == 1:
                    spaces.append(" ")
                if spaces:
                    spacing = "".join(spaces)
                    print(spacing, end='')
                print(frame, flush=True)
                if x == m_spins - 1 and rigged[guess] == frame:
                    print("\n" + opposite[guess])
                    if guess == "Heads":
                        taunt = heads_picked_taunt.pop(0)
                    else:
                        taunt = tails_picked_taunt.pop(0)
                    sl_print(taunt)
                    break
        print()
    sl_print("PFFFFFFFFFFFFFT")
    sl_print("6 LOSSES IN A ROW??? \t You must be the worst guesser in the world!")
    response = [
        {
            'type': 'list',
            'message': 'Your Reply?',
            'name': 'rigged_response',
            'choices': [
                {
                    'name': 'THIS IS RIGGED. LEMME SEE THE COIN'
                },
                {
                    'name': "I've got one more try."
                }
            ],
        }
    ]
    print('\n')
    response = prompt(response, style=style)['rigged_response']
    if response == 'THIS IS RIGGED. LEMME SEE THE COIN':
        sl_print("Heh, you mean this thing?  ")
        print(red('-' + '\n'), end='')
        sleep(3)
        sl_print("I can assure you that the coin is guaranteed to be potentially fair!")
        sleep(3)
        print(" And it's all virtual anyways... Good luck trying to prove that I'm CHEATING lol")
        sleep(3)
    else:
        sl_print("Well, considering the way the last 6 guesses have gone, I'm gonna take a wiiiiild guess and" +
                 " say that you're not winning this one either, bucko")
        sleep(3)

    last = [
        {
            'type': 'list',
            'message': 'Heads or Tails?',
            'name': 'last',
            'choices': [
                {
                    'name': 'Sideways.'
                },
                {
                    'name': 'Sideways?'
                },
                {
                    'name': 'SIDEWAYS?!?!?!?!?!?!?!'
                }
            ],
        }
    ]
    print('\n')
    print("Number of Tries Left: ", red("1"), flush=True)
    last_coin = prompt(last, style=style)['last']

    sl_print("HAHAHAHAHAHAHA *wheeze*")
    sleep(3)
    sl_print("Today just isn't you're day, is it? Why'd you pick sideways, anyways? Looks like someone's finally"
             " lost it...")
    sleep(3)
    sl_print("Anyways, let's just end it here. <3")
    sleep(3)
    m_spins = randint(4, 8)
    spaces = []
    for x in range(m_spins):
        for frame in anims:
            sleep(.1)
            if spaces and randint(0, 3) > 2:
                spaces.pop()
            elif randint(0, 1) == 1:
                spaces.append(" ")
            if spaces:
                spacing = "".join(spaces)
                print(spacing, end='')
            print(frame, flush=True)
            if x == m_spins - 1 and (frame == red('|') or frame == blue('|')):
                sl_print("....")
                sleep(2)
                sl_print("It's... sideways?")
                sleep(1)
                sl_print("well look at that. Guess I underestimated you after all. " +
                         " Or maybe you're the one that cheated.")
                sleep(1)
                sl_print("You won, so I guess I have to tell you who your big is.")
                msg = green(" SOMEONE IN CSA!!!!!!!!!!!")
                sleep(2)
                print("your big is: (drumroll please)", end='')
                sleep(4)
                print(msg)
                sl_print("Good for you! Now say hi to your big for me! You can thank me later :)")
                exit()
    exit()


def main():
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })

    questions = [
        {
            'type': 'list',
            'message': 'Are you a Big or a Little?',
            'name': 'position',
            'choices': [
                {
                    'name': 'Big'
                },
                {
                    'name': 'Little'
                }
            ],
        }
    ]

    print_intro()
    print('\n')
    intro_answers = prompt(questions, style=style)
    if intro_answers['position'] == 'Big':
        sl_print("Uh...")
        sl_print("I think you might might have the wrong program...")
        sl_print(big_exit_msg)
        exit()
    sl_print("Welcome!")
    sl_print("So you want to find who your big is, huh?")
    sleep(2)
    sl_print("WELL IT WON'T BE THAT EASY!!!")
    sleep(2)
    sl_print("You just have to be me in a reeeeaaaaal easy game - coin toss!")
    sl_print("Here's a magical coin -> it's " + termcolor.colored("RED", 'red') + " when it's heads" +
             " and " + termcolor.colored("BLUE", 'blue') + " when it's tails")
    sleep(4)
    sl_print("all you have to do is guess it correctly ONE out of SEVEN times? Easy, right?")
    sleep(4)
    sl_print("heh-heh - let's get rolling! (or is it flipping?)")
    flip_coin(style)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        import termcolor
    except:
        install('termcolor')
        import termcolor
    try:
        import colorama
    except:
        install('colorama')
        import colorama
    try:
        import pyfiglet
    except:
        install('pyfiglet')
        import pyfiglet
    try:
        from PyInquirer import style_from_dict, Token, prompt, Separator
    except:
        install('PyInquirer')
        from PyInquirer import style_from_dict, Token, prompt, Separator
    colorama.init(strip=not sys.stdout.isatty())
    try:
        from pprint import pprint
    except:
        install('pprint')
        from pprint import pprint
    main()

'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).

W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy:

- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop".

Podpowiedź: Użyj wzorca Command (polecenie).

W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.

Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd, sys
import turtle


class TurtleCommand(object):
    def __init__(self, arg):
        self.arg = arg

    def run(self):
        pass


class SingleTurtleCommand(TurtleCommand):
    def __init__(self, command, arg):
        super(SingleTurtleCommand, self).__init__(arg)
        self.command = command

    def run(self):
        self.command(int(self.arg))


class HomeCommand(TurtleCommand):
    def run(self):
        turtle.home()


class PositionCommand(TurtleCommand):
    def run(self):
        print('Current position is %d %d\n' % turtle.position())


class HeadingCommand(TurtleCommand):
    def run(self):
        print('Current heading is %d\n' % (turtle.heading(),))


class ResetCommand(TurtleCommand):
    def run(self):
        turtle.reset()


class ByeCommand(TurtleCommand):
    def run(self):
        print('Thank you for using Turtle')
        turtle.bye()


class MacroCommand(TurtleCommand):
    def run(self):
        for command in self.arg:
            command.run()


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    _is_recording = False

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        self._run(SingleTurtleCommand(turtle.forward, arg))

    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        self._run(SingleTurtleCommand(turtle.right, arg))

    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        self._run(SingleTurtleCommand(turtle.left, arg))

    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        self._run(HomeCommand(arg))

    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        self._run(SingleTurtleCommand(turtle.circle, arg))

    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        self._run(PositionCommand(arg))

    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        self._run(HeadingCommand(arg))

    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        self._run(ResetCommand(arg))

    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        self._run(ByeCommand(arg))
        return True

    def do_record(self, arg):
        self._commands = []
        self._is_recording = True

    def do_stop(self, arg):
        self._is_recording = False
        self._macro = MacroCommand(self._commands)

    def do_playback(self, arg):
        self._run(self._macro)

    def _run(self, command):
        if self._is_recording:
            self._commands.append(command)
        else:
            command.run()

if __name__ == '__main__':
    TurtleShell().cmdloop()

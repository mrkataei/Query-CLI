from CLI.cli import welcome, commands

if __name__ == '__main__':
    wel = welcome()
    if wel:
        print('some error occur , system can not create table')
    else:
        print('enter command! or ?\n'
              'enter exit to terminate')
        commands()


import cmd
class fileCmd(cmd.Cmd):
    #OK P
    intro='''Please Enter send [filepath] To Send A File,
    Then you will get A KEY TO get the file on another computer.
    And ENTER get [key&path] To Get A File Which The key Means.'''
    
    #OK P
    def do_help(self, arg):
        return print(self.intro)
        
    def do_send(self,arg):
        print(send(arg))

    def do_get(self,arg):
        get(arg)
        print('OK')

if __name__=='__main__':
    C=fileCmd().cmdloop()

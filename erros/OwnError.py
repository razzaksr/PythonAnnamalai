class AnnamalaiError(RuntimeError):
    def __int__(self,msg=""):
        self.args=msg
    def __str__(self):
        return "MismatchError"
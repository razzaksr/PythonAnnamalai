class InvalidProofError(RuntimeError):
    def __init__(self):
        super().__init__()
        self.msg="InvalidProofAttached"
    def __str__(self):
        return self.msg
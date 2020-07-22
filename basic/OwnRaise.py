class TheatreError(RuntimeError):
    def __init__(self):
        super().__init__()
        self.msg="TicketNotAllowedError"
    def __str__(self):
        return str(self.msg)
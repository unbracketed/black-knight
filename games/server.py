from itty import run_itty, get as GET


@GET('/')
def index(request):
    pass

@GET('/game/tic-tac-toe')
def tictactoe_new(request):
    pass
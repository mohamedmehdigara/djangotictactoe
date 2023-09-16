from django.shortcuts import render, redirect
from .models import TicTacToeGame

def index(request):
    game = TicTacToeGame.objects.first()  # Assuming there's only one game
    context = {
        'board': game.board,
        'next_player': game.next_player,
    }
    return render(request, 'game/index.html', context)

def make_move(request, position):
    game = TicTacToeGame.objects.first()
    board_list = list(game.board)

    if board_list[position] == ' ':
        board_list[position] = game.next_player
        game.board = ''.join(board_list)
        game.next_player = 'X' if game.next_player == 'O' else 'O'
        game.save()

    return redirect('game:index')

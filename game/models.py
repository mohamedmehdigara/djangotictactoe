
# Create your models here.

from django.db import models

class TicTacToeGame(models.Model):
    board = models.CharField(max_length=9)  # Represent the board as a string, e.g., "XOXOXOXOX"
    next_player = models.CharField(max_length=1, default='X')  # 'X' or 'O' indicating the next player

    def __str__(self):
        return self.board

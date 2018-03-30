#!/usr/bin/python3

import Const
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import chess.uci
import chess.polyglot
import chess.syzygy
import FeaturesExtraction as fe


class Eval:

    def __init__(self, modelfile=Const.MODELFILE+".hdf5", openingbookfile=None, tablebases=None):
        self.model = load_model(modelfile)
        print("Model "+modelfile+" loaded")
        #if openingbook != None: self.openingbook = chess.polyglot.open_reader(openingbookfile)

    def EvaluatePositionB(self, board):
        sign = 1
        # evaluations are always done on white side
        if board.turn == chess.BLACK:
            board = board.mirror()
            sign = -1
        # evaluate position
        X = np.array([fe.extract_features(board)])
        Y = self.model.predict(X, batch_size=1, verbose=0)
        return sign * Y[0]

    def EvaluatePosition(self, fenstring):
        epdposition = fenstring
        board = chess.Board()
        board.set_epd(epdposition)
        return self.EvaluatePositionB(board)

    #def PredefinedMoves(self, board)
        # look into opening book if required
        #if openingbook:
        #    bookentry = book.find(board)
        #    if bookentry.move():
        #        return bookentry.move()
        #    else:
        #        if openingbook: openingbook.close()
        #        openingbook = False
        #---
        # if pieces <= 5 or 6 -> look endgame tanlebases
        #tablebases = chess.syzygy.open_tablebases(Const.TABLEBASES)
        #tablebases. ...
        #tablebases.close()
    

import random

class Player():
    def countMatches (self,board):
        """
        Count matches on the board
        """

        nbAll =0
        for ligne in board:
            if ligne >= 0:
                nbAll+=ligne
        return nbAll


    def isValidStrategy (self,line, nbMatches, board):
        """
        test if a strategy is valid for a board
        """
        if (line < 0 or line >=4):
            return False

        if nbMatches < 1 or nbMatches >3 :
            return False

        if board[line]-nbMatches < 0:
            return False

        return True

    def getValidNextStrategies (self,board):
        """
        get an array of all possible strategy for a board
        Each Strategy is a tuple containing (numLine, nbMatches)
        """

        strategies = []
        for nbMatches in [1,2,3]:
            for line in [0,1,2,3]:
                if board[line] - nbMatches >= 0 :
                    strategies.append((line, nbMatches))

        return strategies


class HumanPlayer(Player):

    def makeChoice(self,board):
        print ("entrez un num de ligne")
        line = int(input())
        print ("entrez un nb d'allumettes'")
        nbMatches = int(input())

        ok = False
        if self.isValidStrategy(line, nbMatches, board):
            ok=True
        while not ok:
            print ("Erreur ")
            print ("player make a choice")
            print ("entrez un num de ligne")
            line = int(input())
            print ("entrez un nb d'allumettes'")
            nbMatches = int(input())
            if self.isValidStrategy(line, nbMatches, board):
                ok=True

        return line, nbMatches

class IAMinMaxPlayer(Player):

    def makeChoice(self,board):

        ## Il reste des allumette
        choices = self.getValidNextStrategies (board)

        maxResu = -2
        bestChoice = (0,0)

        known = {}
        for c in choices:
            line, nbMatches = c
            nboard = board.copy()
            nboard[line]-=nbMatches
            resu = self.evaluate(nboard, False,0,known)


            if resu > maxResu:
                maxResu = resu
                bestChoice=c

            '''
            if IA and resu == 1:
                return 1
            if not IA and resu == -1:
                return -1
            '''
        '''
        if maxResu == 1:
            print ("je vais te piler")
        else :
            print ("Si tu joues bien, tu peux gagner")
        '''

        return bestChoice

    def computeKey(self,tab):
        triee = sorted(tab, reverse=True)
        clef=0
        N = len(tab)
        for i in range(N):
            clef+= triee[i]*10**(N-i-1)

        return clef


    def evaluate(self,board, IA,level,known,prune=True):
        #print ("\t"*level,"evaluation de ", board)
        #print ("\t"*level,"kown avant", known)
        clef = self.computeKey(board)

        if clef in known:
            oldResu=known[clef]
            if IA:
                return oldResu
            else :
                return -oldResu

        if self.countMatches(board) == 0:
            known[clef]= 1
            #print ("\t"*level,"kown feuille", known)
            if IA :
                return 1
            return -1

        ## Il reste des allumette
        choices = self.getValidNextStrategies (board)
        #print(choices)
        results =[]
        for c in choices:
            line, nbMatches = c
            #print ("\t"*level,"je teste ",line, nbMatches)
            nboard = board.copy()
            nboard[line]-=nbMatches
            resu = self.evaluate(nboard, not IA,level+1,known,prune=prune)

            if prune:
                if IA and (resu == 1):
                    known[clef]=1
                    #print ("\t"*level,"known 1", known)
                    return 1
                if (not IA) and (resu == -1):
                    #print ("\t"*level,"known 2", known)
                    return -1

            #print ("\t"*level,"resu pour", nboard," :" , resu)
            results.append(resu)

        #print ("\t"*level,"known apres", known)
        if IA :
            final= max(results)
            known[clef]=max(results)
        else :
            final = min(results)
            known[clef]=-min(results)


        return final

class IARandomPlayer(Player):
        def makeChoice(self,board):

            ## Il reste des allumette
            choices = self.getValidNextStrategies (board)
            return random.choice(choices)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import os
import mymodel

class IADeepPlayer(Player):
    def __init__(self):
        checkpoint_path = "training_1/cp.ckpt"
        self.model = mymodel.build_model()
        self.model.load_weights(checkpoint_path)
        self.epsilon=0.2

    def makeChoice(self,board,train=False):

        ## Il reste des allumette
        choices = self.getValidNextStrategies (board)

        maxResu = -2
        bestChoice = (0,0)

        for c in choices:
            line, nbMatches = c
            nboard = board.copy()
            nboard[line]-=nbMatches
            npboard=np.asarray([sorted(nboard, reverse=True)])
            resu = self.model.predict(npboard)

            resu = -resu[0][0]

            if resu > maxResu:
                maxResu = resu
                bestChoice=c

            '''
            if IA and resu == 1:
                return 1
            if not IA and resu == -1:
                return -1
            '''
        '''
        if maxResu == 1:
            print ("je vais te piler")
        else :
            print ("Si tu joues bien, tu peux gagner")
        '''
        # En exploitation, on joue le meilleur coups possible
        # en entrainement, on joue au hasard avec une probabilité de epsilon
        # et on joue le meilleur coup avec une probabilité de 1-epsilon
        if not train :
            return bestChoice
        else :
            if random.random()<self.epsilon:
                return random.choice(choices)
            else :
                return bestChoice

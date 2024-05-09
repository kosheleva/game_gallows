"""
Entry file - main.py
Configuration settings, board initialization and run.
"""

from game.board import Board
from game.gui import GUI
from game.alphabet import Alphabet
from game.word import Word
from game.gallows import Gallows

lightColor = "#99CCFF"
darkColor = "#336699"

GUICongig = {
    "board": {
        "width": 900,
        "height": 450,
        "title": "Welcome to Gallows Game!",
        "opacity": 1,
        "bgColorLight": lightColor,
        "bgColorDark": darkColor
    },
    "menuFrame": {
        "width": 78, 
        "height": 400,
        "bgColor": lightColor, 
        "side": "left", 
        "padx": 10, 
        "pady": 10,
        "rulesIconCode": 10064,
        "lightModeIconCode": 9728,
        "darkModeIconCode": 9790,
        "refreshIconCode": 10558,
        "closeIconCode": 10060
    },
    "gallowsFrame": {
        "width": 250, 
        "height": 330,
        "bgColor": lightColor, 
        "outlineColor": "#000000",
        "fillColor": "#CCCCCC",
        "color": "#000000",
        "side": "left", 
        "padx": 10, 
        "pady": 25
    },
    "wordFrame": {
        "width": 250, 
        "height": 400,
        "bgColor": lightColor, 
        "side": "left", 
        "padx": 10, 
        "pady": 35
    },
    "alphabetFrame": {
        "width": 250, 
        "height": 250,
        "bgColor": lightColor, 
        "side": "left", 
        "padx": 10, 
        "pady": 35
    },
    "button": {
        "size": 25,  
        "contentPadx": 2,
        "contentPady": 2, 
        "padx": 10, 
        "pady": 15, 
        "width": 2, 
        "height": 1,
        "highlightbackground": lightColor,
        "side": "top"
    },
    "letterBtn": {
        "size": 18,  
        "contentPadx": 2,
        "contentPady": 2, 
        "padx": 2, 
        "pady": 2, 
        "width": 2, 
        "height": 1,
        "side": "left",
        "highlightbackground": lightColor
    },
    "label": {
        "side": "left",
        "padx": 5,
        "pady": 3,
        "bgColor": "#FFFFFF",
        "highlightbackground": lightColor
    }
}

board = Board(GUI, Alphabet, Word, Gallows, GUICongig)
board.run()
#!/usr/bin/python


#def rps_game_winner(game):
	#raise WrongNumberOfPlayersError unless game.length == 2
	# your code here


game=[\
[\
[ ["Armando", "P"], ["Dave", "S"] ],\
[ ["Richard", "R"], ["Michael", "S"] ],\
],\
[\
[ ["Allen", "S"], ["Omer", "P"] ],\
[ ["David E.", "R"], ["Richard X.", "P"] ]\
]\
]		
def main():
	print(game)
	match([ ["David E.", "R"], ["Richard X.", "P"] ])
def match((p0,p1)):
	print(p0)
	print(p1)
main()
"""
1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

"""


def function_1(function_2):
	print("Hello World!")
	function_2()


def function_2():
	print("Mi primera funcion")


function_1(function_2)
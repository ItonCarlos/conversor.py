# -*- coding: utf-8 -*-

"""
Criado em quinta-feira, 20 de abril 00:16:23 2023
@autor: iton C. Sangaletti
"""

segundos_str = input('Por favor, entre com o número de segundos que deseja converter:')
total_segundos = int(segundos_str) 
dias = total_segundos // 86400 
dias_restante = total_segundos % 86400
horas = dias_restante // 3600
horas_rest = dias_restante % 3600
minutos = horas_rest // 60
minutos_rest = horas_rest % 60
segundos = minutos_rest // 1


print (dias,'dias,',horas ,'horas,',minutos,'minutos e',segundos,'segundos.')

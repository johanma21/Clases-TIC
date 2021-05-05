print ()
print ("EJERCICIO 1")
print ()
#Número 5
print (2 + 2 + 2 - (2/2) )
#Número 6
print (2+2+2+2-2)
#Número 7
print ((2*2)+2+(2/2))
#Número 8
print ((2*(2*2))-2+2)
#Número 9 
print ((((2*2)**2)+2)/2)
#Número 10 
print ((((2*2)**2)/2)+2) 
print()
print("EJERCICIO 2")
print()
valor_celular = 420
valor_de_iva_dia = 0.2 
print ("valor de celular en euros mas IVA =",valor_celular * valor_de_iva_dia + valor_celular )
print()
print("EJERCICIO 3")
print () 
#ENTRADA
vueltas_por_minuto_fitget_spinner = 147
tiempo_en_segundos_de_fitget_spinner_en_movimiento = 640
segundos_por_minuto = 60 
#PROCESO
vueltas_por_segundo_fitget_spinner = vueltas_por_minuto_fitget_spinner / segundos_por_minuto 
#SALIDA 
print ("vueltas fitget spinner por tiempo en movimiento = ", (vueltas_por_segundo_fitget_spinner * tiempo_en_segundos_de_fitget_spinner_en_movimiento))
print()
print ("EJERCICIO 4")
print()
#ENTRADA
cajas_de_refresco = 9
latas_por_cada_caja = 24
personas_invitadas_al_evento = 56
#PROCESO
total_de_latas_disponibles_para_evento = cajas_de_refresco * latas_por_cada_caja
latas_de_refresco_que_sobran = (cajas_de_refresco * latas_por_cada_caja ) % personas_invitadas_al_evento
latas_que_corresponden_por_persona = total_de_latas_disponibles_para_evento // personas_invitadas_al_evento
#SALIDA 
print ("latas de refresco que sobran=", latas_de_refresco_que_sobran )
print ("latas que coreesponden por persona = ", latas_que_corresponden_por_persona)
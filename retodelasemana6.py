#le damos la bienvenida al usuario
print("Bienvenido, esta usted accediendo al programa de validacion de contraseñas.")
print()

#creamos un ciclo para que maximo 3 intentos el usuario pueda ingresar su contraseña
contador = 0
while contador <= 3:
   
   contraseña = input("Ingrese una contraseña que contenga un número al principio: ")
   if contraseña == "":
      print("intento " + str(contador+1)+" Error, no ingreso ninguna contraseña")
      contador+=1
      if contador==3:
         print("Alcanzo el maximo de intentos permitidos, fin del programa")
         break
      continue  
   elif contraseña:
      num = False
      
      for carac in contraseña[0]:#utilizamos un for para validar el indice 0
         if carac.isdigit() == True:#utilizamos el metodo isdigit para validar que sea un numero
            num = True
            print("Contraseña valida")
            contador = 4
            valido = True

         

      if not num:
         print("intento " + str(contador+1)+ " La contraseña debe de tener un número al principio")   
         contador = contador + 1
         valido=False
      if contador==3:
         print("Haz alcanzado el número maximo de intentos, fin del programa.")
         break     
   
   
   if valido == True: #si la contraseña es correcta manda true a la variable valido y entra en este if
      cont = 0
      while cont <=3:
         contraseña2 = input("Ingrese nuevamente su contraseña: ")
            
         if contraseña == contraseña2:
            print("Bienvenido contraseña ingresada correctamente")
            break
         
         elif contraseña != contraseña2:
            print("intento " + str(cont+1)+ " Las contraseñas no coinciden")
            cont = cont+1
                  

         elif carac.isalpha()== False:
            print("intento " + str(cont+1)+" No debe ingresar otro caracter que no sea un número")
            cont = cont + 1
               
         if cont == 3:
            print("Haz ingresado la contraseña el número máximo de intentos permitidos") 
            break 
   
      
   
      

import pyttsx3 
import webbrowser
import speech_recognition as sr

corona = "https://www.mayoclinic.org/es-es/diseases-conditions/coronavirus/symptoms-causes/syc-20479963"
gripe = "https://www.mayoclinic.org/es-es/diseases-conditions/flu/symptoms-causes/syc-20351719"
resfriado = "https://www.mayoclinic.org/es-es/diseases-conditions/common-cold/symptoms-causes/syc-20351605"
alergia = "https://www.mayoclinic.org/es-es/diseases-conditions/allergies/symptoms-causes/syc-20351497#:~:text=Las%20alergias%20aparecen%20cuando%20el,sustancias%20conocidas%20como%20%C2%ABanticuerpos%C2%BB."

escuchar = sr.Recognizer()
guma = pyttsx3.init()


def grabar():
    with sr.Microphone() as source:
        print("Estoy escuchando")
        audio = escuchar.listen(source)
        voice_data = escuchar.recognize_google(audio, language='es-ES')
        return voice_data
        

def responder( voice_data ):
    if "nombre" in voice_data:   
         
        guma.say("Me llamo Guma. Seré tu asistente de Servicios Médicos")
        guma.runAndWait()

    if "navegar" in voice_data:
        guma.say("¿Qué desea buscar?")
        guma.runAndWait()
        busqueda = grabar()
        url = "https://google.com.ar/search?q="+ busqueda
        webbrowser.open_new( url )
        print("Esto es lo que encontre: " + busqueda)
    

    if "mapa" in voice_data:
        guma.say("¿Donde quiere ir?")
        guma.runAndWait()
        busqueda = grabar()
        url = 'https://google.com.ar/maps/place/' + busqueda + "/&amp"
        webbrowser.get().open(url)
        print("Esto es lo que encontre: " + busqueda)





    if "salir" in voice_data:
        guma.say("Nos vemos, y no olvides seguir las normas")
        guma.runAndWait()
        exit()

hospital = "XXXX"
print ("Bienvenido al Sistema de Predicción de Enfermedades Argentino. Usted será sometido a una serie de preguntas para poder agilizar la creación de un Informe Clínico")
print ("Seleccione un número para responder")

indicacion = input ("¿A que hospital se dirigirá? 1. Hospital Italiano, 2. Hospital Santojanni, 3. Hospital Garrahan: ")
if (int(indicacion) == 1): 
     hospital = ("Hospital Italiano") 
elif (int(indicacion) == 2):
      hospital = ("Hospital Santojanni") 
elif (int(indicacion) == 3):
     hospital = ("Hospital Garrahan")
else:
     hospital = ("Desconocido") 
     print ("Hospital no encontrado en la base de datos. ERROR") 

nombrePaciente = input ("Para comenzar, ingrese su nombre completo: ") 
fechaDeNacimiento = input ("Ingrese su fecha de nacimiento: ")
edadPaciente = input ("Ingrese su edad actual: ") 
nacionalidadPaciente = input ("Ingrese su nacionalidad: ") 
dniPaciente = input ("Ingrese su DNI: ")
telefonoPaciente = input ("Ingrese su número telefónico: ")
motivoIngreso = input ("En breves palabras, explique el motivo de su ingreso: ")

print ("Las siguientes preguntas están relacionadas con sus antecedentes personales. Responda con `sí´ o `no`") 
hipertensionArterial = input ("¿ha usted padecido Hipertensión arterial?: ")
tabaquismo = input ("¿ha usted experimentado tabaquismo?: ") 
asma = input ("¿ha usted padecido asma?: ")
oncologicos = input ("¿ha sido usted un paciente oncológico/padeció tumores?: ") 
diabetes = input ("¿Tiene usted diabetes?: ") 
ACV = input ("¿ha usted padecido un ACV?: ")
EPOC = input ("¿ha usted padecido EPOC?: ")
obesidad = input ("¿ha usted padecido obesidad?: ")
tuberculosis = input ("¿ha usted padecido tuberculosis?: ")
EnfermedadesCoronarias = input  ("¿ha usted padecido alguna enfermedad coronaria?: ")
HIV = input ("¿ha usted padecido HIV?: ")
sedentarismo = input ("¿ha usted padecido sedentarismo?: ")

def posibleEnfermedad ():
     print ("Ahora nos centraremos más específicamente en sus síntomas actuales. Responda con `si` o `no`")
     fiebreprob = input ("¿Tiene usted fiebre?: ")
     if (fiebreprob == "si"): 
         airelackek = input ("¿experimenta falta de aire?: ") 
         if (airelackek == "si"):
             print ("Usted podría tener coronavirus")
             print ("Otros síntomas podrían ser tales como tos, fatiga, debilidad")
             print ("Estos son síntomas comunes, que pueden variar de persona en persona. Solo un doctor puede diagnosticarlo oficialmente.")
             print ("Dirijase a la pagina que se abrirá a continuación, infórmese y tome las precauciones necesarias.")
             webbrowser.get().open(corona)
         elif (airelackek == "no"):
             print ("Usted podría tener gripe")
             print ("Otros síntomas podría ser tales como tos, fatiga, debilidad")
             print ("Estos son síntomas comunes, que pueden variar de persona en persona. Solo un doctor puede diagnosticarlo oficialmente.")
             print ("Dirijase a la pagina que se abrirá a continuación, infórmese y tome las precauciones necesarias.")
             webbrowser.get().open(gripe)
         else:
             print ("Usted a introducido un dato incorrecto. Responda con `si´ o `no´, sin mayúsculas ni acentos o puntos.")
             posibleEnfermedad() 
     elif (fiebreprob == "no"):
         ojosirritados = input ("¿Tiene usted los ojos irritados?") 
         if (ojosirritados == "si"):
             print ("Podría tener alergia")
             print ("Otros síntomas podrían ser tales como estornudos, goteo nasal")
             print ("Estos son síntomas comunes, que pueden variar de persona en persona. Solo un doctor puede diagnosticarlo oficialmente.")
             print ("Dirijase a la pagina que se abrirá a continuación, infórmese y tome las precauciones necesarias.")
             webbrowser.get().open(alergia) 
         elif (ojosirritados == "no"):
             print ("Usted podría tener un resfriado común")
             print ("Otros síntomas podrían ser tales como estornudos, goteo nasal, leve molestia en el pecho")
             print ("Estos son síntomas comunes, que pueden variar de persona en persona. Solo un doctor puede diagnosticarlo oficialmente.")
             print ("Dirijase a la pagina que se abrirá a continuación, infórmese y tome las precauciones necesarias.")
             webbrowser.get().open(resfriado)
         else: 
             print ("Usted a introducido un dato incorrecto. Responda con `si´ o `no´, sin mayúsculas ni acentos o puntos.")
             posibleEnfermedad() 
     else: 
         print ("Usted a introducido un dato incorrecto. Responda con `si´ o `no´, sin mayúsculas ni acentos o puntos.")
         posibleEnfermedad() 

posibleEnfermedad() 

nada = input ("Presione `enter´ para mostrar el reporte para su médico.") 

print ("Informe médico del  paciente" + " " + nombrePaciente + " " + "para el hospital: " + hospital) 
print ("Fecha de nacimiento: " + str(fechaDeNacimiento))
print ("Edad: " + edadPaciente)
print ("Nacionalidad: " + nacionalidadPaciente) 
print ("DNI: " + str(dniPaciente)) 
print ("Teléfono: " + str(telefonoPaciente)) 
print ("Motivo de ingreso: " + motivoIngreso) 
print ("Historial Clínico del paciente: ") 
print ("Hipertensión Arterial: " + hipertensionArterial)
print ("Tabaquismo: " + tabaquismo) 
print ("Asma: " + asma) 
print ("Oncológicos: " + oncologicos)
print ("Diabetes: " + diabetes)
print ("ACV: " + ACV)
print ("EPOC: " + EPOC)
print ("Obesidad: " + obesidad)
print ("Tuberculosis: " + tuberculosis)
print ("Enfermedades Coronarias: " + EnfermedadesCoronarias)
print ("HIV: " + HIV)
print ("Sedentarismo: " + sedentarismo) 

guma.say("¿En que puedo ayudarte? soy Guma, tu asistente médica")
guma.runAndWait()

grabacion = grabar()
responder( grabacion )

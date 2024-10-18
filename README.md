# IA Practica 1
## Grupo IWSIT21-7
##### ARIAS FERNANDEZ, COVADONGA
##### GARCIA FOMINAYA, JOSE MARIA
##### GILPEREZ ALCAZAR, GUILLERMO
## Guía para crear un entorno virtual
* Abrir un terminal en el directorio raíz de este repositorio.
* Ejecutar el comando: `python -m venv venv`
        
        NOTA: en algunos dispositivos el comando es python3
* Activamos el entorno virtual:
    * Windows (PowerShell): `.\venv\Scripts\activate`

            NOTA: En caso de dar error de no poder ejecutar archivos de powershell abrir powershell en modo administrador y ejecutar lo siguiente: `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser` y volver a intentarlo
    * Linux/MacOS: `source ./venv/bin/activate`
* Una vez activado el entorno virtual, podemos instalar las librerías que usaremos `python -m pip install -r requirements.txt`

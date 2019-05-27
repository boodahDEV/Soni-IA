# Soni-IA 🌌

## Descarga 👀
  * [Soni.md](https://drive.google.com/file/d/1Re4AMED8gcfD2M02xjKh6Ex-G91a8pYb/view)<br>
  * [sonic.py](https://drive.google.com/file/d/1-kHaBaKDEFAGSO1p1t6I0DA1GyCC1TBs/view)
  
## Procedimiento de instalacion 😎:
 * Creen una carpeta y dentro de ella ejecutar:
   ```console
       virtualenv -p python3 env
        source env/bin/activate
       pip3 install gym-retro  
	```

 * Creen una carpeta llamada roms dentro de la carpeta que se creó y colocar el archivo md de sonic. 
   Ejecutar:
    ``` console
      python3 -m retro.import roms
   ```

* Colocar el archivo controlador (sonic.py) dentro de la carpeta ya creada, y ejecutar
    ``` console
       python sonic.py
   ```
* Si sonic se mueve, entonces ya funciona.

## Poniendo en marcha el control
Simplemente copia el sonic.py de este repositorio a la carpeta creada y coloca lo siguiente por terminal:
   ```console
      source env/bin/activate
      python sonic.py
   ```
### Los controles basicos son:
* flecha_arriba = salta
* flecha_abajo = agachar
* flecha_izquierda = camina a izquierda
* flecha_derecha = camina a derecha

#### Se genera un archivo Data_game.csv para proximas versiones y su control autonomo con NEAT.
<br><br>
#### 🤓 Este desarrollo mas que nada es con fines educativos.

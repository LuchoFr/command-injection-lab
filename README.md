# Laboratorio de Command injection 

Mini laboratorio local para demostrar una vulnerabilidad en el codigo que permiten que un atacante injecte codigo.

Para esto creamos una app con la vulnerabilidad que permite ser levantada con python usando flask y librerias que permiten ejecucion de subprocesos con bash.

## Instalación

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt.
```
## Ejecucion 
 
python3 app/app.py

Abrir http://127.0.0.1:5000 con el navegador: 

127.0.0.1

Prueba de exploit controlado 

127.0.0.1; echo "hackeado por command injection" > hackeado.txt

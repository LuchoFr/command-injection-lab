# Command Injection Lab

## Vulnerabilidad

La aplicación concatena el input del usuario en un comando del sistema:

```python
command = f"ping -c 4 {target}"
```

Luego lo ejecuta con 

subprocess.run(command, shell=True)

Por eso si uno coloca un ; puede concatenar commands

EL riesgo de que un atacante pueda ejecutar comandos arbitrarios con los 
permisos del proceso de Flask (evitar shell=true).



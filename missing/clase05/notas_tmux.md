# Notas de Clase 05: Jobs, `tmux` y Alias

## 1. Tabla de comandos, atajos y alias

| Comando / Atajo | Qué hace |
| :--- | :--- |
| `comando &` | Lanza una tarea en segundo plano (*background*). |
| `Ctrl + Z` | Pausa (suspende) el proceso actual en primer plano. |
| `jobs` | Lista los trabajos pausados o corriendo en la terminal actual. |
| `bg %1` | Reanuda en segundo plano el trabajo número 1. |
| `fg %1` | Trae al primer plano el trabajo número 1. |
| `kill %1` | Detiene y cancela el trabajo número 1. |
| `wait` | Espera a que terminen los trabajos en segundo plano. |
| `tmux new -s e0` | Crea una nueva sesión de `tmux` llamada `e0`. |
| `Ctrl + b` luego `d` | Despega (*detach*) la sesión dejando las tareas corriendo. |
| `Ctrl + b` luego `%` | Divide el panel verticalmente (izquierda / derecha). |
| `Ctrl + b` luego `"` | Divide el panel horizontalmente (arriba / abajo). |
| `Ctrl + b` luego `o` | Cambia el cursor al siguiente panel activo. |
| `Ctrl + b` luego `c` | Crea una nueva ventana dentro de la sesión. |
| `exit` | Cierra el panel, la ventana o la sesión actual de `tmux`. |
| `tmux ls` | Muestra las sesiones de `tmux` activas desde fuera. |
| `tmux attach -t e0` | Vuelve a entrar (*attach*) a la sesión `e0`. |
| `alias ll='ls -lG'` | Crea el alias `ll` para listar archivos en detalle y con color. |
| `alias gs='git status -s'` | Crea el alias `gs` para ver el estado resumido de Git. |

---

## 2. Frontera de hoy · B3: "llamar ahora, recoger después" (MCP Tasks)

| Control de procesos en Bash | Equivalente en MCP (*Tasks*) |
| :--- | :--- |
| Lanzar con `&` | **Crear una tarea (*Task*)** asíncrona sin bloquear al agente. |
| `jobs` | **Listar tareas** activas o en curso. |
| `wait` / `fg` | **Recoger el resultado** cuando la herramienta termina su ejecución. |
| `kill %1` | **Cancelar** una tarea que está en progreso. |
| **¿Qué pasa con un `job` si cierras la terminal, y qué hace `tmux` para evitarlo?** | Si cierras la terminal, el sistema cierra todos los procesos hijos (`jobs`) asociados a esa ventana y se detienen. **`tmux`** ejecuta la sesión en un servidor independiente en segundo plano, por lo que **las tareas siguen vivas** aunque cierres la ventana o pierdas la conexión. |

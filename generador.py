import ollama
import os
import subprocess
import time

cliente_docker = ollama.Client(host='http://localhost:11434', timeout=3600)
MODELO = "qwen2.5-coder:7b"
RUTA_REPO = "/root/IA-demos/demo/preubademos/"
ARCHIVO_LOG = os.path.join(RUTA_REPO, "logs.txt")

os.chdir(RUTA_REPO)

def escribir_log(mensaje):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    texto_final = f"[{timestamp}] {mensaje}\n"
    print(texto_final.strip())
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
        f.write(texto_final)

def ejecutar_git(mensaje_commit):
    try:
        escribir_log("Subiendo cambios a GitHub...")
        subprocess.run(["git", "add", "index.html", "logs.txt"], check=True)
        subprocess.run(["git", "commit", "-m", mensaje_commit], stderr=subprocess.DEVNULL)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        escribir_log("🚀 Push exitoso a GitHub.")
    except Exception as e:
        escribir_log(f"⚠️ Error Git: {e}")

def limpiar_codigo_ia(texto):
    lineas = texto.strip().split("\n")
    if lineas[0].startswith("```"):
        lineas.pop(0)
    if lineas[-1].startswith("```"):
        lineas.pop()
    return "\n".join(lineas)

def consultar_ia(prompt):
    response = cliente_docker.generate(model=MODELO, prompt=prompt)
    return limpiar_codigo_ia(response['response'])

escribir_log("=== INICIANDO GENERACIÓN DE MAQUETA ===")

prompt_html = """
Genera un archivo 'index.html' premium para 'Vermuteca'.
Debe incluir:
1. Navbar elegante con logotipo y enlaces fluidos.
2. Sección Hero de alto impacto.
3. Menú de platos (Tapas, Platillos, Vermuts) estructurado con clases para títulos, descripciones y precios.
4. SECCIÓN DE HORARIOS ORDENADA VERTICALMENTE DÍA POR DÍA:
   - Lunes
   - Martes
   - Miércoles
   - Jueves
   - Viernes
   - Sábado
   - Domingo
5. Sección de Contacto y Footer corporativo.

Devuelve EXCLUSIVAMENTE el código HTML completo desde <!DOCTYPE html> hasta </html>. Sin notas ni explicaciones.
"""

codigo_html = consultar_ia(prompt_html)
with open(os.path.join(RUTA_REPO, "index.html"), "w", encoding="utf-8") as f:
    f.write(codigo_html)
escribir_log("HTML guardado.")

ejecutar_git("HTML premium con estructura de títulos centrados y horarios ordenados")

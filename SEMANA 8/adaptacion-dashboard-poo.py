#!/usr/bin/env python3
# ============================================================
# DASHBOARD.PY (MEJORADO)
# Autor: Henry Baldeón Ochoa
# Asignatura: Programación Orientada a Objetos
# Objetivo:
#   Organizar y ejecutar scripts de tus unidades/proyectos desde
#   un menú claro, con opciones extra (buscar, favoritos, abrir).
#
# Estructura esperada (puedes adaptarla):
#   /tu_repositorio/
#       Dashboard.py
#       Unidad 1/
#           Tema 1/
#               script1.py
#               script2.py
#       Unidad 2/
#           ...
#
# NOTA:
# - Este Dashboard detecta automáticamente carpetas "Unidad ..."
# - Guarda favoritos en un archivo: dashboard_favoritos.txt
# - Funciona en Windows / Linux / macOS
# ============================================================

import os
import sys
import subprocess
from dataclasses import dataclass
from typing import List, Optional, Tuple


# --------------------------- Utilidades ---------------------------

def clear_screen() -> None:
    """Limpia la pantalla (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def pause(msg: str = "Presiona Enter para continuar...") -> None:
    input(f"\n{msg}")


def is_python_file(filename: str) -> bool:
    return filename.lower().endswith(".py")


def safe_list_dirs(path: str) -> List[str]:
    """Lista subcarpetas (solo directorios)."""
    try:
        return sorted([f.name for f in os.scandir(path) if f.is_dir()])
    except FileNotFoundError:
        return []
    except PermissionError:
        return []
    except Exception:
        return []


def safe_list_py_files(path: str) -> List[str]:
    """Lista archivos .py (solo archivos)."""
    try:
        return sorted([f.name for f in os.scandir(path) if f.is_file() and is_python_file(f.name)])
    except FileNotFoundError:
        return []
    except PermissionError:
        return []
    except Exception:
        return []


def read_text_file(path: str) -> Optional[str]:
    """Lee un archivo de texto y devuelve su contenido."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None
    except UnicodeDecodeError:
        # fallback por si el archivo tiene otra codificación
        try:
            with open(path, "r", encoding="latin-1") as f:
                return f.read()
        except Exception:
            return None
    except Exception:
        return None


def open_in_editor(filepath: str) -> None:
    """
    Abre un archivo en el editor por defecto:
    - Windows: start
    - macOS: open
    - Linux: xdg-open
    """
    try:
        if os.name == "nt":
            os.startfile(os.path.abspath(filepath))  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", os.path.abspath(filepath)])
        else:
            subprocess.Popen(["xdg-open", os.path.abspath(filepath)])
    except Exception as e:
        print(f"No se pudo abrir el archivo en el editor: {e}")


def choose_python_interpreter() -> str:
    """
    Selecciona el intérprete de Python:
    - En Windows suele ser 'python'
    - En Linux/mac suele ser 'python3'
    """
    # Si el programa se ejecuta con python, usar el mismo intérprete:
    # sys.executable es el camino real al python actual.
    return sys.executable if sys.executable else ("python" if os.name == "nt" else "python3")


# --------------------------- Datos y Favoritos ---------------------------

@dataclass
class ScriptItem:
    unit_name: str
    topic_name: str
    script_name: str
    script_path: str

    def display_label(self) -> str:
        return f"{self.unit_name} > {self.topic_name} > {self.script_name}"


class FavoritesManager:
    """
    Maneja favoritos en un archivo de texto.
    Cada línea guarda una ruta absoluta del script.
    """
    def __init__(self, favorites_file: str) -> None:
        self.favorites_file = favorites_file
        self._favorites: List[str] = []
        self.load()

    def load(self) -> None:
        content = read_text_file(self.favorites_file)
        if not content:
            self._favorites = []
            return
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        # mantener solo existentes
        self._favorites = [p for p in lines if os.path.exists(p)]

    def save(self) -> None:
        try:
            with open(self.favorites_file, "w", encoding="utf-8") as f:
                for p in self._favorites:
                    f.write(p + "\n")
        except Exception as e:
            print(f"No se pudo guardar favoritos: {e}")

    def list(self) -> List[str]:
        return list(self._favorites)

    def is_favorite(self, path: str) -> bool:
        return os.path.abspath(path) in set(map(os.path.abspath, self._favorites))

    def add(self, path: str) -> None:
        p = os.path.abspath(path)
        if p not in self._favorites and os.path.exists(p):
            self._favorites.append(p)
            self.save()

    def remove(self, path: str) -> None:
        p = os.path.abspath(path)
        self._favorites = [x for x in self._favorites if os.path.abspath(x) != p]
        self.save()


# --------------------------- Exploración de Proyecto ---------------------------

class ProjectExplorer:
    """
    Explora la estructura del proyecto para detectar unidades, temas y scripts.
    """
    def __init__(self, base_path: str) -> None:
        self.base_path = base_path

    def get_units(self) -> List[str]:
        """
        Detecta carpetas que empiecen con "Unidad" (ej: "Unidad 1").
        Si no existen, devuelve todas las carpetas del directorio base.
        """
        all_dirs = safe_list_dirs(self.base_path)
        unidades = [d for d in all_dirs if d.lower().startswith("unidad")]
        return unidades if unidades else all_dirs

    def get_topics(self, unit_path: str) -> List[str]:
        return safe_list_dirs(unit_path)

    def get_scripts(self, topic_path: str) -> List[str]:
        return safe_list_py_files(topic_path)

    def collect_all_scripts(self) -> List[ScriptItem]:
        """
        Recorre todas las unidades y temas para construir una lista global de scripts.
        Útil para búsqueda rápida.
        """
        items: List[ScriptItem] = []
        for unit in self.get_units():
            unit_path = os.path.join(self.base_path, unit)
            topics = self.get_topics(unit_path)
            if not topics:
                # si no hay subcarpetas, buscar scripts directo en unidad
                scripts = safe_list_py_files(unit_path)
                for s in scripts:
                    spath = os.path.join(unit_path, s)
                    items.append(ScriptItem(unit, "(sin tema)", s, spath))
                continue

            for topic in topics:
                topic_path = os.path.join(unit_path, topic)
                scripts = self.get_scripts(topic_path)
                for s in scripts:
                    spath = os.path.join(topic_path, s)
                    items.append(ScriptItem(unit, topic, s, spath))
        return items


# --------------------------- Ejecutar y Mostrar Código ---------------------------

class ScriptRunner:
    """
    Maneja la visualización y ejecución de scripts.
    """
    def __init__(self) -> None:
        self.python_cmd = choose_python_interpreter()

    def show_code(self, script_path: str) -> None:
        code = read_text_file(script_path)
        print(f"\n--- Código: {os.path.basename(script_path)} ---\n")
        if code is None:
            print("No se pudo leer el archivo.")
            return
        print(code)

    def run(self, script_path: str) -> None:
        """
        Ejecuta el script en un proceso separado.
        - En Windows abre una consola nueva con cmd /k (deja la ventana abierta).
        - En Linux/mac intenta ejecutar en terminal si existe; si no, ejecuta en segundo plano.
        """
        try:
            abs_path = os.path.abspath(script_path)

            if os.name == "nt":
                # Abre una terminal y deja abierta para ver salida
                subprocess.Popen(["cmd", "/k", self.python_cmd, abs_path])
                return

            # macOS / Linux: intentar abrir terminal
            # 1) GNOME Terminal
            for term_cmd in [
                ["gnome-terminal", "--", self.python_cmd, abs_path],
                ["konsole", "-e", self.python_cmd, abs_path],
                ["xterm", "-hold", "-e", self.python_cmd, abs_path],
                ["mate-terminal", "-e", f"{self.python_cmd} {abs_path}"],
            ]:
                try:
                    subprocess.Popen(term_cmd)
                    return
                except FileNotFoundError:
                    continue
                except Exception:
                    continue

            # fallback: ejecutar sin terminal nueva
            subprocess.Popen([self.python_cmd, abs_path])

        except Exception as e:
            print(f"Ocurrió un error al ejecutar el script: {e}")


# --------------------------- Interfaz de Menú ---------------------------

class DashboardApp:
    def __init__(self) -> None:
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.explorer = ProjectExplorer(self.base_path)
        self.runner = ScriptRunner()
        self.favorites = FavoritesManager(os.path.join(self.base_path, "dashboard_favoritos.txt"))

    def header(self, title: str) -> None:
        clear_screen()
        print("=" * 60)
        print(f"{title}".center(60))
        print("=" * 60)
        print(f"Autor: Henry Baldeón Ochoa")
        print(f"Ruta del proyecto: {self.base_path}")
        print("=" * 60)

    def input_option(self, prompt: str) -> str:
        return input(f"\n{prompt} ").strip()

    def main_menu(self) -> None:
        while True:
            self.header("MENU PRINCIPAL - DASHBOARD")
            units = self.explorer.get_units()

            if not units:
                print("No se encontraron carpetas en el proyecto.")
                print("Crea carpetas como: 'Unidad 1', 'Unidad 2', etc.")
                pause()
                return

            print("\nOpciones:")
            print("1) Ver Unidades y scripts")
            print("2) Buscar script por nombre")
            print("3) Favoritos")
            print("4) Abrir carpeta del proyecto")
            print("0) Salir")

            op = self.input_option("Elige una opción:")
            if op == "0":
                print("\nSaliendo del Dashboard. ¡Éxitos!")
                break
            elif op == "1":
                self.units_menu(units)
            elif op == "2":
                self.search_menu()
            elif op == "3":
                self.favorites_menu()
            elif op == "4":
                open_in_editor(self.base_path)
                pause("Se intentó abrir la carpeta. Presiona Enter...")
            else:
                print("Opción no válida.")
                pause()

    def units_menu(self, units: List[str]) -> None:
        while True:
            self.header("UNIDADES")
            for i, u in enumerate(units, start=1):
                print(f"{i}) {u}")
            print("0) Volver")

            op = self.input_option("Selecciona una unidad:")
            if op == "0":
                return
            if not op.isdigit():
                print("Ingresa un número válido.")
                pause()
                continue

            idx = int(op) - 1
            if idx < 0 or idx >= len(units):
                print("Opción fuera de rango.")
                pause()
                continue

            unit_name = units[idx]
            unit_path = os.path.join(self.base_path, unit_name)
            self.topics_menu(unit_name, unit_path)

    def topics_menu(self, unit_name: str, unit_path: str) -> None:
        while True:
            self.header(f"TEMAS / CARPETAS - {unit_name}")
            topics = self.explorer.get_topics(unit_path)

            if not topics:
                print("No se encontraron subcarpetas (temas) dentro de esta unidad.")
                print("Se buscarán scripts directamente en la carpeta de la unidad.\n")
                self.scripts_menu(unit_name, "(sin tema)", unit_path)
                return

            for i, t in enumerate(topics, start=1):
                print(f"{i}) {t}")
            print("0) Volver")

            op = self.input_option("Selecciona un tema/carpeta:")
            if op == "0":
                return
            if not op.isdigit():
                print("Ingresa un número válido.")
                pause()
                continue

            idx = int(op) - 1
            if idx < 0 or idx >= len(topics):
                print("Opción fuera de rango.")
                pause()
                continue

            topic_name = topics[idx]
            topic_path = os.path.join(unit_path, topic_name)
            self.scripts_menu(unit_name, topic_name, topic_path)

    def scripts_menu(self, unit_name: str, topic_name: str, topic_path: str) -> None:
        while True:
            self.header(f"SCRIPTS - {unit_name} > {topic_name}")
            scripts = self.explorer.get_scripts(topic_path)

            if not scripts:
                print("No se encontraron scripts (.py) en esta carpeta.")
                pause()
                return

            for i, s in enumerate(scripts, start=1):
                spath = os.path.join(topic_path, s)
                fav_mark = "★" if self.favorites.is_favorite(spath) else " "
                print(f"{i}) [{fav_mark}] {s}")

            print("\nAcciones:")
            print("0) Volver")
            print("9) Ir al menú principal")

            op = self.input_option("Elige un script (número) o 0/9:")
            if op == "0":
                return
            if op == "9":
                return

            if not op.isdigit():
                print("Ingresa un número válido.")
                pause()
                continue

            idx = int(op) - 1
            if idx < 0 or idx >= len(scripts):
                print("Opción fuera de rango.")
                pause()
                continue

            script_name = scripts[idx]
            script_path = os.path.join(topic_path, script_name)
            self.script_actions_menu(ScriptItem(unit_name, topic_name, script_name, script_path))

    def script_actions_menu(self, item: ScriptItem) -> None:
        while True:
            self.header("ACCIONES DEL SCRIPT")
            print(f"\nSeleccionado: {item.display_label()}")
            print(f"Ruta: {item.script_path}\n")

            print("1) Ver código")
            print("2) Ejecutar script")
            print("3) Abrir script en editor")
            print("4) Marcar/Desmarcar favorito")
            print("0) Volver")

            op = self.input_option("Elige una acción:")
            if op == "0":
                return
            elif op == "1":
                self.runner.show_code(item.script_path)
                pause()
            elif op == "2":
                print("Ejecutando... (se abrirá una consola/terminal si es posible)")
                self.runner.run(item.script_path)
                pause("Script lanzado. Presiona Enter para volver...")
            elif op == "3":
                open_in_editor(item.script_path)
                pause("Se intentó abrir el script. Presiona Enter...")
            elif op == "4":
                if self.favorites.is_favorite(item.script_path):
                    self.favorites.remove(item.script_path)
                    print("Favorito removido.")
                else:
                    self.favorites.add(item.script_path)
                    print("Favorito agregado.")
                pause()
            else:
                print("Opción no válida.")
                pause()

    def search_menu(self) -> None:
        while True:
            self.header("BUSCAR SCRIPT")
            query = self.input_option("Escribe parte del nombre del script (.py) o 0 para volver:")
            if query == "0":
                return

            all_items = self.explorer.collect_all_scripts()
            matches = [it for it in all_items if query.lower() in it.script_name.lower()]

            if not matches:
                print("\nNo se encontraron coincidencias.")
                pause()
                continue

            print("\nCoincidencias:")
            for i, it in enumerate(matches, start=1):
                fav_mark = "★" if self.favorites.is_favorite(it.script_path) else " "
                print(f"{i}) [{fav_mark}] {it.display_label()}")

            op = self.input_option("\nElige un número para abrir acciones, o 0 para buscar de nuevo:")
            if op == "0":
                continue
            if not op.isdigit():
                print("Ingresa un número válido.")
                pause()
                continue

            idx = int(op) - 1
            if idx < 0 or idx >= len(matches):
                print("Opción fuera de rango.")
                pause()
                continue

            self.script_actions_menu(matches[idx])

    def favorites_menu(self) -> None:
        while True:
            self.header("FAVORITOS")
            favs = self.favorites.list()

            if not favs:
                print("Aún no tienes favoritos.")
                print("Marca scripts como favoritos desde el menú de scripts.\n")
                pause()
                return

            # Convertir rutas a ScriptItem "simple"
            items: List[ScriptItem] = []
            for p in favs:
                # Intentar inferir unidad/tema por ruta relativa
                rel = os.path.relpath(p, self.base_path)
                parts = rel.split(os.sep)
                unit = parts[0] if len(parts) >= 1 else "(desconocido)"
                topic = parts[1] if len(parts) >= 3 else "(sin tema)"
                script = parts[-1]
                items.append(ScriptItem(unit, topic, script, p))

            for i, it in enumerate(items, start=1):
                print(f"{i}) ★ {it.display_label()}")

            print("\nAcciones:")
            print("0) Volver")

            op = self.input_option("Elige un favorito para acciones, o 0 para volver:")
            if op == "0":
                return
            if not op.isdigit():
                print("Ingresa un número válido.")
                pause()
                continue

            idx = int(op) - 1
            if idx < 0 or idx >= len(items):
                print("Opción fuera de rango.")
                pause()
                continue

            self.script_actions_menu(items[idx])


# --------------------------- Punto de Entrada ---------------------------

def main() -> None:
    app = DashboardApp()
    app.main_menu()


if __name__ == "__main__":
    main()
¿
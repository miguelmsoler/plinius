import os
import pathspec
from .nodes import DirectoryNode, FileNode

class DirectoryLister:
    def __init__(self, root_path):
        self.spec = None
        self.read_gitignore(root_path)

    def read_gitignore(self, root_path):
        gitignore_path = os.path.join(root_path, '.gitignore')
        patterns = ['.git/']  # Asegurarse de ignorar siempre el directorio .git
        if os.path.isfile(gitignore_path):
            with open(gitignore_path, 'r') as gitignore_file:
                patterns += [line.strip() for line in gitignore_file if line.strip() and not line.startswith('#')]
        self.spec = pathspec.PathSpec.from_lines('gitwildmatch', patterns)

        # Loguear los patrones cargados para depuración
        print("Patrones cargados en self.spec:", patterns)


    def isIgnored(self, full_path, root_path):
        if self.spec:
            # Calcular la ruta relativa para la verificación de pathspec
            relative_path = os.path.relpath(full_path, start=root_path)
            is_ignored = self.spec.match_file(relative_path)
            # Loguear si el archivo/directorio está siendo ignorado
            if is_ignored:
                print(f"{relative_path} está siendo ignorado.")
            else:
                print(f"{relative_path} no está siendo ignorado.")
            return is_ignored
        return False
    
    def list_directory(self, root_path):
        try:
            root_node = DirectoryNode(root_path)
            entries = os.listdir(root_path)
            for entry in entries:
                full_path = os.path.join(root_path, entry)
                if self.isIgnored(full_path, root_path):
                    continue
                if os.path.isdir(full_path):
                    root_node.children.append(self.list_directory(full_path))  # Recursividad para subdirectorios
                else:
                    root_node.children.append(FileNode(full_path))
            return root_node
        except FileNotFoundError:
            print(f"El directorio {root_path} no fue encontrado.")
        except PermissionError:
            print(f"Permiso denegado para acceder a {root_path}.")

    def document_directory(self, path):
        root_node = self.list_directory(path)
        if root_node:
            root_node.document()
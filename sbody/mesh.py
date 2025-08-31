import chumpy as ch
import numpy as np


class Mesh:
    """Simple mesh class that provides the interface expected by fit_scan.py"""

    def __init__(self, v=None, f=None, filename=None):
        if filename is not None:
            self.v, self.f = self._load_obj(filename)
        else:
            self.v = v if v is not None else np.array([])
            self.f = f if f is not None else np.array([])

        # For model objects, we need a result attribute
        self.r = self.v.copy()

    def _load_obj(self, filename):
        """Load vertices and faces from an OBJ file"""
        vertices = []
        faces = []

        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('v '):  # vertex
                    parts = line.strip().split()
                    vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
                elif line.startswith('f '):  # face
                    parts = line.strip().split()
                    # OBJ faces are 1-indexed, convert to 0-indexed
                    face = [int(parts[i].split('/')[0]) - 1 for i in range(1, 4)]
                    faces.append(face)

        return np.array(vertices), np.array(faces)

    def copy(self):
        """Return a copy of the mesh"""
        new_mesh = Mesh(v=self.v.copy(), f=self.f.copy())
        new_mesh.r = self.r.copy() if hasattr(self, 'r') else new_mesh.v.copy()
        return new_mesh

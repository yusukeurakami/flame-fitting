import numpy as np


def aabbtree_compute(v, f):
    """Simple AABB tree computation - returns a simple structure with vertices and faces"""
    return {'v': v, 'f': f}


def aabbtree_nearest(cpp_handle, v_samples):
    """Simple nearest point computation - finds the closest point on the mesh surface"""
    v = cpp_handle['v']
    f = cpp_handle['f']

    # For simplicity, just find the closest vertex for now
    # This is a very basic implementation
    f_idxs = np.zeros(len(v_samples), dtype=np.uint32)
    f_part = np.zeros(len(v_samples), dtype=np.uint32)
    nearest_points = np.zeros_like(v_samples)

    for i, sample_point in enumerate(v_samples):
        # Find the closest vertex
        distances = np.linalg.norm(v - sample_point, axis=1)
        closest_vertex_idx = np.argmin(distances)
        f_idxs[i] = closest_vertex_idx
        f_part[i] = 6  # Vertex (following the original convention)
        nearest_points[i] = v[closest_vertex_idx]

    return f_idxs, f_part, nearest_points

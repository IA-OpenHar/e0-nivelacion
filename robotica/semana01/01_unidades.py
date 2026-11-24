import math


def kmh_a_ms(v_kmh):
    """convierte velocidad de km/h a m/s."""
    return v_kmh / 3.6


def rpm_a_rad_s(rpm):
    """Convierte velocidad angular de rmp a rad/s."""
    return rpm * (2 * math.pi / 60)


def grados_a_radianes(grados):
    """Convierte angulos de grados a radianes."""
    return grados * (math.pi / 180)

def kgcm_a_nm(torque_kgcm):
    """Convierte torque de kg.cm a N.m."""
    return torque_kgcm * 9.81 / 100


# --- Pruebas de validación ---
if __name__ == "__main__":
    print(f"36 km/h a m/s: {kmh_a_ms(36)}")  # Esperado: 10.0
    print(f"60 rpm a rad/s: {rpm_a_rad_s(60)}")  # Esperado: 6.283185...
    print(f"180° a radianes: {grados_a_radianes(180)}")  # Esperado: 3.141592...
    print(f"1.8 kg·cm a N·m: {kgcm_a_nm(1.8)}")  # Esperado: 0.17658
    
    # Test de validacion contra referencia 
    assert math.isclose(
        grados_a_radianes(180), math.radians(180)
    ), "Error en la conversion"
    print("Validacion exitosa: grados_a_radianes(180) coincida con math.radians(180)")
    

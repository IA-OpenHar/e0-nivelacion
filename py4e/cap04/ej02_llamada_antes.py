"""Demostracion del orden correcto de definicion y llamada de funciones."""

def print_lyrics():
    """Imprime dos versos de la canción."""
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
    
def repeat_lyrics():
    """Llama dos veces a la funcion print_lyrics."""
    print_lyrics()
    print_lyrics()
    

repeat_lyrics()
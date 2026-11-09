
# Non-Metal Elements
from pyscript import display, document


def search_element(e):
    document.getElementById('result').innerHTML = ''

    user_input = document.getElementById('element_input').value.strip().title()

    non_metals = {
        'O': {'name': 'Oxygen', 'atomic_num': 8, 'atomic_mass': 15.999},
        'Br': {'name': 'Bromine', 'atomic_num': 35, 'atomic_mass': 79.904},
        'H': {'name': 'Hydrogen', 'atomic_num': 1, 'atomic_mass': 1.008},
        'Xe': {'name': 'Xenon', 'atomic_num': 54, 'atomic_mass': 131.293},
        'C': {'name': 'Carbon', 'atomic_num': 6, 'atomic_mass': 12.011},
        'Cl': {'name': 'Chlorine', 'atomic_num': 17, 'atomic_mass': 35.45},
        'Se': {'name': 'Selenium', 'atomic_num': 34, 'atomic_mass': 78.971},
        'He': {'name': 'Helium', 'atomic_num': 2, 'atomic_mass': 4.0026},
        'Rn': {'name': 'Radon', 'atomic_num': 86, 'atomic_mass': 222},
        'N': {'name': 'Nitrogen', 'atomic_num': 7, 'atomic_mass': 14.007},
        'I': {'name': 'Iodine', 'atomic_num': 53, 'atomic_mass': 126.904},
        'Ar': {'name': 'Argon', 'atomic_num': 18, 'atomic_mass': 39.948},
        'F': {'name': 'Fluorine', 'atomic_num': 9, 'atomic_mass': 18.998},
        'Kr': {'name': 'Krypton', 'atomic_num': 36, 'atomic_mass': 83.798},
        'S': {'name': 'Sulfur', 'atomic_num': 16, 'atomic_mass': 32.06},
        'P': {'name': 'Phosphorus', 'atomic_num': 15, 'atomic_mass': 30.974},
        'Ne': {'name': 'Neon', 'atomic_num': 10, 'atomic_mass': 20.180}
    }

    data = non_metals.get(user_input, {
        'name': 'Not Found',
        'atomic_num': 'N/A',
        'atomic_mass': 'N/A'
    })

    display(f"Symbol: {user_input}", target="result")
    display(f"Element: {data['name']}", target="result")
    display(f"Atomic Number: {data['atomic_num']}", target="result")
    display(f"Atomic Mass: {data['atomic_mass']}", target="result")

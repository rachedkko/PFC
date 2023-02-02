from cx_Freeze import setup,Executable

setup(
    name="PFC Pokémon",
    version="1.0",
    executables=[Executable("client.py")]

    )

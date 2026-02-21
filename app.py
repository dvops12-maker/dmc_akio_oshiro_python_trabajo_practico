import streamlit as st

st.set_page_config(
    page_title="Proyecto Módulo 1 - Fundamentos",
    page_icon="📊",
    layout="wide"
)
if "actividades" not in st.session_state:
    st.session_state.actividades = []  


# Ejercicio 4 (POO)

class Actividad:
    def __init__(self, nombre: str, tipo: str, presupuesto: float, gasto_real: float):
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = float(presupuesto)
        self.gasto_real = float(gasto_real)

    def esta_en_presupuesto(self) -> bool:
        return self.gasto_real <= self.presupuesto

    def mostrar_info(self) -> str:
        diff = self.presupuesto - self.gasto_real
        estado = "Dentro del presupuesto ✅" if self.esta_en_presupuesto() else "Presupuesto excedido ⚠️"
        return (
            f"**Actividad:** {self.nombre}\n\n"
            f"**Tipo:** {self.tipo}\n\n"
            f"**Presupuesto:** {self.presupuesto:.2f}\n\n"
            f"**Gasto real:** {self.gasto_real:.2f}\n\n"
            f"**Diferencia (presupuesto - gasto):** {diff:.2f}\n\n"
            f"**Estado:** {estado}"
        )


def home():
    st.title("Proyecto Módulo 1 – Fundamentos (Streamlit)")
    st.write("**Nombre del estudiante:** Akio Alexis Oshiro Nakasone")
    st.write("**Curso / Módulo:** Especialización Python for Analytics – Módulo 1 (Python Fundamentals)")
    st.write("**Año:** 2026")

    st.write("---")
    st.write(
        "### Objetivo del trabajo\n"
        "Integrar conceptos fundamentales de programación en Python a través de una aplicación en Streamlit, "
        "incluyendo variables y condicionales, estructuras de datos, funciones y programación funcional, "
        "y programación orientada a objetos (POO)."
    )

    st.write("### Tecnologías que utilicé y requeridas")
    st.write("- Python")
    st.write("- Streamlit")

    
st.markdown(
    """
    <div style="
        padding:14px 16px;
        border-radius:14px;
        border:1px solid rgba(0,0,0,.10);
        background: linear-gradient(135deg, rgba(59,130,246,.10), rgba(168,85,247,.08));
        box-shadow: 0 8px 18px rgba(0,0,0,.06);
    ">
      <h4 style="margin:0;font-size:15px;">🧭 Guía rápida</h4>
      <p style="margin:6px 0 0 0;font-size:13px;line-height:1.4;">
        Navega desde la barra lateral. Tu avance se guarda mientras la sesión siga abierta.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)


def ejercicio_1():
    st.title("Ejercicio 1")
    st.write("Verificador de presupuesto:")
    st.write("Ingresa un presupuesto y un gasto, y el sistema evalúa si se excedió.")

    presupuesto = st.number_input("Presupuesto", min_value=0.0, step=1.0, format="%.2f")
    gasto = st.number_input("Gasto", min_value=0.0, step=1.0, format="%.2f")

    if st.button("Evaluador"):
        diferencia = presupuesto - gasto
        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto.")
        else:
            st.warning("El gasto excede el presupuesto.")
        st.write(f"Diferencia (presupuesto - gasto): {diferencia:.2f}")


def ejercicio_2():
    st.title("Ejercicio 2")
    st.write("Registro de actividades financieras:")
    col1, col2 = st.columns(2)

    with col1:
        nombre = st.text_input("Nombre de la actividad")
        tipo = st.selectbox("Tipo", ["Ingreso", "Gasto", "Inversión", "Ahorro", "Otro"])

    with col2:
        presupuesto = st.number_input("Presupuesto", min_value=0.0, step=1.0, format="%.2f")
        gasto_real = st.number_input("Gasto real", min_value=0.0, step=1.0, format="%.2f")

    if st.button("Agregar actividad"):
        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            st.warning("Debes ingresar un nombre para la actividad.")
        else:
            actividad = {
                "nombre": nombre_limpio,
                "tipo": tipo,
                "presupuesto": float(presupuesto),
                "gasto_real": float(gasto_real),
            }
            st.session_state.actividades.append(actividad)
            st.success("✅ Actividad agregada correctamente.")

    st.subheader("Actividades registradas")

    if not st.session_state.actividades:
        st.write("TodavíA no hay actividades registradas.")
        return

    st.dataframe(st.session_state.actividades, use_container_width=True)

    st.write("### Estado de cada actividad")
    for a in st.session_state.actividades:
        if a["gasto_real"] <= a["presupuesto"]:
            st.write(f"- **{a['nombre']}**: Dentro del presupuesto")
        else:
            st.write(f"- **{a['nombre']}**: Presupuesto excedido")

def tener_retorno(actividad: dict, tasa: float, meses: int) -> float:
    return float(actividad["presupuesto"]) * float(tasa) * int(meses)


def ejercicio_3():
    st.title("Ejercicio 3")
    st.write("**Fórmula:** Retorno = presupuesto × tasa × meses")

    if not st.session_state.actividades:
        st.warning("Primero registra actividades en el Ejercicio 2 para poder calcular retornos.")
        return

    tasa = st.slider("Tasa (por ejemplo 0.05 = 5%)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
    meses = st.number_input("Meses", min_value=1, step=1, value=12)

    if st.button("Calcular retorno"):
        retornos = list(map(lambda act: tener_retorno(act, tasa, meses), st.session_state.actividades))

        st.write("### Resultados")
        for act, ret in zip(st.session_state.actividades, retornos):
            st.write(f"- **{act['nombre']}** → Retorno esperado: **{ret:.2f}**")


def ejercicio_4():
    st.title("Ejercicio 4")

    if not st.session_state.actividades:
        st.warning("Primero registra actividades en el Ejercicio 2 para poder crear objetos.")
        return

    objetos = [
        Actividad(a["nombre"], a["tipo"], a["presupuesto"], a["gasto_real"])
        for a in st.session_state.actividades
    ]

    st.subheader("Actividades (como objetos)")
    for obj in objetos:
        st.write("---")
        st.write(obj.mostrar_info())
        if obj.esta_en_presupuesto():
            st.success("Cumple el presupuesto.")
        else:
            st.warning("No cumple el presupuesto.")

st.sidebar.title("Menú")
opcion = st.sidebar.selectbox(
    "Estoy en:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

if opcion == "Home":
    home()
elif opcion == "Ejercicio 1":
    ejercicio_1()
elif opcion == "Ejercicio 2":
    ejercicio_2()
elif opcion == "Ejercicio 3":
    ejercicio_3()
elif opcion == "Ejercicio 4":
    ejercicio_4()
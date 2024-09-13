import streamlit as st
import pandas as pd
import numpy as np


def validate_form(fields):
    errors = {}
    for field, value in fields.items():
        if not value:
            errors[field] = f" es obligatorio."
    return errors


# title
st.title("Formulario QA")

option = st.radio(
    "¿Qué vas a registrar?",
    ["Reportes", "Incidencia de Reportes"],
)

# Manejo de la opción seleccionada
if option == "Reportes":
    st.header("Creación de reporte de QA")

    # Campos específicos para reportes
    report_name = st.text_input("Nombre del reporte")
    priority = st.radio(
        "Prioridad",
        ["BAJA", "MEDIA", "ALTA", "BLOQUEANTE"],
        index=None,
    )

    product = st.radio(
        "Producto",
        [
            "AGROS BUYER",
            "AGROS STORE",
            "COMMUNITTY PANEL",
            "APPCOPIO",
            "PERHUSA",
            "ALPACA TRACE",
            "ACOPIO MODULO",
            "MICACAO",
            "IDENTI-COLLECTOR",
            "APP IDENTI-COLLECTOR",
        ],
        index=None,
    )

    pm = st.radio(
        "PM a cargo",
        [
            "SILVIA",
            "GABO",
        ],
        index=None,
    )

    qa = st.radio(
        "QA a cargo",
        [
            "JUAN",
        ],
        index=None,
    )

    # falta los devs involucrados

    design = st.radio(
        "Equipo de Diseño a cargo",
        [
            "ALEJO",
        ],
        index=None,
    )

    # Espacio para subir un link
    figma_link = st.text_input("Ingrese el link de figma")

    # Validación
    if st.button("Enviar reporte"):
        fields = {
            "Nombre del reporte": report_name,
            "Prioridad": priority,
            "Producto": product,
            "PM a cargo": pm,
            "QA a cargo": qa,
        }

        errors = validate_form(fields)

        if errors:
            for field, error in errors.items():
                st.error(f"{field}: {error}")
        else:
            st.success("Formulario enviado exitosamente.")


elif option == "Incidencia de Reportes":
    st.header("Creación de incidencia a reporte de QA")

    # Campos específicos para incidencias
    id_hu = st.text_input("Identificador de la historia de usuario")
    obs_name = st.text_input("Nombre de la observación")

    type = st.radio(
        "Tipo de observación",
        ["BUG", "DISEÑO", "LOGICA"],
        index=None,
    )

    exe_env = st.radio(
        "Ambiente de ejecución",
        ["DEV", "QA", "BETA", "PROD"],
        index=None,
    )

    priority = st.radio(
        "Prioridad",
        ["BAJA", "MEDIA", "ALTA", "BLOQUEANTE"],
        index=None,
    )

    exe_devices = st.radio(
        "Dispositivo de ejecucion",
        ["NAVEGADOR WEB", "NAVEGADOR WEB RESPONSIVO", "MOBILE"],
        index=None,
    )

    comp_app = st.radio(
        "Componente de la aplicación involucrado",
        ["BACKEND", "FRONTEND", "SERVICIO DE TERCEROS"],
        index=None,
    )

    # falta los devs involucrados

    obs_summary = st.text_area("Resumen de la observación", " ")

    exp_result = st.text_area("Resultado esperado", " ")
    # Espacio para subir fotos o videos
    archivos = st.file_uploader(
        "Sube fotos o videos relacionados con la incidencia",
        accept_multiple_files=True,
        type=["jpg", "jpeg", "png", "mp4", "avi", "mkv"],
    )

    if st.button("Enviar Incidencia"):
        fields = {
            "Identificador de la historia de usuario": id_hu,
            "Nombre de la observación": obs_name,
            "Tipo de observación": type,
            "Ambiente de ejecución": exe_env,
            "Prioridad": priority,
            "Dispositivo de ejecucion": exe_devices,
            "Componente de la aplicación involucrado": comp_app,
            "Resumen de la observación": obs_summary,
            "Resultado esperado": exp_result,
        }

        # prueba para ver como se envian los datos
        print("Datos enviados:")
        for field, value in fields.items():
            print(f"{field}: {value}")

        errors = validate_form(fields)

        if errors:
            for field, error in errors.items():
                st.error(f"{field}: {error}")
        else:
            st.success("Formulario enviado exitosamente.")

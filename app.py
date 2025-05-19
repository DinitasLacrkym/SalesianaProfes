# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="BrightSpace Instructores", layout="wide")

st.title("📊 Análisis de Actividades en BrightSpace")
st.write("Este dashboard nos  permite analizar el uso del LMS  BrightSpace por parte  de los profesores de la Fundación Universitaria Salesiana en e.")

# Enlace público al archivo CSV desde Google Drive
csv_url = "https://drive.google.com/uc?export=download&id=1QGs-0UrDWK7AX3u15CqJja-J6V_6G0Fs"

# Cargar los datos
df = pd.read_csv(csv_url)

# Columnas esperadas (incluyendo asignaciones)
cols_metrica = [
    "Cantidad de elementos de calificación",
    "Cantidad de publicaciones de debate",
    "Cantidad de publicaciones de debate iniciado",
    "Cantidad de inicios de sesión en el sistema",
    "Cantidad de asignaciones"
]

# Convertir columnas a numérico
df[cols_metrica] = df[cols_metrica].apply(pd.to_numeric, errors='coerce').fillna(0)

# Tabla resumen
st.header("📋 Resumen General")
resumen_total = df[cols_metrica].sum().reset_index()
resumen_total.columns = ["Métrica", "Total"]
st.table(resumen_total)

# Indicadores Clave en columnas
st.header("📌 Indicadores Clave")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(label="📝 Calificaciones", value=int(resumen_total.loc[0, "Total"]))

with col2:
    st.metric(label="💬 Publicaciones de debate", value=int(resumen_total.loc[1, "Total"]))

with col3:
    st.metric(label="📢 Debates iniciados", value=int(resumen_total.loc[2, "Total"]))

with col4:
    st.metric(label="🔐 Inicios de sesión", value=int(resumen_total.loc[3, "Total"]))

with col5:
    st.metric(label="📂 Asignaciones", value=int(resumen_total.loc[4, "Total"]))

# Gráficos por profesor
st.header("📊 Análisis por Profesor")

fig1 = px.bar(df, x="Nombre de Profesor", y="Cantidad de elementos de calificación",
              title="📝 Elementos de calificación por profesor", color="Nombre de Profesor", text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(df, x="Nombre de Profesor", y="Cantidad de publicaciones de debate",
              title="💬 Publicaciones de debate por profesor", color="Nombre de Profesor", text_auto=True)
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.bar(df, x="Nombre de Profesor", y="Cantidad de publicaciones de debate iniciado",
              title="📢 Debates iniciados por profesor", color="Nombre de Profesor", text_auto=True)
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.bar(df, x="Nombre de Profesor", y="Cantidad de inicios de sesión en el sistema",
              title="🔐 Inicios de sesión por profesor", color="Nombre de Profesor", text_auto=True)
st.plotly_chart(fig4, use_container_width=True)

fig5 = px.bar(df, x="Nombre de Profesor", y="Cantidad de asignaciones",
              title="📂 Asignaciones por profesor", color="Nombre de Profesor", text_auto=True)
st.plotly_chart(fig5, use_container_width=True)

# 🔍 Análisis de uso total de la plataforma
st.header("🏆 Ranking de uso total de la plataforma")

# Crear columna "Uso Total"
df["Uso Total"] = df[cols_metrica].sum(axis=1)

# Ordenar de mayor a menor
df_uso = df.sort_values("Uso Total", ascending=False)

# Gráfico de uso total
fig_uso = px.bar(df_uso, x="Nombre de Profesor", y="Uso Total",
                 title="🏆 Uso total de la plataforma por profesor",
                 color="Nombre de Profesor", text_auto=True)
st.plotly_chart(fig_uso, use_container_width=True)

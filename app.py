
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="BrightSpace Instructores", layout="wide")

st.title("📊 Análisis de Actividades en BrightSpace")
st.write("Esta aplicación permite analizar las actividades de los instructores en la plataforma BrightSpace.")

# Autenticación con Google
# Cargar hoja pública de Google Sheets como CSV
SHEET_ID = "1Eh3X8Bwd-0GoF3pyl0Xz6-oCOJm-SW9l5fItahcn99g"
SHEET_NAME = "Hoja 1"  # Asegúrate que coincide con el nombre de la hoja
csv_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
df = pd.read_csv(csv_url).dropna(how="all")

# Limpieza y conversión
cols_metrica = [
    "Cantidad de elementos de calificación",
    "Cantidad de publicaciones de debate",
    "Cantidad de publicaciones de debate iniciado",
    "Cantidad de inicios de sesión en el sistema"
]
df[cols_metrica] = df[cols_metrica].apply(pd.to_numeric, errors='coerce').fillna(0)

# Tabla resumen
st.header("📋 Resumen General")
resumen_total = df[cols_metrica].sum().reset_index()
resumen_total.columns = ["Métrica", "Total"]
st.table(resumen_total)

# Indicadores KPI
st.header("📌 Indicadores Clave")
fig_kpi = go.Figure()
fig_kpi.add_trace(go.Indicator(mode="number", value=resumen_total.loc[0, "Total"], title="📝 Calificaciones"))
fig_kpi.add_trace(go.Indicator(mode="number", value=resumen_total.loc[1, "Total"], title="💬 Publicaciones de debate"))
fig_kpi.add_trace(go.Indicator(mode="number", value=resumen_total.loc[2, "Total"], title="📢 Debates iniciados"))
fig_kpi.add_trace(go.Indicator(mode="number", value=resumen_total.loc[3, "Total"], title="🔐 Inicios de sesión"))
st.plotly_chart(fig_kpi, use_container_width=True)

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


# Gráfica combinada: Asignaciones vs Inicios de sesión por profesor
st.header("📈 Comparación: Asignaciones vs Inicios de Sesión por Profesor")
fig_comparativa = go.Figure()

fig_comparativa.add_trace(go.Bar(
    x=df["Nombre de Profesor"],
    y=df["Cantidad de asignaciones"],
    name="📂 Asignaciones"
))

fig_comparativa.add_trace(go.Bar(
    x=df["Nombre de Profesor"],
    y=df["Cantidad de inicios de sesión en el sistema"],
    name="🔐 Inicios de Sesión"
))

fig_comparativa.update_layout(
    barmode='group',
    xaxis_title="Profesor",
    yaxis_title="Cantidad",
    title="📊 Asignaciones vs Inicios de Sesión por Profesor",
    legend_title="Métrica"
)

st.plotly_chart(fig_comparativa, use_container_width=True)

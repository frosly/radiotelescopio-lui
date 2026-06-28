import streamlit as st
import base64
import os

# Configuración de la página
st.set_page_config(
    page_title="Radiotelescopio del Amor - Señales Cósmicas",
    page_icon="🌌",
    layout="centered"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        background-color: #0b0f19;
        color: #e2e8f0;
    }
    h1, h2, h3 {
        color: #fef08a !important; /* Amarillo Girasol */
        font-family: 'Courier New', Courier, monospace;
    }
    .stSlider > div > div > div > div {
        background-color: #fef08a;
    }
    .estatica {
        font-family: monospace;
        color: #64748b;
        text-align: center;
        padding: 20px;
        border: 1px dashed #334155;
        border-radius: 10px;
        background-color: #0f172a;
    }
    .mensaje-amor {
        background: linear-gradient(135deg, #1e1b4b 0%, #311042 100%);
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #fef08a;
        margin-top: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
    }
    .audio-contenedor {
        margin-top: 15px;
        text-align: center;
    }
    audio {
        width: 100%;
        max-width: 400px;
    }
    </style>
    """, unsafe_allow_html=True)

# Función definitiva para reproducir el archivo local convertido a Base64
def reproducir_audio_local(nombre_archivo):
    # Buscamos el archivo en la carpeta interna del servidor
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "rb") as f:
            audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        audio_html = f"""
        <div class="audio-contenedor">
            <audio controls autoplay>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                Tu navegador no soporta este reproductor.
            </audio>
        </div>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
    else:
        st.error(f"⚠️ El archivo '{nombre_archivo}' no se encuentra en el satélite. Verifica el nombre en GitHub.")

# Encabezado de la App
st.title("🌌 Observatorio Espacial Personalizado")
st.subheader("Proyecto: Radiotelescopio del Amor")
st.write(f"**Operador del Sistema:** nenito | **Objetivo de Escaneo:** my queen (Luisaury)")
st.markdown("---")

st.write("✨ *Luisaury, arrastra el dial del radiotelescopio para sintonizar las frecuencias cósmicas y captar las señales ocultas...*")

# El control deslizante (Dial de Frecuencia de 100 a 105 MHz)
frecuencia = st.slider(
    "🎛️ Ajustar Frecuencia del Radiotelescopio (MHz):",
    min_value=100.0,
    max_value=105.0,
    value=100.0,
    step=0.1,
    format="%.1f MHz"
)

st.markdown("---")

# Nombres exactos de tus archivos con el doble .mp3.mp3 que generó Windows
CANCIONES = {
    "1d_little_things": "1d_little_things.mp3.mp3",
    "1d_write_a_song": "1d_write_a_song.mp3.mp3",
    "1d_half_a_heart": "1d_half_a_heart.mp3.mp3",
    "1d_night_changes": "1d_night_changes.mp3.mp3",
    "1d_if_i_could_fly": "1d_if_i_could_fly.mp3.mp3",
    "btr_real_ikyk": "btr_ikyk.mp3.mp3"
}

# Lógica del Radiotelescopio
if frecuencia == 100.5:
    st.success("🛰️ ¡SEÑAL DETECTADA: Frecuencia de Inicio de Órbita (29/06/2025)!")
    st.balloons() 
    
    st.markdown("""
    <div class="mensaje-amor">
        <h3>🌻 El día que nuestro universo cambió</h3>
        <p><b>Frecuencia Estelar: 100.5 MHz</b></p>
        <p>Un 29 de junio de 2025 (¡el día de mi cumpleaños!), el espacio-tiempo se alineó perfectamente 
        para permitirme conocerte. Desde ese instante, mi órbita cambió por completo para girar alrededor de ti, 
        mi flor favorita en todo el cosmos.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("🎵 *Sintonizando: Little Things - One Direction*")
    reproducir_audio_local(CANCIONES["1d_little_things"])

elif frecuencia == 102.0:
    st.success("🛰️ ¡SEÑAL DETECTADA: Frecuencia de la Primera Cita (20/08/2025)!")
    st.balloons()
    
    st.markdown("""
    <div class="mensaje-amor">
        <h3>✍️ El primer capítulo de nuestra historia</h3>
        <p><b>Frecuencia Estelar: 102.0 MHz</b></p>
        <p>Un 20 de agosto empezamos a salir. No imaginaba que esos primeros encuentros se convertirían 
        en la historia de amor más bonita de mi vida. Fue el inicio de todo lo que somos hoy.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("🎵 *Sintonizando: I Want to Write You a Song - One Direction*")
    reproducir_audio_local(CANCIONES["1d_write_a_song"])

elif frecuencia == 101.7:
    st.success("🛰️ ¡SEÑAL DETECTADA: Frecuencia del Gran Impacto (17/01/2026)!")
    st.balloons()
    
    st.markdown("""
    <div class="mensaje-amor">
        <h3>💖 El Inicio Oficial de Nuestra Galaxia</h3>
        <p><b>Frecuencia Estelar: 101.7 MHz</b></p>
        <p>El 17 de enero de 2026 dejó de ser una fecha cualquiera para convertirse en el día en que nos hicimos novios. 
        Por eso, los 17 de cada mes son nuestro cumple mes. ¡Te amo con todo mi corazón, my queen!</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("🎵 *Sintonizando: Half a Heart - One Direction*")
    reproducir_audio_local(CANCIONES["1d_half_a_heart"])

elif frecuencia == 102.7:
    st.success("🛰️ ¡SEÑAL DETECTADA: Frecuencia de la Estrella Más Brillante (07/02)!")
    st.balloons()
    
    st.markdown("""
    <div class="mensaje-amor">
        <h3>🎂 El destello más hermoso del cosmos</h3>
        <p><b>Frecuencia Estelar: 102.7 MHz</b></p>
        <p>El 7 de febrero nació la persona que llena mis días de luz. Eres hermosa, inteligente y mi compañera perfecta. 
        Si pudiera, te regalaría un campo infinito de girasoles en la Luna.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("🎵 *Sintonizando: Night Changes - One Direction*")
    reproducir_audio_local(CANCIONES["1d_night_changes"])

elif frecuencia == 104.2:
    st.success("🛰️ ¡SEÑAL DETECTADA: Frecuencia del Combustible Espacial!")
    
    st.markdown("""
    <div class="mensaje-amor">
        <h3>🍝 Transmisión Especial: El Menú Intergaláctico</h3>
        <p><b>Frecuencia Estelar: 104.2 MHz</b></p>
        <p>Los sistemas del radiotelescopio indican que la energía de la reina está baja. 
        Se sugiere recargar baterías con un plato gigante de su comida favorita: 
        <b>¡Pasta con carne molida preparada por su nenito!</b> ¿Te provoca una cita?</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("🎵 *Sintonizando: If I Could Fly - One Direction*")
    reproducir_audio_local(CANCIONES["1d_if_i_could_fly"])

else:
    # Ruido cósmico por defecto
    st.markdown(f"""
    <div class="estatica">
        <p>📡 ESCANEANDO EL ESPACIO PROFUNDO... Frecuencia actual: <b>{frecuencia} MHz</b></p>
        <p style="font-size: 0.8rem; color: #475569;">[Ruido cósmico: ░░▒▒▓▓🎚️▓▓▒▒░░] Pistas: Busca en 100.5, 101.7, 102.0, 102.7 o 104.2</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("📻 *Interceptando señal de fondo:*")
    reproducir_audio_local(CANCIONES["btr_real_ikyk"])

# Pie de página fijo
st.markdown("<br><br><p style='text-align: center; color: #475569; font-size: 0.8rem;'>Hecho con 💛 por tu nenito para su reina Luisaury</p>", unsafe_allow_html=True)

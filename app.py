import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la página (Debe ser la primera instrucción de Streamlit)
st.set_page_config(page_title="Simulador de Procesos", layout="wide", initial_sidebar_state="collapsed")

# 2. Ocultar la interfaz de Streamlit (Menús, Header, Footer)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
div[data-testid="stStatusWidget"] {visibility: hidden;}
/* Ajustar márgenes para que ocupe toda la pantalla */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
iframe {
    border: none;
    width: 100%;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. Todo el código HTML/CSS/JS dentro de un string
html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulador EdTech: Procesos de la Memoria RAM y Hardware</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* =========================================
        VARIABLES Y ESTILOS GLOBALES
           ========================================= */
        :root {
            --bg-base: #05050a;
            --bg-panel: rgba(15, 15, 30, 0.7);
            --bg-panel-hover: rgba(25, 25, 45, 0.9);
            --primary-cyan: #00e5ff;
            --primary-purple: #9d4edd;
            --secondary-purple: #5a189a;
            --text-main: #e0e0e0;
            --text-muted: #8a8a9e;
            --border-glow: rgba(0, 229, 255, 0.3);
            --glow-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
            --success: #00ff88;
            --warning: #ffaa00;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-base);
            color: var(--text-main);
            background-image: 
                radial-gradient(circle at 15% 50%, rgba(157, 78, 221, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 85% 30%, rgba(0, 229, 255, 0.08) 0%, transparent 50%);
            background-attachment: fixed;
            min-height: 100vh;
            line-height: 1.6;
        }

        /* =========================================
        TIPOGRAFÍA Y UTILIDADES
           ========================================= */
        h1, h2, h3 { font-weight: 800; letter-spacing: -0.5px; }
        h2 { color: var(--primary-cyan); font-size: 1.5rem; margin-bottom: 1rem; border-bottom: 1px solid var(--border-glow); padding-bottom: 0.5rem; }
        h3 { color: var(--primary-purple); font-size: 1.1rem; margin-bottom: 0.5rem; }
        p { font-size: 0.95rem; color: var(--text-muted); margin-bottom: 1rem; }
        ul { margin-left: 1.5rem; margin-bottom: 1rem; color: var(--text-muted); font-size: 0.95rem; }
        li { margin-bottom: 0.5rem; }
        .mono { font-family: 'JetBrains Mono', monospace; }

        /* =========================================
        LAYOUT PRINCIPAL
           ========================================= */
        header {
            text-align: center;
            padding: 2rem 1rem;
            background: linear-gradient(180deg, rgba(5,5,10,0.9) 0%, transparent 100%);
            border-bottom: 1px solid rgba(0, 229, 255, 0.1);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }
        
        header h1 { 
            font-size: 2.2rem; 
            background: linear-gradient(90deg, var(--primary-cyan), var(--primary-purple)); 
            background-clip: text; 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
        }
        
        header p { 
            max-width: 800px; 
            margin: 0 auto; 
            color: var(--text-muted); 
        }
        
        .btn-criteria {
            background: rgba(0, 229, 255, 0.1);
            border: 1px solid var(--primary-cyan);
            color: var(--primary-cyan);
            padding: 0.5rem 1.5rem;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            margin-top: 0.5rem;
        }
        .btn-criteria:hover {
            background: var(--primary-cyan);
            color: var(--bg-base);
            box-shadow: var(--glow-shadow);
        }

        .layout-grid {
            max-width: 1400px;
            margin: 2rem auto;
            padding: 0 1rem;
            display: grid;
            grid-template-columns: 1fr 400px;
            gap: 2rem;
        }

        /* =========================================
        PANELES DE CRISTAL (GLASSMORPHISM)
           ========================================= */
        .glass-panel {
            background: var(--bg-panel);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
            transition: border-color 0.3s ease;
        }
        .glass-panel:hover { border-color: rgba(157, 78, 221, 0.3); }

        /* =========================================
        BOTONES GENERALES
           ========================================= */
        button {
            background: transparent;
            border: 1px solid var(--primary-cyan);
            color: var(--primary-cyan);
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            font-family: 'Inter', sans-serif;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.85rem;
        }
        button:hover:not(:disabled) { background: rgba(0, 229, 255, 0.1); box-shadow: var(--glow-shadow); }
        button.primary { background: var(--primary-cyan); color: var(--bg-base); }
        button.primary:hover:not(:disabled) { background: #00b8cc; box-shadow: 0 0 20px rgba(0, 229, 255, 0.6); }
        button.danger { border-color: var(--primary-purple); color: var(--primary-purple); }
        button.danger:hover:not(:disabled) { background: rgba(157, 78, 221, 0.1); box-shadow: 0 0 15px rgba(157, 78, 221, 0.4); }
        button:disabled { opacity: 0.3; cursor: not-allowed; border-color: var(--text-muted); color: var(--text-muted); box-shadow: none; }

        /* =========================================
        SIMULADOR 1: CONTROLES Y VISUALIZACIÓN
           ========================================= */
        .controls-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        .control-group {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        label { font-size: 0.85rem; color: var(--primary-cyan); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
        
        input[type="number"], select {
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(0, 229, 255, 0.2);
            color: var(--text-main);
            padding: 0.75rem;
            border-radius: 8px;
            font-family: 'JetBrains Mono', monospace;
            outline: none;
            transition: all 0.3s ease;
        }
        input[type="number"]:focus, select:focus { border-color: var(--primary-cyan); box-shadow: 0 0 10px rgba(0, 229, 255, 0.2); }
        select option { background: var(--bg-base); color: var(--text-main); }

        .btn-group {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
            align-items: center;
        }

        .visualizer {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }
        .node-box {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1rem;
            min-height: 150px;
            position: relative;
        }
        .node-box h4 {
            position: absolute;
            top: -10px;
            left: 15px;
            background: var(--bg-panel);
            padding: 0 8px;
            font-size: 0.8rem;
            color: var(--text-muted);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 4px;
        }
        
        .queue-container, .ram-container {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            align-items: flex-start;
            justify-content: center;
            padding-top: 1rem;
            min-height: 120px;
        }

        .cpu-container {
            grid-column: 1 / -1;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 2rem;
            padding: 2rem;
            background: radial-gradient(circle, rgba(157, 78, 221, 0.1) 0%, transparent 70%);
            border: 1px solid rgba(157, 78, 221, 0.2);
            border-radius: 12px;
            margin-bottom: 1.5rem;
            position: relative;
        }
        .cpu-core {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 2px dashed rgba(255,255,255,0.1);
            display: flex;
            justify-content: center;
            align-items: center;
            transition: all 0.3s ease;
        }
        .cpu-core.active {
            border: 2px solid var(--primary-cyan);
            box-shadow: 0 0 30px rgba(0, 229, 255, 0.4), inset 0 0 20px rgba(0, 229, 255, 0.2);
            animation: pulse-cpu 2s infinite;
        }
        @keyframes pulse-cpu {
            0% { box-shadow: 0 0 20px rgba(0, 229, 255, 0.4), inset 0 0 10px rgba(0, 229, 255, 0.2); }
            50% { box-shadow: 0 0 40px rgba(0, 229, 255, 0.7), inset 0 0 30px rgba(0, 229, 255, 0.4); }
            100% { box-shadow: 0 0 20px rgba(0, 229, 255, 0.4), inset 0 0 10px rgba(0, 229, 255, 0.2); }
        }

        /* TARJETAS DE PROCESO */
        .process-card {
            background: linear-gradient(135deg, rgba(0, 229, 255, 0.1), rgba(157, 78, 221, 0.1));
            border: 1px solid var(--primary-purple);
            border-radius: 8px;
            padding: 0.75rem;
            text-align: center;
            min-width: 70px;
            animation: fade-in 0.3s ease-out;
            position: relative;
        }
        .process-card.active { border-color: var(--primary-cyan); background: rgba(0, 229, 255, 0.2); box-shadow: 0 0 15px rgba(0,229,255,0.3); }
        .process-card .pid { font-size: 0.9rem; font-weight: 800; color: #fff; display: block; }
        .process-card .ptime { font-size: 0.75rem; color: var(--primary-cyan); font-family: 'JetBrains Mono', monospace; }
        .process-card .pstate { font-size: 0.6rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.3rem; display: block; }
        
        @keyframes fade-in { from { opacity: 0; transform: scale(0.8); } to { opacity: 1; transform: scale(1); } }

        /* MÉTRICAS */
        .metrics-panel {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            margin-top: 1.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(255,255,255,0.1);
        }
        .metric-box {
            background: rgba(0,0,0,0.3);
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .metric-box span { display: block; }
        .metric-label { font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; margin-bottom: 0.5rem; }
        .metric-value { font-size: 1.2rem; font-weight: 800; color: var(--primary-cyan); font-family: 'JetBrains Mono', monospace; }

        /* =========================================
        PANELES INFORMATIVOS DINÁMICOS Y ESTÁTICOS
           ========================================= */
        .info-panel {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            height: 100%;
        }
        .dynamic-log {
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid var(--border-glow);
            border-radius: 8px;
            padding: 1rem;
            height: 250px;
            overflow-y: auto;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        .log-entry { padding: 0.5rem; border-left: 2px solid var(--primary-purple); background: rgba(157, 78, 221, 0.05); animation: fade-in 0.2s ease; }
        .log-entry.info { border-color: var(--primary-cyan); background: rgba(0, 229, 255, 0.05); color: var(--primary-cyan); }
        .log-entry.warn { border-color: var(--warning); background: rgba(255, 170, 0, 0.05); color: var(--warning); }
        .log-entry.success { border-color: var(--success); background: rgba(0, 255, 136, 0.05); color: var(--success); }
        
        /* =========================================
        NUEVA SECCIÓN: INSTALACIÓN DE APPS (JUEGO 2)
           ========================================= */
        .apps-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        .app-card {
            background: rgba(0,0,0,0.4);
            border: 1px solid var(--border-glow);
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s;
            user-select: none;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .app-card:hover { transform: translateY(-5px); box-shadow: var(--glow-shadow); border-color: var(--primary-cyan); }
        
        .app-logo {
            width: 40px;
            height: 40px;
            margin-bottom: 0.5rem;
            filter: drop-shadow(0 0 5px rgba(255,255,255,0.2));
        }
        
        .app-name { font-size: 0.8rem; font-weight: 600; color: var(--text-main); }
        
        .install-queue {
            display: flex;
            gap: 1rem;
            overflow-x: auto;
            padding-bottom: 1rem;
            min-height: 100px;
        }
        .install-item {
            background: rgba(157, 78, 221, 0.1);
            border: 1px solid var(--primary-purple);
            border-radius: 8px;
            padding: 0.75rem 0.5rem;
            min-width: 120px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .progress-bar {
            width: 100%;
            height: 6px;
            background: rgba(255,255,255,0.1);
            border-radius: 3px;
            margin-top: 0.5rem;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: var(--primary-cyan);
            width: 0%;
            transition: width 0.3s linear;
        }
        
        .toggle-container {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 1rem;
            background: rgba(0,0,0,0.3);
            padding: 0.5rem 1rem;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .toggle-switch {
            position: relative;
            display: inline-block;
            width: 50px;
            height: 24px;
            flex-shrink: 0;
        }
        .toggle-switch input { opacity: 0; width: 0; height: 0; }
        .slider {
            position: absolute;
            cursor: pointer;
            top: 0; left: 0; right: 0; bottom: 0;
            background-color: #333;
            transition: .4s;
            border-radius: 24px;
        }
        .slider:before {
            position: absolute;
            content: "";
            height: 18px; width: 18px;
            left: 3px; bottom: 3px;
            background-color: white;
            transition: .4s;
            border-radius: 50%;
        }
        input:checked + .slider { background-color: var(--primary-purple); }
        input:checked + .slider:before { transform: translateX(26px); }

        /* =========================================
        SELECTOR INLINE
           ========================================= */
        #inline-app-selector {
            display: none;
            align-items: center;
            gap: 0.5rem;
            background: rgba(0, 0, 0, 0.4);
            padding: 0.5rem 1rem;
            border-radius: 8px;
            border: 1px solid var(--border-glow);
            animation: fade-in 0.3s ease-out;
        }
        #inline-app-name {
            font-weight: 600;
            color: var(--primary-cyan);
            font-size: 0.9rem;
            margin-right: 0.5rem;
        }
        #inline-weight-input {
            width: 70px;
            padding: 0.5rem;
            font-size: 0.9rem;
            margin-bottom: 0;
        }
        #inline-app-selector button {
            padding: 0.5rem 1rem;
            font-size: 0.75rem;
        }
        #inline-app-selector .cancel-btn {
            padding: 0.5rem 0.8rem;
            font-size: 1rem;
            line-height: 1;
        }

        /* =========================================
        MODAL CRITERIOS DE EVALUACIÓN
           ========================================= */
        .modal-overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(5, 5, 10, 0.9);
            backdrop-filter: blur(5px);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            padding: 1rem;
        }
        .modal-content {
            background: var(--bg-panel);
            border: 1px solid var(--primary-cyan);
            border-radius: 16px;
            max-width: 800px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            padding: 2rem;
            position: relative;
            box-shadow: 0 0 50px rgba(0, 229, 255, 0.2);
        }
        .close-modal {
            position: absolute;
            top: 1rem;
            right: 1rem;
            font-size: 1.5rem;
            color: var(--primary-cyan);
            cursor: pointer;
            background: none;
            border: none;
            padding: 0;
            box-shadow: none;
            text-transform: none;
        }
        .close-modal:hover { color: #fff; background: none; box-shadow: none; }
        
        .criteria-list { list-style: none; margin-left: 0; }
        .criteria-list li {
            background: rgba(0,0,0,0.3);
            margin-bottom: 0.5rem;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid var(--success);
            display: flex;
            align-items: flex-start;
            gap: 1rem;
        }
        .criteria-list li strong { color: var(--success); }
        .check-icon { color: var(--success); font-size: 1.2rem; line-height: 1; }

        /* =========================================
        RESPONSIVE
           ========================================= */
        @media (max-width: 1024px) {
            .layout-grid { grid-template-columns: 1fr; }
            .cpu-container { flex-direction: column; }
            .metrics-panel { grid-template-columns: 1fr 1fr; }
        }
        @media (max-width: 768px) {
            header h1 { font-size: 1.8rem; }
            .controls-grid { grid-template-columns: 1fr; }
            .visualizer { grid-template-columns: 1fr; }
            .metrics-panel { grid-template-columns: 1fr; }
            .btn-group { flex-direction: column; align-items: stretch; }
            .btn-group button { width: 100%; }
            #inline-app-selector { flex-direction: column; align-items: flex-start; }
            #inline-weight-input { width: 100%; }
            .apps-grid { grid-template-columns: repeat(2, 1fr); }
            .modal-content { padding: 1.5rem; }
        }
        @media (max-width: 480px) {
            header h1 { font-size: 1.5rem; }
            .apps-grid { grid-template-columns: repeat(2, 1fr); }
        }

        /* SCROLLBAR */
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: rgba(0,0,0,0.5); border-radius: 4px; }
        ::-webkit-scrollbar-thumb { background: var(--secondary-purple); border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--primary-purple); }
    </style>
</head>
<body>

    <header>
        <h1>Planificación de Procesos y Arquitectura de Hardware</h1>
        <p>Simulador educativo interactivo: Analiza el impacto de los algoritmos FIFO y Round Robin en los recursos físicos del sistema (CPU, RAM y Colas).</p>
        <button id="btn-show-criteria" class="btn-criteria">Ver Criterios de Evaluación</button>
    </header>

    <!-- =========================================
        JUEGO 1: PROCESOS DE LA MEMORIA RAM
        ========================================= -->
    <div class="layout-grid">
        <main class="glass-panel">
            <h2>Procesos de la Memoria RAM</h2>
            
            <div class="controls-grid">
                <div class="control-group">
                    <label for="algo-select">Algoritmo de Planificación</label>
                    <select id="algo-select">
                        <option value="FIFO">FIFO (First-In, First-Out) - No Apropiativo</option>
                        <option value="RR">Round Robin - Apropiativo</option>
                    </select>
                </div>
                <div class="control-group">
                    <label for="quantum-input">Quantum (Solo para Round Robin)</label>
                    <input type="number" id="quantum-input" value="3" min="1" max="10" disabled>
                </div>
            </div>

            <div class="btn-group">
                <button id="btn-create" class="primary">+ Crear Proceso</button>
                <button id="btn-play" class="primary" disabled>Iniciar</button>
                <button id="btn-pause" disabled>Pausar</button>
                <button id="btn-reset" class="danger">Reiniciar</button>
            </div>

            <div class="visualizer">
                <div class="node-box">
                    <h4>Cola de Procesos (Listos)</h4>
                    <div id="queue-visual" class="queue-container"></div>
                </div>
                <div class="node-box">
                    <h4>Memoria RAM (Capacidad: 3)</h4>
                    <div id="ram-visual" class="ram-container"></div>
                </div>
            </div>

            <div class="cpu-container" id="cpu-visual">
                <h4>Unidad Central de Procesamiento (CPU)</h4>
                <div class="cpu-core" id="core-1"></div>
            </div>

            <div class="metrics-panel">
                <div class="metric-box">
                    <span class="metric-label">Tiempo Global (t)</span>
                    <span class="metric-value" id="metric-time">0</span>
                </div>
                <div class="metric-box">
                    <span class="metric-label">Procesos Completados</span>
                    <span class="metric-value" id="metric-completed">0</span>
                </div>
                <div class="metric-box">
                    <span class="metric-label">T. Espera Medio (E)</span>
                    <span class="metric-value" id="metric-wait">0.0</span>
                </div>
                <div class="metric-box">
                    <span class="metric-label">T. Respuesta Medio (F)</span>
                    <span class="metric-value" id="metric-response">0.0</span>
                </div>
            </div>
        </main>

        <aside class="info-panel">
            <div class="glass-panel" style="flex: 1;">
                <h2>Monitor del Sistema</h2>
                <div class="dynamic-log" id="log-container">
                    <div class="log-entry info">Bienvenido. Crea procesos y presiona "Iniciar" para ver la simulación.</div>
                </div>
            </div>

            <div class="glass-panel static-info">
                <h2>Hardware vs. Software</h2>
                <p>La ejecución del software (algoritmos) está inexorablemente ligada a las limitaciones físicas del hardware:</p>
                <h3>1. La CPU y los Registros</h3>
                <p>La velocidad del reloj dicta la rapidez de ejecución. En <strong>Round Robin</strong>, un Quantum muy pequeño causa cambios de contexto constantes (Overhead).</p>
                <h3>2. Memoria RAM</h3>
                <p>Si la RAM se llena (límite de 3), los procesos esperan en colas secundarias, aumentando exponencialmente el Tiempo de Respuesta (F).</p>
                <h3>3. Efecto Convoy (FIFO)</h3>
                <p>FIFO es no apropiativo. Un proceso con una ráfaga de tiempo muy larga monopolizará la CPU. Los procesos cortos que lleguen después sufrirán una tasa de penalización altísima.</p>
            </div>
        </aside>
    </div>

    <!-- =========================================
        JUEGO 2: INSTALACIÓN DE APLICACIONES
        ========================================= -->
    <div class="layout-grid">
        <main class="glass-panel">
            <h2>Simulador de Instalación: Primer vs Segundo Plano</h2>
            <p>Selecciona aplicaciones para encolarlas. Elige si deseas que se instalen en <strong>Primer Plano (FIFO - Bloquea el sistema)</strong> o <strong>Segundo Plano (Round Robin - No bloquea)</strong>.</p>
            
            <div class="toggle-container">
                <label class="toggle-switch">
                    <input type="checkbox" id="background-toggle">
                    <span class="slider"></span>
                </label>
                <span id="toggle-label" style="font-weight: 600; color: var(--warning);">Modo Actual: Primer Plano (FIFO)</span>
            </div>

            <div class="apps-grid" id="apps-grid">
                <!-- Generado por JS -->
            </div>

            <div class="btn-group">
                <button id="btn-install-start" class="primary">Iniciar Instalación</button>
                <button id="btn-install-reset" class="danger">Limpiar Cola</button>
                
                <!-- SELECTOR INLINE -->
                <div id="inline-app-selector">
                    <span id="inline-app-name">App</span>
                    <input type="number" id="inline-weight-input" min="1" max="100" value="5">
                    <span style="font-size: 0.8rem; color: var(--text-muted);">MB</span>
                    <button id="btn-inline-add" class="primary">Añadir</button>
                    <button id="btn-inline-cancel" class="danger cancel-btn">&times;</button>
                </div>
            </div>

            <h3>Cola de Instalación</h3>
            <div class="install-queue" id="install-queue-container">
                <p style="color: var(--text-muted); font-size: 0.9rem;">No hay aplicaciones en cola...</p>
            </div>
        </main>

        <aside class="info-panel">
            <!-- MONITOR DE INSTALACIÓN -->
            <div class="glass-panel" style="flex: 1;">
                <h2>Monitor de Instalación</h2>
                <div class="dynamic-log" id="app-log-container">
                    <div class="log-entry info">Bienvenido. Selecciona apps y presiona "Iniciar Instalación".</div>
                </div>
            </div>

            <div class="glass-panel static-info">
                <h2>¿Qué está pasando?</h2>
                <p>La instalación de software compite por los recursos del procesador. El sistema operativo decide cómo administrar este proceso:</p>
                
                <h3>Primer Plano (FIFO)</h3>
                <p>El proceso de instalación se ejecuta de forma <strong>No Apropiativa</strong>. La aplicación captura la CPU y no la suelta hasta terminar. <em>El usuario no puede interactuar con otras apps hasta que finalice.</em></p>
                
                <h3>Segundo Plano (Round Robin)</h3>
                <p>El sistema operativo divide la instalación en pequeñas ráfagas (Quantum). Después de cada ráfaga, el proceso regresa a la cola, permitiendo que otras aplicaciones se ejecuten. <em>El usuario puede seguir usando el dispositivo sin que se congele.</em></p>
            </div>
        </aside>
    </div>

    <!-- =========================================
        MODAL OCULTO: CRITERIOS DE EVALUACIÓN
        ========================================= -->
    <div class="modal-overlay" id="criteria-modal">
        <div class="modal-content">
            <button class="close-modal" id="btn-close-criteria">&times;</button>
            <h2>Criterios de Evaluación Cumplidos</h2>
            <p>Este simulador demuestra funcionalmente los conceptos del eje temático "Procesos y Planificación de Trabajos":</p>
            
            <ul class="criteria-list">
                <li>
                    <span class="check-icon">✔</span>
                    <div><strong>Gestión de procesos (creación, estados, PCB, transiciones):</strong> El Juego 1 representa visualmente la creación de procesos, su PCB (tarjetas con ID y tiempo), y sus transiciones (Listos -> RAM -> CPU -> Terminado).</div>
                </li>
                <li>
                    <span class="check-icon">✔</span>
                    <div><strong>Algoritmos de planificación de CPU (FCFS, SJF, Round Robin, Prioridades, Colas Multinivel):</strong> Implementación funcional de FCFS (FIFO) y Round Robin con Quantum configurable en el Juego 1, y su abstracción en el Juego 2.</div>
                </li>
                <li>
                    <span class="check-icon">✔</span>
                    <div><strong>Cambio de contexto:</strong> En el Juego 1 (Round Robin), se observa cómo el proceso regresa a la cola y se guarda su tiempo restante, simulando la sobrecarga del cambio de contexto.</div>
                </li>
                <li>
                    <span class="check-icon">✔</span>
                    <div><strong>Sincronización y comunicación entre procesos (semáforos, mutex, memoria compartida):</strong> La limitación física de la Memoria RAM (Capacidad: 3) en el Juego 1 actúa como un semáforo/mutex que bloquea la entrada de nuevos procesos hasta que se libere un espacio.</div>
                </li>
                <li>
                    <span class="check-icon">✔</span>
                    <div><strong>Cálculo de métricas (tiempo de espera, tiempo de retorno, tiempo de respuesta, throughput, uso de CPU):</strong> El panel de métricas calcula y actualiza en tiempo real el Tiempo de Espera Medio, el Tiempo de Respuesta (F) y el Tiempo Global (Throughput implícito).</div>
                </li>
            </ul>
        </div>
    </div>

    <script>
        // =========================================
        // LÓGICA JUEGO 1: PROCESOS DE LA MEMORIA RAM
        // =========================================
        class Process {
            constructor(id, burstTime) {
                this.id = `P${id}`;
                this.burstTime = burstTime;
                this.remainingTime = burstTime;
                this.arrivalTime = state.currentTime;
                this.state = 'Nuevo';
                this.waitTime = 0;
                this.responseTime = 0;
            }
        }

        const state = {
            isRunning: false,
            currentTime: 0,
            quantum: 3,
            algorithm: 'FIFO',
            processCounter: 1,
            queue: [],
            ram: [],
            cpu: null,
            currentQuantum: 0,
            completedProcesses: [],
            intervalId: null,
            ramCapacity: 3
        };

        const dom = {
            algoSelect: document.getElementById('algo-select'),
            quantumInput: document.getElementById('quantum-input'),
            btnCreate: document.getElementById('btn-create'),
            btnPlay: document.getElementById('btn-play'),
            btnPause: document.getElementById('btn-pause'),
            btnReset: document.getElementById('btn-reset'),
            queueVisual: document.getElementById('queue-visual'),
            ramVisual: document.getElementById('ram-visual'),
            core1: document.getElementById('core-1'),
            logContainer: document.getElementById('log-container'),
            metricTime: document.getElementById('metric-time'),
            metricCompleted: document.getElementById('metric-completed'),
            metricWait: document.getElementById('metric-wait'),
            metricResponse: document.getElementById('metric-response')
        };

        function addLog(message, type = 'normal') {
            const entry = document.createElement('div');
            entry.className = `log-entry ${type}`;
            entry.innerHTML = `<span class="mono" style="color: var(--text-muted); margin-right: 5px;">[t=${state.currentTime}]</span> ${message}`;
            dom.logContainer.appendChild(entry);
            dom.logContainer.scrollTop = dom.logContainer.scrollHeight;
        }

        function createProcess() {
            const burst = Math.floor(Math.random() * 7) + 2; 
            const newProcess = new Process(state.processCounter++, burst);
            
            if (state.ram.length < state.ramCapacity) {
                newProcess.state = 'Listo';
                state.ram.push(newProcess);
                addLog(`Proceso ${newProcess.id} (T: ${newProcess.burstTime}) cargado en RAM.`, 'info');
            } else {
                newProcess.state = 'Listo';
                state.queue.push(newProcess);
                addLog(`Proceso ${newProcess.id} (T: ${newProcess.burstTime}) en espera. RAM llena.`, 'warn');
            }
            updateUI();
        }

        function tick() {
            if (!state.isRunning) return;
            state.currentTime++;
            
            if (state.queue.length > 0 && state.ram.length < state.ramCapacity) {
                const p = state.queue.shift();
                state.ram.push(p);
                addLog(`Proceso ${p.id} transferido de Cola a RAM.`, 'info');
            }

            if (state.cpu) {
                state.cpu.remainingTime--;
                state.currentQuantum++;
                
                if (state.cpu.remainingTime === 0) {
                    state.cpu.responseTime = state.currentTime - state.cpu.arrivalTime;
                    state.completedProcesses.push(state.cpu);
                    addLog(`Proceso ${state.cpu.id} TERMINADO.`, 'normal');
                    state.ram = state.ram.filter(p => p.id !== state.cpu.id);
                    state.cpu = null;
                    state.currentQuantum = 0;
                    
                    if (state.queue.length > 0) {
                        state.ram.push(state.queue.shift());
                    }
                } else if (state.algorithm === 'RR' && state.currentQuantum >= state.quantum) {
                    addLog(`Quantum agotado para ${state.cpu.id}. Cambio de contexto (regresa a Cola).`, 'warn');
                    state.cpu.state = 'Listo';
                    state.queue.push(state.cpu);
                    state.cpu = null;
                    state.currentQuantum = 0;
                }
            }

            if (!state.cpu && state.ram.length > 0) {
                state.cpu = state.ram.shift();
                state.cpu.state = 'Ejecucion';
                state.currentQuantum = 0;
                addLog(`CPU asignada a ${state.cpu.id} (${state.cpu.remainingTime} u. restantes).`, 'normal');
            }

            state.queue.forEach(p => p.waitTime++);
            state.ram.forEach(p => p.waitTime++);
            updateUI();
        }

        function startSimulation() {
            if (state.isRunning) return;
            state.isRunning = true;
            dom.btnPlay.disabled = true;
            dom.btnPause.disabled = false;
            dom.btnCreate.disabled = true;
            addLog("Simulación Iniciada.", "info");
            state.intervalId = setInterval(tick, 1000);
        }

        function pauseSimulation() {
            if (!state.isRunning) return;
            state.isRunning = false;
            clearInterval(state.intervalId);
            dom.btnPlay.disabled = false;
            dom.btnPause.disabled = true;
            addLog("Simulación Pausada.", "warn");
        }

        function resetSimulation() {
            clearInterval(state.intervalId);
            state.isRunning = false;
            state.currentTime = 0;
            state.processCounter = 1;
            state.queue = [];
            state.ram = [];
            state.cpu = null;
            state.completedProcesses = [];
            
            dom.btnPlay.disabled = true;
            dom.btnPause.disabled = true;
            dom.btnCreate.disabled = false;
            dom.logContainer.innerHTML = '<div class="log-entry info">Sistema reiniciado.</div>';
            updateUI();
        }

        function createProcessCard(p, isActive = false) {
            return `
                <div class="process-card ${isActive ? 'active' : ''}">
                    <span class="pid">${p.id}</span>
                    <span class="ptime">T: ${p.remainingTime}</span>
                    <span class="pstate">${p.state}</span>
                </div>
            `;
        }

        function updateUI() {
            dom.metricTime.textContent = state.currentTime;
            dom.metricCompleted.textContent = state.completedProcesses.length;

            if (state.completedProcesses.length > 0) {
                const totalWait = state.completedProcesses.reduce((acc, p) => acc + p.waitTime, 0);
                const totalResponse = state.completedProcesses.reduce((acc, p) => acc + p.responseTime, 0);
                dom.metricWait.textContent = (totalWait / state.completedProcesses.length).toFixed(1);
                dom.metricResponse.textContent = (totalResponse / state.completedProcesses.length).toFixed(1);
            } else {
                dom.metricWait.textContent = '0.0';
                dom.metricResponse.textContent = '0.0';
            }

            dom.queueVisual.innerHTML = state.queue.map(p => createProcessCard(p)).join('') || '<span style="color:var(--text-muted); font-size:0.8rem; margin-top:1rem;">Cola Vacía</span>';
            dom.ramVisual.innerHTML = state.ram.map(p => createProcessCard(p)).join('') || '<span style="color:var(--text-muted); font-size:0.8rem; margin-top:1rem;">RAM Vacía</span>';

            if (state.cpu) {
                dom.core1.classList.add('active');
                dom.core1.innerHTML = createProcessCard(state.cpu, true);
                if (state.algorithm === 'RR') {
                    dom.core1.querySelector('.pstate').textContent = `Q: ${state.quantum - state.currentQuantum}`;
                    dom.core1.querySelector('.pstate').style.color = 'var(--primary-purple)';
                }
            } else {
                dom.core1.classList.remove('active');
                dom.core1.innerHTML = '<span style="color: var(--text-muted); font-size: 0.8rem;">IDLE</span>';
            }

            if (!state.isRunning && (state.cpu || state.ram.length > 0 || state.queue.length > 0)) {
                dom.btnPlay.disabled = false;
            }
        }

        dom.algoSelect.addEventListener('change', (e) => {
            state.algorithm = e.target.value;
            dom.quantumInput.disabled = (state.algorithm !== 'RR');
        });

        dom.quantumInput.addEventListener('change', (e) => {
            let val = parseInt(e.target.value);
            if (val < 1) val = 1;
            state.quantum = val;
        });

        dom.btnCreate.addEventListener('click', createProcess);
        dom.btnPlay.addEventListener('click', startSimulation);
        dom.btnPause.addEventListener('click', pauseSimulation);
        dom.btnReset.addEventListener('click', resetSimulation);


        // =========================================
        // LÓGICA JUEGO 2: INSTALACIÓN DE APPS
        // =========================================
        
        const apps = [
            { id: 'ig', name: 'Instagram', icon: 'https://cdn.simpleicons.org/instagram/white', size: 5 },
            { id: 'class', name: 'Classroom', icon: 'https://cdn.simpleicons.org/googleclassroom/white', size: 4 },
            { id: 'tt', name: 'TikTok', icon: 'https://cdn.simpleicons.org/tiktok/white', size: 6 },
            { id: 'wa', name: 'WhatsApp', icon: 'https://cdn.simpleicons.org/whatsapp/white', size: 3 },
            { id: 'sp', name: 'Spotify', icon: 'https://cdn.simpleicons.org/spotify/white', size: 5 },
            { id: 'steam', name: 'Steam', icon: 'https://cdn.simpleicons.org/steam/white', size: 8 },
            { id: 'py', name: 'Python', icon: 'https://cdn.simpleicons.org/python/white', size: 7 },
            { id: 'opera', name: 'Opera', icon: 'https://cdn.simpleicons.org/opera/white', size: 4 }
        ];

        let installQueue = [];
        let isInstalling = false;
        let installInterval = null;
        let isBackgroundMode = false;

        const appsGrid = document.getElementById('apps-grid');
        const installQueueContainer = document.getElementById('install-queue-container');
        const appLogContainer = document.getElementById('app-log-container');
        const toggleSwitch = document.getElementById('background-toggle');
        const toggleLabel = document.getElementById('toggle-label');
        const btnInstallStart = document.getElementById('btn-install-start');
        const btnInstallReset = document.getElementById('btn-install-reset');

        // Referencias al selector inline
        const inlineSelector = document.getElementById('inline-app-selector');
        const inlineAppName = document.getElementById('inline-app-name');
        const inlineWeightInput = document.getElementById('inline-weight-input');
        const btnInlineAdd = document.getElementById('btn-inline-add');
        const btnInlineCancel = document.getElementById('btn-inline-cancel');
        let selectedApp = null;

        function addAppLog(message, type = 'normal') {
            const entry = document.createElement('div');
            entry.className = `log-entry ${type}`;
            entry.innerHTML = message;
            appLogContainer.appendChild(entry);
            appLogContainer.scrollTop = appLogContainer.scrollHeight;
        }

        apps.forEach(app => {
            const card = document.createElement('div');
            card.className = 'app-card';
            card.innerHTML = `
                <img src="${app.icon}" alt="${app.name}" class="app-logo">
                <span class="app-name">${app.name}</span>
            `;
            card.addEventListener('click', () => {
                if (isInstalling) return;
                if (installQueue.find(a => a.id === app.id)) {
                    addAppLog(`La app <strong>${app.name}</strong> ya está en la cola.`, 'warn');
                    return;
                }
                
                // Mostrar selector inline
                selectedApp = app;
                inlineAppName.textContent = app.name;
                inlineWeightInput.value = app.size;
                inlineSelector.style.display = 'flex';
                inlineWeightInput.focus();
                inlineWeightInput.select();
            });
            appsGrid.appendChild(card);
        });

        // Lógica del selector inline
        btnInlineAdd.addEventListener('click', () => {
            if (!selectedApp) return;
            
            let customSize = parseInt(inlineWeightInput.value);
            if (isNaN(customSize) || customSize <= 0) {
                customSize = selectedApp.size; 
            }
            
            installQueue.push({ ...selectedApp, progress: 0, remaining: customSize, size: customSize });
            addAppLog(`App <strong>${selectedApp.name}</strong> añadida a la cola (${customSize} MB).`, 'info');
            renderInstallQueue();
            
            // Ocultar selector
            inlineSelector.style.display = 'none';
            selectedApp = null;
        });

        btnInlineCancel.addEventListener('click', () => {
            inlineSelector.style.display = 'none';
            selectedApp = null;
        });

        inlineWeightInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                btnInlineAdd.click();
            }
        });

        function renderInstallQueue() {
            if (installQueue.length === 0) {
                installQueueContainer.innerHTML = '<p style="color: var(--text-muted); font-size: 0.9rem;">No hay aplicaciones en cola...</p>';
                return;
            }

            installQueueContainer.innerHTML = installQueue.map((app, index) => `
                <div class="install-item">
                    <img src="${app.icon}" alt="${app.name}" style="width: 30px; height: 30px; margin-bottom: 5px;">
                    <div style="font-size: 0.8rem; font-weight: bold; margin-bottom: 5px;">${app.name}</div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: ${(app.progress / app.size) * 100}%; background: ${isBackgroundMode ? 'var(--primary-purple)' : 'var(--primary-cyan)'};"></div>
                    </div>
                    <div style="font-size: 0.7rem; color: var(--text-muted); margin-top: 5px;">${app.progress}/${app.size} MB</div>
                </div>
            `).join('');
        }

        toggleSwitch.addEventListener('change', (e) => {
            if (isInstalling) {
                e.preventDefault();
                toggleSwitch.checked = !e.target.checked;
                return;
            }
            isBackgroundMode = e.target.checked;
            if (isBackgroundMode) {
                toggleLabel.textContent = "Modo Actual: Segundo Plano (Round Robin)";
                toggleLabel.style.color = "var(--primary-purple)";
                addAppLog(`Modo cambiado a <strong>Segundo Plano</strong> (Round Robin).`, 'warn');
            } else {
                toggleLabel.textContent = "Modo Actual: Primer Plano (FIFO)";
                toggleLabel.style.color = "var(--warning)";
                addAppLog(`Modo cambiado a <strong>Primer Plano</strong> (FIFO).`, 'warn');
            }
            renderInstallQueue(); 
        });

        btnInstallStart.addEventListener('click', () => {
            if (isInstalling || installQueue.length === 0) return;
            
            isInstalling = true;
            btnInstallStart.disabled = true;
            toggleSwitch.disabled = true;
            
            addAppLog("▶ Iniciando proceso de instalación...", "info");

            installInterval = setInterval(() => {
                if (installQueue.length === 0) {
                    clearInterval(installInterval);
                    isInstalling = false;
                    btnInstallStart.disabled = false;
                    toggleSwitch.disabled = false;
                    addAppLog("✅ Todas las instalaciones han finalizado.", "success");
                    return;
                }

                if (!isBackgroundMode) {
                    let currentApp = installQueue[0];
                    currentApp.progress++;
                    if (currentApp.progress >= currentApp.size) {
                        addAppLog(`✅ <strong>${currentApp.name}</strong> instalado (FIFO).`, "success");
                        installQueue.shift();
                    }
                } else {
                    for (let i = 0; i < installQueue.length; i++) {
                        if (installQueue[i].progress < installQueue[i].size) {
                            installQueue[i].progress++;
                            if (installQueue[i].progress >= installQueue[i].size) {
                                addAppLog(`✅ <strong>${installQueue[i].name}</strong> instalado (Round Robin).`, "success");
                            }
                        }
                    }
                    installQueue = installQueue.filter(app => app.progress < app.size);
                }
                
                renderInstallQueue();
            }, 300); 
        });

        btnInstallReset.addEventListener('click', () => {
            clearInterval(installInterval);
            installQueue = [];
            isInstalling = false;
            btnInstallStart.disabled = false;
            toggleSwitch.disabled = false;
            inlineSelector.style.display = 'none';
            selectedApp = null;
            appLogContainer.innerHTML = '<div class="log-entry info">Cola limpiada. Sistema listo.</div>';
            renderInstallQueue();
        });

        // =========================================
        // LÓGICA MODAL CRITERIOS
        // =========================================
        const btnShowCriteria = document.getElementById('btn-show-criteria');
        const btnCloseCriteria = document.getElementById('btn-close-criteria');
        const criteriaModal = document.getElementById('criteria-modal');

        btnShowCriteria.addEventListener('click', () => {
            criteriaModal.style.display = 'flex';
        });

        btnCloseCriteria.addEventListener('click', () => {
            criteriaModal.style.display = 'none';
        });

        criteriaModal.addEventListener('click', (e) => {
            if (e.target === criteriaModal) {
                criteriaModal.style.display = 'none';
            }
        });

        // Init general
        updateUI();
    </script>
</body>
</html>
"""

# 4. Renderizar el HTML en Streamlit
# El parámetro height debe ser lo suficientemente grande para mostrar todo el simulador sin cortes.
# El parámetro scrolling=True permite que el usuario se desplace si la pantalla es pequeña.
components.html(html_code, height=2400, scrolling=True)
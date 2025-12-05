<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatórios de Ponto</title>
    <link rel="stylesheet" href="/static/css/relatorios.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="header-content">
                <h1>Relatórios de Ponto</h1>
                <p>Acompanhe o fluxo de chegada e saída em tempo real</p>
            </div>
            <div class="header-actions">
                <button class="btn-filtros">
                    <span>⚙️</span> Filtros
                </button>
                <button class="btn-exportar">
                    <span>⬇️</span> Exportar
                </button>
            </div>
        </header>

        <!-- Metrics Cards -->
        <section class="metrics">
            <div class="metric-card">
                <div class="metric-header">
                    <h3>Trabalhadores Presentes</h3>
                    <div class="metric-icon">👥</div>
                </div>
                <div class="metric-value">142</div>
                <div class="metric-change positive">
                    <span>↑ +12%</span>
                    <span>vs. ontem</span>
                </div>
            </div>

            <div class="metric-card">
                <div class="metric-header">
                    <h3>Chegadas no Horário</h3>
                    <div class="metric-icon">👥</div>
                </div>
                <div class="metric-value">89%</div>
                <div class="metric-change positive">
                    <span>↑ +5%</span>
                    <span>taxa de pontualidade</span>
                </div>
            </div>

            <div class="metric-card">
                <div class="metric-header">
                    <h3>Tempo Médio de Chegada</h3>
                    <div class="metric-icon">🕐</div>
                </div>
                <div class="metric-value">08:07</div>
                <div class="metric-change negative">
                    <span>↓ -3 min</span>
                    <span>horário médio</span>
                </div>
            </div>

            <div class="metric-card">
                <div class="metric-header">
                    <h3>Ausências</h3>
                    <div class="metric-icon">👥</div>
                </div>
                <div class="metric-value">8</div>
                <div class="metric-change negative">
                    <span>↓ -2</span>
                    <span>vs. ontem</span>
                </div>
            </div>
        </section>

        <!-- Charts Section -->
        <section class="charts-section">
            <div class="chart-container">
                <h2>Fluxo de Chegada e Saída</h2>
                <p>Visualização em tempo real dos registros de ponto</p>
                <canvas id="fluxoChart"></canvas>
            </div>

            <div class="chart-container">
                <h2>Presença por Departamento</h2>
                <p>Distribuição dos trabalhadores presentes</p>
                <div class="chart-wrapper">
                    <canvas id="departamentoChart"></canvas>
                    <div class="chart-legend">
                        <div class="legend-item">
                            <span class="legend-label">Produção</span>
                            <span class="legend-value">45%</span>
                        </div>
                        <div class="legend-item">
                            <span class="legend-label">Administrativo</span>
                            <span class="legend-value">28%</span>
                        </div>
                        <div class="legend-item">
                            <span class="legend-label">Logística</span>
                            <span class="legend-value">18%</span>
                        </div>
                        <div class="legend-item">
                            <span class="legend-label">Manutenção</span>
                            <span class="legend-value">12%</span>
                        </div>
                        <div class="legend-item">
                            <span class="legend-label">Outros</span>
                            <span class="legend-value">8%</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Recent Activity -->
        <section class="activity-section">
            <h2>Atividade Recente</h2>
            <p>Últimos registros de ponto realizados</p>
            
            <div class="activity-list">
                <div class="activity-item">
                    <div class="activity-avatar">JS</div>
                    <div class="activity-info">
                        <div class="activity-name">João Silva</div>
                        <div class="activity-department">Produção</div>
                    </div>
                    <div class="activity-time">08:02</div>
                    <div class="activity-status">No horário</div>
                </div>

                <div class="activity-item">
                    <div class="activity-avatar ms">MS</div>
                    <div class="activity-info">
                        <div class="activity-name">Maria Santos</div>
                        <div class="activity-department">Administrativo</div>
                    </div>
                    <div class="activity-time">17:45</div>
                    <div class="activity-status">No horário</div>
                </div>

                <div class="activity-item">
                    <div class="activity-avatar po">PO</div>
                    <div class="activity-info">
                        <div class="activity-name">Pedro Oliveira</div>
                        <div class="activity-department">Logística</div>
                    </div>
                    <div class="activity-time">08:15</div>
                    <div class="activity-status delayed">Atrasado</div>
                </div>

                <div class="activity-item">
                    <div class="activity-avatar ac">AC</div>
                    <div class="activity-info">
                        <div class="activity-name">Ana Costa</div>
                        <div class="activity-department">Manutenção</div>
                    </div>
                    <div class="activity-time">07:58</div>
                    <div class="activity-status">Adiantado</div>
                </div>
            </div>
        </section>
    </div>

    <script src="/static/js/relatorios.js"></script>
</body>
</html>
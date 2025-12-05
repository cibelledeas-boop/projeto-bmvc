<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registros de Pontualidade</title>
    <link rel="stylesheet" href="/static/css/registers.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
</head>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registros de Pontualidade</title>
    <link rel="stylesheet" href="/static/css/registers.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="dashboard">  
            <div class="section">
                <h2 class="section-title">Assiduidade do Mês</h2>
                <div class="chart-container">
                    <canvas id="attendanceChart"></canvas>
                </div>
            </div> 
            <div class="section">
                <h2 class="section-title">Últimos Registros</h2>
                <div class="records-list">
                    <div class="record-item">
                        <span class="record-date">Hoje</span>
                        <span class="record-time">08:00 - 17:30</span>
                    </div>
                    <div class="record-item">
                        <span class="record-date">Ontem</span>
                        <span class="record-time">08:05 - 17:35</span>
                    </div>
                    <div class="record-item">
                        <span class="record-date">2 dias atrás</span>
                        <span class="record-time">08:10 - 18:00</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="/static/js/pagina.js"></script>
    <script>
        const ctx = document.getElementById('attendanceChart').getContext('2d');
        const chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
                datasets: [{
                    label: 'Horas',
                    data: [8, 8, 8, 8, 8, 0, 0],
                    backgroundColor: '#2196F3',
                    borderRadius: 8,
                    borderSkipped: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 10,
                        ticks: {
                            stepSize: 2
                        },
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
    </script>
</body>
</html>

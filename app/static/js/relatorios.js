
function initFluxoChart() {
    const ctx = document.getElementById('fluxoChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00'],
            datasets: [
                {
                    label: 'Chegadas',
                    data: [5, 45, 70, 50, 25, 15, 10, 30, 35, 40, 50, 60, 20],
                    borderColor: '#003d7a',
                    backgroundColor: 'rgba(0, 61, 122, 0.1)',
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0,
                    borderWidth: 2
                },
                {
                    label: 'Saídas',
                    backgroundColor: 'rgba(100, 150, 200, 0.1)',
                    data: [2, 25, 35, 30, 20, 12, 8, 20, 22, 28, 35, 40, 15],
                    borderColor: '#6496c8',
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0,
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'bottom',
                    labels: {
                        boxWidth: 12,
                        usePointStyle: true,
                        padding: 20,
                        font: {
                            size: 12,
                            weight: '600'
                        }
                    }
                },
                filler: {
                    propagate: true
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 80,
                    grid: {
                        drawBorder: false,
                        color: 'rgba(0, 0, 0, 0.05)'
                    },
                    ticks: {
                        font: {
                            size: 12
                        }
                    }
                },
                x: {
                    grid: {
                        display: false,
                        drawBorder: false
                    },
                    ticks: {
                        font: {
                            size: 12
                        }
                    }
                }
            }
        }
    });
}


function initDepartamentoChart() {
    const ctx = document.getElementById('departamentoChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Produção', 'Administrativo', 'Logística', 'Manutenção', 'Outros'],
            datasets: [
                {
                    data: [45, 28, 18, 12, 8],
                    backgroundColor: [
                        '#6c757d',
                        '#999999',
                        '#b3b3b3',
                        '#cccccc',
                        '#e6e6e6'
                    ],
                    borderColor: '#ffffff',
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.parsed + '%';
                        }
                    }
                }
            }
        }
    });
}


document.addEventListener('DOMContentLoaded', function() {
    initFluxoChart();
    initDepartamentoChart();

    const btnFiltros = document.querySelector('.btn-filtros');
    const btnExportar = document.querySelector('.btn-exportar');

    btnFiltros.addEventListener('click', function() {
        alert('Funcionalidade de filtros a ser implementada');
    });

    btnExportar.addEventListener('click', function() {
        alert('Funcionalidade de exportação a ser implementada');
    });

    const activityItems = document.querySelectorAll('.activity-item');
    activityItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.cursor = 'pointer';
        });
    });
});

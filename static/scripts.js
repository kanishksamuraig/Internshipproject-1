function showGraph(type) {
    const graphContainer = document.getElementById('graph-container');
    graphContainer.innerHTML = '';

    if (type === 'bar') {
        const trace = {
            x: hierarchyData.Level_2.map(d => d.Protocol),
            y: hierarchyData.Level_2.map(d => d.Frames),
            type: 'bar'
        };
        const data = [trace];
        Plotly.newPlot('graph-container', data);
    } else if (type === 'pie') {
        const trace = {
            labels: hierarchyData.Level_2.map(d => d.Protocol),
            values: hierarchyData.Level_2.map(d => d.Frames),
            type: 'pie'
        };
        const data = [trace];
        Plotly.newPlot('graph-container', data);
    }
}

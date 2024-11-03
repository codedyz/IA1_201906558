// Variables para almacenar los datos de entrenamiento
var xTrain = [];
var yTrain = [];
var yPredict = [];
var dataRows = [];
var dataGrades = [];
var selectedAlgorithm = "linear"; // Por defecto, Linear Regression

function updateAlgorithm() {
    selectedAlgorithm = document.getElementById("algorithmSelect").value;
    document.getElementById("gradeInput").value = '';
    document.getElementById("predict").disabled = true;
    document.getElementById("graph").disabled = true;

    if(selectedAlgorithm.toLowerCase() == "linear"){
        document.getElementById("params_poly").style.display = "none";

    }else if(selectedAlgorithm.toLowerCase() == "polynomial"){
        document.getElementById("params_poly").style.display = "block";
    }
}

function loadCSV() {
    xTrain = [];
    yTrain = [];
    yPredict = [];
    dataRows = [];
    dataGradesgrades = [];

    var fileInput = document.getElementById("csvFile");
    var file = fileInput.files[0];
    if (!file) {
        alert("Please upload a CSV file.");
        return;
    }
    document.getElementById("predict").disabled = false;

    var reader = new FileReader();
    reader.onload = function(event) {
        var csvData = event.target.result;
        processCSVData(csvData);
        populateTable(dataRows);
    };
    reader.readAsText(file);
    document.getElementById('csvFile').value = null;
}

function grades() {
    const inputValor = document.getElementById("gradeInput").value;

    const formatoValido = /^(\d+)(,\d+)*$/;

    if (!formatoValido.test(inputValor)) {
        alert("Formato inválido. Asegúrate de ingresar solo enteros separados por comas (ejemplo: 1,5,6)");
        return; 
    }

    const valores = inputValor.split(',').map(valor => parseInt(valor.trim()));
    
    // Agregar los valores al arreglo global
    dataGrades.unshift(...valores);

    // Mostrar el arreglo en la consola para verificar
    alert("Grado "+dataGrades[0]+ " cargado exitosamente")
    console.log(dataGrades);

}

function processCSVData(csvData) {
    var lines = csvData.trim().split("\n");
    if (lines.length < 2) {
        alert("CSV file must contain at least two rows: one for headers and one for data.");
        return;
    }

    // Obtener encabezados y verificar si son específicos
    var headers = lines[0].split(",").map(header => header.trim());
    var hasXTrain = headers.includes("XTrain");
    var hasYTrain = headers.includes("YTrain");

    var thead = document.getElementById("dataTable").getElementsByTagName("thead")[0];
    thead.innerHTML = ""; // Limpiar encabezados previos
    var headerRow = thead.insertRow();

    headers.forEach(function(header) {
        var th = document.createElement("th");
        th.textContent = header;
        headerRow.appendChild(th);
    });

    // Procesar las filas de datos (omitimos la primera línea de encabezados)
    dataRows = [];
    for (var i = 1; i < lines.length; i++) {
        var values = lines[i].split(",").map(parseFloat);
        if (values.length === headers.length) {
            dataRows.push(values);
            if (hasXTrain) xTrain.push(values[headers.indexOf("XTrain")]);
            if (hasYTrain) yTrain.push(values[headers.indexOf("YTrain")]);
        }
    }

}

function populateTable(dataRows) {
    var tbody = document.getElementById("dataTable").getElementsByTagName("tbody")[0];
    tbody.innerHTML = ""; // Limpiar cualquier dato previo
    dataRows.forEach(function(row) {
        var rowElement = tbody.insertRow();
        row.forEach(function(cellData) {
            var cell = rowElement.insertCell();
            cell.textContent = cellData;
        });
    });
}

function model_type() {
    const div2 = document.getElementById("resultsTable");
    div2.scrollIntoView({ behavior: "smooth" });
    if(selectedAlgorithm.toLowerCase() == "linear"){
        runLinearRegression()

    }else if(selectedAlgorithm.toLowerCase() == "polynomial"){
        runPolyRegression() 

    }
}

function runPolyRegression() {
    var poly = new PolynomialRegression();
    poly.fit(xTrain, yTrain,dataGrades[0]);
    yPredict = poly.predict(xTrain)
    var r2 = poly.getError();

    
    for (let i = 0; i < yPredict.length; i++) {
        yPredict[i] = Number(yPredict[i].toFixed(2));
    }
    document.getElementById("predict-title").innerHTML = `
    <th scope="col">Error</th>
    <th scope="col">YPredict</th>
    `;

    document.getElementById("resultsRow").innerHTML = `
        <td>${r2}</td>
        <td>${yPredict.join(", ")}</td>
    `;

    document.getElementById("graph").disabled = false;

}

// Ejecutar regresión lineal y mostrar los resultados
function runLinearRegression() {
    var linear = new LinearRegression();
    linear.fit(xTrain, yTrain);
    yPredict = linear.predict(xTrain);

    var msError = linear.mserror(yTrain,yPredict).toFixed(4)
    var pendiente = linear.m.toFixed(4)
    var punto = linear.b.toFixed(4)

    yPredict = yPredict.map(value => Number(value.toFixed(4)));
    xTrain = xTrain.map(value => Number(value.toFixed(4)));
    yTrain = yTrain.map(value => Number(value.toFixed(4)));
    document.getElementById("predict-title").innerHTML = `
    <th scope="col">Pendiente</th>
    <th scope="col">Intercepto</th>
    <th scope="col">Error</th>
    <th scope="col">YPredict</th>
    `;
    document.getElementById("resultsRow").innerHTML = `
        <td>${pendiente}</td>
        <td>${punto}</td>
        <td>${msError}</td>
        <td>${yPredict.join(", ")}</td>
    `;
    // Preparar datos para Google Charts

    document.getElementById("graph").disabled = false;

}

function callDraw() {
    const div2 = document.getElementById("chart_div");
    div2.scrollIntoView({ behavior: "smooth" });
    var a = joinArrays('x', xTrain, 'yTrain', yTrain, 'yPredict', yPredict);

    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(function() { drawChart(a); });
}

function drawChart(dataArray) {
    var data = google.visualization.arrayToDataTable(dataArray);
    var options = {
        seriesType: 'scatter',
        series: { 1: { type: 'line' } }
    };
    var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}

// https://www.chartjs.org/docs/latest/samples/bar/border-radius.html
//https://www.chartjs.org/samples/2.9.4/utils.js
'use strict';
// import colorLib from "@kurkle/color";


const CHART_COLORS = {
  red: 'rgb(255, 99, 132)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(75, 192, 192)',
  blue: 'rgb(54, 162, 235)',
  purple: 'rgb(153, 102, 255)',
  grey: 'rgb(201, 203, 207)'
};


// analysis by app
fetch('/dating_analysis_app.json')
  .then((response) => response.json())
  .then((responseJson) => {
    
    const data = {
      labels: Object.keys(responseJson.data),
      datasets: [
        {
          label: "You",
          data: Object.entries(responseJson.data).map(d => d[1].my_rating),
          borderColor: CHART_COLORS.grey,
          backgroundColor: CHART_COLORS.blue,
          borderWidth: 2,
          borderRadius: 5,
          borderSkipped: false,
        },
        {
          label: 'Other ppl',
          data: Object.entries(responseJson.data).map(d => d[1].other_ppl_rating),
          borderColor: CHART_COLORS.grey,
          backgroundColor: CHART_COLORS.yellow,
          borderWidth: 2,
          borderRadius: 5,
          borderSkipped: false,
        }
      ]
    };

  
  new Chart(document.querySelector("#chart_by_app"), {
    type: 'bar',
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Averge rating comparison by app'
        }
      }
    },
  });
  }
  )


// analysis by region
fetch('/dating_analysis_region.json')
  .then((response) => response.json())
  .then((responseJson) => {
    
    const data = {
      labels: Object.keys(responseJson.data),
      datasets: [
        {
          label: "You",
          data: Object.entries(responseJson.data).map(d => d[1].my_rating),
          borderColor: CHART_COLORS.grey,
          backgroundColor: CHART_COLORS.blue,
          borderWidth: 2,
          borderRadius: 5,
          borderSkipped: false,
        },
        {
          label: 'Other ppl',
          data: Object.entries(responseJson.data).map(d => d[1].other_ppl_rating),
          borderColor: CHART_COLORS.grey,
          backgroundColor: CHART_COLORS.yellow,
          borderWidth: 2,
          borderRadius: 5,
          borderSkipped: false,
        }
      ]
    };

  
  new Chart(document.querySelector("#chart_by_region"), {
    type: 'bar',
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Averge rating comparison by region'
        }
      }
    },
  });
  }
  )


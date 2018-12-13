function processResult(result){
  $('#hard_predict').html(`Your best chance for compensation is ${result.max_prob} if you file ${result.best_day} days after the incident.`);
  makePlot('#vis', result.probs);

}

function makePlot(selector, list_of_probs){
    const yourVlSpec = {
      "$schema": "https://vega.github.io/schema/vega-lite/v3.0.0-rc0.json",
      "description": "A simple line chart with embedded data.",
      "data": {
        "values": list_of_probs.map((prob, index) => {return {'Days': index + 1, 'Probability': prob}; })
      },
      // Properties for any single view specifications
      "mark": {"type": "line", "point": true},
      "encoding": {
        "x": {
          "field": "Days", 
          "type": "nominal",
          "axis": {
            "orient": "bottom",
            "domain": true,
            "domainColor": "#27b7e7",
            "domainWidth": 3,
            "ticks": true,
            "tickColor": "black",
            "title": "Days Waited After Incident To File Claim",
            "titleColor": "#27b7e7",
            "titleFont": "Roboto",
            "titleFontSize": 20,
            "labels": true,
            "labelColor": "black",
            "labelAngle": 0
          
          }    
      },
        "y": {
          "field": "Probability",
          "type": "quantitative",
          "axis": {
            "orient": "left",
            "domain": true,
            "domainColor": "#27b7e7",
            "domainWidth": 3,
            "ticks": true,
            "tickColor": "#27b7e7",
            "title": "Probability",
            "titlePadding": 50,
            "titleAngle": 0,
            "titleColor": "#27b7e7",
            "titleFont": "Roboto",
            "titleFontSize": 20,
            "labels": true,
            "labelColor": "black"

        }
      },
        "color": {"value": "#ff9900ff"}

      }
    };

    vegaEmbed(selector, yourVlSpec);
}


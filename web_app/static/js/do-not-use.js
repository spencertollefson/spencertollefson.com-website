function processResult(result){
  $('#hard_predict').html(`Your best chance for compensation is ${result.max_prob} if you file ${result.best_day} days after the incident.`);
  makePlot('#vis', result.probs);

}

function makePlot(selector, list_of_probs){
    const yourVlSpec = {
      "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
      "description": "A simple line chart with embedded data.",
      "data": {
        "values": list_of_probs.map((prob, index) => {return {'Days': index + 1, 'Probability': prob}; })
      },
      // Properties for any single view specifications
      // "width": ...,
      // "height": ...,
      "mark": {"type": "line", "point": true},
      "encoding": {
        // "size": 10,
        "x": {
          "field": "Days", 
          "type": "ordinal",
          "axis": {
            "orient": "black",
            "domain": true,
            "domainColor": "black",
            "domainWidth": 3,
            "ticks": true,
            "tickColor": "black",
            "title": "Days Waited After Incident To File Claim",
            "titleColor": "black",
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
            "domainColor": "black",
            "domainWidth": 3,
            "ticks": true,
            "tickColor": "black",
            "title": "Probability",
            "titlePadding": 50,
            "titleAngle": 0,
            "titleColor": "black",
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


'use strict';

document.querySelector('#sort').addEventListener("click", (evt) => {
    evt.preventDefault();

    const formInputs = {
        sorting_object: document.querySelector('#sorting_object').value,
        sorting_rule: document.querySelector('#sorting_rule').value,
      };

    fetch("/user/sorting/user_email/api", {
        method: "POST",
        body: JSON.stringify(formInputs),
        headers: {
            'Content-Type': 'application/json',
          },
        })
        .then((response) => response.json())
        .then((result) => {Sort(result)})
});

function Sort(result) {
  
    const divs_objects = document.querySelectorAll('#historical_logs_clean_after_sorting');
    
    for (const div of divs_objects) {
        div.remove()
    };

    for (let number_order in result) {
    
    document.querySelector('#historical_logs').insertAdjacentHTML('beforeend', `
        <div id = "historical_logs_clean_after_sorting">
            <div> 
                <a href= "/user/logs/${result[number_order]["log_id"]}">
                    ${ result[number_order]["log_id"] }
                </a> 
            </div>
            <div> Name: ${ result[number_order]["name"] } </div>
            <div> Overall rating: ${ result[number_order]["overall_rating"] } </div>
            <div> Picture: <img src= ${ result[number_order]["picture"]} /> </div>
        </div>`)
     }


};
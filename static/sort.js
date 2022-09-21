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
        <p>
            <div id = "historical_logs_clean_after_sorting">
                <div class="card mb-3" style="max-width: 540px;">
                <div class="row g-0">
                <div class="col-md-4">
                    <img src=${ result[number_order]["picture"]} class="img-fluid rounded-start profile_pic" >
                </div>
                <div class="col-md-8">
                <div class="card-body">
                    <a href="/user/logs/${result[number_order]["log_id"]}">
                        <h5 class="card-title"> ${ result[number_order]["name"] }</h5>
                    </a> 
                <p class="card-text">
                    Overall rating: ${ result[number_order]["overall_rating"] } <br>
                    Key takeaway:  ${ result[number_order]["key_takeaway"] }
                </p>
                <p class="card-text"><small class="text-muted"> We met on ${ result[number_order]["date_of_the_date"] } </small></p>
                </div>
            </div>
            </div>
        </div>

        </p>
            `)
     }


};
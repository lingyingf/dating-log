'use strict';

document.querySelector('#question_submit').addEventListener("click", (evt) => {
    evt.preventDefault();

    const formInputs = {
        question: document.querySelector('#question').value,
      };
    
    fetch("/user/fortune_telling/answer/api", {
    method: "POST",
    body: JSON.stringify(formInputs),
    headers: {
        'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((result) => {Show_answer(result)})

});


function Show_answer(result) {
    
    const divs_objects = document.querySelectorAll('#result_clean_after_resubmit');
    
    for (const div of divs_objects) {
        div.remove()
    };
    
    document.querySelector('#result').insertAdjacentHTML('beforeend', `
        
        <div id="result_clean_after_resubmit">
            ${result["data"]}
        </div>
`)}
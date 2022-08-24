'use strick';

document.querySelector('#question_submit').addEventListener("submit", (evt) => {
    evt.preventDefault();

    const formInputs = {
        question: document.querySelector('#question').value,
      };
    
    console.log(formInputs)
    
    fetch(`"/user/${user_email}/fortune_telling/answer/api"`, {
    method: "POST",
    body: JSON.stringify(formInputs),
    headers: {
        'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((result) => {console.log(result)})
});
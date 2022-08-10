


// function Sort(result) {

//     return(
//         <div>
//             {% for log_id in result %}
//             <p>
//                 <div> 
//                     <a href= {'/user/logs/${log_id}'}>
//                         {log_id }
//                     </a> 
//                 </div>
//                 <div> Name: { result[log_id]["name"] } </div>
//                 <div> Overall rating: { result[log_id]["overall_rating"] } </div>
//                 <div> Picture: <img src= { result[log_id][picture]} /> </div>
//             </p>
//             {% endfor %}
//         </div>
//     );
    
//     fetch("/user/sorting/<user_email>/api")
//         .then((response) => response.json())
//         .then((result) => Sort(result))
// }

document.querySelector('#sort').addEventListener("submit", (evt) => {
    evt.preventDefault();

    const formInputs = {
        sorting_object: document.querySelector('#sorting_object').value,
        sorting_rule: document.querySelector('#sorting_rule').value,
      };
    
      console.log(formInputs)

    fetch("/user/sorting/<user_email>/api", {
        method: "POST",
        body: JSON.stringify(formInputs),
        headers: {
            'Content-Type': 'application/json',
          },
        })
        .then((response) => response.json())
        .then((result) => console.log(result))
});

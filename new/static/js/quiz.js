function onclickquiz(quizid, option){

 $.ajax({
    type: "POST"
    url:"/quizanswers/"+ quizid + "/" + option
    success: function(response) {
        // This function is called when the server returns a successful response
        console.log('Success:', response);
        // You might want to redirect to the next question or update the page dynamically here
    },
        error: function(xhr, status, error) {
            // This function is called when the request fails
        console.log('Error:', error);
        }
    
    });
 }
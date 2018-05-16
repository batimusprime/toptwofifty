//Empty array to hold results
var movielist = {}
// Initialize Firebase as a database
var database = firebase.database();

//select database by name
var ref = database.ref('movies');

//search for data, with call and error handler
//returns a large object
ref.on('value',gotData,errData);



//Triggers function if data is received from ref
function gotData(data){
    
    var movies = data.val();
    
    //idk if this can be changed as it referenced key/pair values
    var keys = Object.values(movies);
    
    //incrementer
    var i;
    
    //generic for loop
    for (i = 0; i < keys.length; i++) { 
        //iterate through list adding to div   
        $("#maindiv").append("<li><input class='css-checkbox' type='checkbox'>"+keys[i] + "</li>");
}
}

function errData(err){

    console.log('Error: ' + err);
}

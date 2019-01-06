// Shorthand for $( document ).ready()
$(function() {
    
    function populate(){
    for (i=0;i<movies.length;i++){
    
        $("#main_table").append( " <input type=\"checkbox\" name=\"movie"+ i + " \" value=\" "+ i + "\">" + movies[i].name + "<br/>");
            
        
    }
        
 
    }
    //end populate

populate();

});
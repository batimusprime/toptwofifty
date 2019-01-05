// Shorthand for $( document ).ready()
$(function() {
    
    function populate(){
    for (i=0;i<movies.length;i++){
    
        $("#main_table").append( "<input type=\"checkbox\" name=\"vehicle1\" value=\"Bike\">" + movies[i].name + "<br/>");
            
        
    }
    
        
        
 
    }
    //end populate

populate();

});
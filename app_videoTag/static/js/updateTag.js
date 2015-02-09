// // Insert code here to run when the DOM is ready
$(document).ready(function() {
     $(".comment_form").submit(addComment);
    
});

 function addComment(){
     event.preventDefault(); //STOP default action-> store things in the database
     var postData = $(this).serialize();
     var formURL = $(this).attr("action");
     
    
    $.ajax(
    {
        url : formURL,
        type: "POST",
        data : postData,//add comment function
        success:function(data, textStatus, jqXHR) 
        {
            
            var text=data[0].fields.text;
            var created=data[0].fields.created;
            var starttime=data[0].fields.starttime;
            var startsecond=data[0].fields.startsecond;
            
           
            $('<tr class='
            +'"comment"'
            +' id='
            +'"tagidentifier"'
            +' tagsecond='
            + startsecond
            +'>'
            +'<td class='
            +'"comment-heading"'
            +'>'
            +starttime
            +'</td>'
            +'<td class='
            +'"comment-heading"'
            +'>'
            +text
            +'</td>'
            +'<td class='
            +'"comment-heading"'
            +'>'
            +'now'
            +'</td></tr>').prependTo('#tagbody');

            
        },
        error: function(jqXHR, textStatus, errorThrown) 
        {
            console.log("mistake");//if fails      
        }
    });
    
}




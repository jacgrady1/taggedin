// Insert code here to run when the DOM is ready
$(document).ready(function() {
    
    $(".comment").click(seekTo);
    
    // setTimeout(addGrumblr, 10000);
});

function seekTo(){
    event.preventDefault(); //STOP default action-> store things in the database
    var tagsecond=$(this).attr("tagsecond");
    console.log(tagsecond)
    document.getElementById("video-1").currentTime = tagsecond;

}




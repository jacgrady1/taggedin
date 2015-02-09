function init() {
    document._video = document.getElementById("video-1");
    setInterval(update_properties, 250);
}

document.addEventListener("DOMContentLoaded", init, false);


function update_properties() {
    $("#current1").text(document._video.currentTime);
    // console.log($("#current").value)
    
    // pass the current time to a hidden field in html 
    document.getElementById('current').setAttribute('value', document._video.currentTime);  
    // console.log($("#current").value)
    $("#duration").text(document._video.duration);
}

/*An example of all the options of the media API in HTML5
More info here: http://www.w3.org/2010/05/video/mediaevents.html

Buttons styled with RGBA, more info here:
http://zurb.com/article/266/super-awesome-buttons-with-css3-and-rgba
*/
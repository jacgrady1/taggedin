var inst;
var $_
function init() {
    $_ = function(e){return document.getElementById(e);};
   
    inst = ABP.create( document.getElementById('load-player'), {
        'src': document.getElementById('video-1'),
        'width': 600,
        'height': 400
        });
    setInterval(update, 250);
}

window.addEventListener("load",init,false);


function update(){
        //$_("click-load").addEventListener("click", function(e){
        // if(e && e.preventDefault)
        // e.preventDefault();
        var identifier = document.getElementById('identifier');
        var filename=identifier.value+".xml";
        console.log(filename);
        CommentLoader("/static/xml/"+filename, inst.cmManager);
        $_("click-load").style.display= "none";
        //});
    }
   
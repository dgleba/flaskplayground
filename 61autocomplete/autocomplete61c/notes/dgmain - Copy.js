$(document).ready(function(){
    
    // jquery works in html file but not separate file
    // https://www.codecademy.com/forum_questions/5438227f8c1ccc12e6000037
    
    //var $ = jQuery;

    $("#namefld")
    .autocomplete({
        source:function(request, response) {
            $.getJSON("{{url_for('_autocomplete')}}",{
                q: request.term, // in flask, "q" will be the argument to look for using request.args
            }, function(data) {
                response(data.matching_results); // matching_results from jsonify
            });
        },
        minLength: 1,
        select: function(event, ui) {
            console.log(ui.item.value); 
        }
    });
});


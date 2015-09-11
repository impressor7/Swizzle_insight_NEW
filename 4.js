var main = function() {
    $('.btn1').click(function() {
      $(this).css('background-color', 'red');

    });
    $('.btn2').click(function() {
      $(this).css('background-color','red');

    });
    $('.btn3').click(function() {
      $(this).css('background-color','red');

    });
    $('.btn4').click(function() {
      $(this).css('background-color','red');

    });
    $('.topic').click(function() {
      window.location.href = "1.html";
    });


};

var jqxhr = function(){
    $('.up-btn').click(function(){

        $.ajax({
            method:"GET",
            url:"http://127.0.0.1:8080/Swizzle_insight_NEW/data_btn4.py",
            dataType:"text"
        })

        .done(function() {
            alert("SUCCESS");
        })
        .fail(function(){
            alert("ERROR");
        })
        .always(function(){
            alert("COMPLETE");
        });

        location.reload();
    })
};


$(document).ready(main)
$(document).ready(jqxhr)
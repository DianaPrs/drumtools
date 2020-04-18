
function btnClick() {
    $('#table').append(
         '<tr><td>'+$('#rawnotes').val()+'</td><td><input type="button" onClick="delClick();"></td></tr>');  
}

function delClick() {
     $('#table').on('click', 'td', function(){ 
           $(this).parent().remove();
   })
}

function get_notes() {
    $('#myModal').modal("hide")
    $('input[name=name]').val($('input[name=name]').val()+$('div.table').html());       
      $.ajax({
          type: "POST",
          url: "/profile/get_notes",
          data: $('form').serialize(),
          type: 'POST',
          success: function(response) {
              var json = jQuery.parseJSON(response)
              $('#view').html(json.view)
              console.log(response);
                       
            },
          error: function(error) {
              console.log(error);
        }
        
    });
}
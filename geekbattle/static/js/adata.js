     jQuery(document).ready(function() {
    $.get('/level_1/answer_json/').done(function(data){
      for(var i = 0; i < data.length; i++) {


$('#name').append(data[i]["user"]);
           $('#level_2').hide()
	           $('#end').hide()	
	$('#level_3').hide()
	if (data[i]["s1"]>=0)		
	 { $('#level_1').hide();
	 if (data[i]["s1"]>=60)	
	   $('#level_2').show();
	$('#score').append(data[i]["s1"]+"%");}
	else
	  $('#score').append("Pending");
	if (data[i]["s2"]==0)
		           {$('#level_2').hide()
				$('#asd').append("File Submitted")
		           $('#level_3').show()
}
	if (data[i]["s3"]==0)
		           {$('#level_3').hide()
				$('#asd1').append("File Submitted")
				$('#end').show()
		          }
}
    });

      });
//<tr><td><a id="qname'+data[i]["id"]+'" name="qname" href="#">Q1</a></td></tr>

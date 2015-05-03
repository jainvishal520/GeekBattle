     jQuery(document).ready(function() {
     var qid = $('#qid').val();
	
     var url = "/level_1/question_json/"+qid;

    $.get(url).done(function(data){
      for(var i = 0; i < data.length; i++) {
                    $('#choice_1').append(data[i]["choice_1"]);
		$('#choice_2').append(data[i]["choice_2"]);	
		$('#choice_3').append(data[i]["choice_3"]);
		$('#choice_4').append(data[i]["choice_4"]);
		$('#descrip').append(data[i]["description"]);
		document.getElementById("count").innerHTML=data[i]["count"];		

if(data[i]["active_status"]=="1")
{document.getElementById("name").innerHTML="Unmark";
document.getElementById("name").value="0";}
else
{document.getElementById("name").innerHTML="Mark";
document.getElementById("name").value="1";      
}

  document.getElementById("qid1").value=data[i]["id"];
document.getElementById("qid2").value=data[i]["id"];
if(data[i]["answer"]=="1")
document.getElementById('button1').checked = true;
else if(data[i]["answer"]=="2")
document.getElementById('button2').checked = true;
else if(data[i]["answer"]=="3")
document.getElementById('button3').checked = true;
else if(data[i]["answer"]=="4")
document.getElementById('button4').checked = true;


      
    }});

      });

     jQuery(document).ready(function() {
    $.get('/level_1/question_list/').done(function(data){
      for(var i = 0; i < data.length; i+=2) {
                    if (data[i]["answer"] == 0)
                     {  
                         var color="color:#6666ff" 
                      }
                    else 
                     {  
                         var color="color:#F80000"
                      }  
                    if (data[i]["active_status"] == 0)
                     {   
                         var temp ="Q."
			}
                    else
                      {   var temp = "&#8594;"+"Q."
                     
                      }

	

		          if (data[i+1]["answer"] == 0)
                     {  
                         var color1="color:#6666ff" 
                      }
                    else 
                     {  
                         var color1="color:#F80000"
                      }  
                    if (data[i+1]["active_status"] == 0)
                     {   
                         var temp1 ="Q."
			}
                    else
                      {   var temp1 = "&#8594;"+"Q."
                     
                      }


        var tr = '<tr><td><button class ="button_link" id="qname'+data[i]["id"]+'" name="qname" onclick="z(this.id);" value='+data[i]["id"]+'><a style="'+color+'">'+temp+''+data[i]["id"]+'</a></button></td><td></td><td><button class ="button_link" id="qname'+data[i+1]["id"]+'" name="qname" onclick="z(this.id);" value='+data[i+1]["id"]+'><a style="'+color1+'">'+temp1+''+data[i+1]["id"]+'</a></button></td></tr>';
                          $('#task-bod').append(tr);
      }
  
    });

      });


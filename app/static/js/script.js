$(document).ready(function() {
//alert('In');
});


function findTweet(){
	text = '';
    text = $("#textfield").val();
    dict = {'text':text};
    $('.feeds').load('find/',dict);
   

/*
    $.ajax({type:"POST",url:'/find_tweets/',data:dict,
		success:function(data){
		//alert('hello');
		//document.write(dict);
			//str = '/find_tweets/?text='+text;
			//alert(str);
		//location.href=str;
		}
    });
    */
};
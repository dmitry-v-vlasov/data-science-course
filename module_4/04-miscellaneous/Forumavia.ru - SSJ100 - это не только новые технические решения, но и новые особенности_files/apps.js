$(document).ready(function() {


   $('.comm_like, .comm_dislike').click(function() {

   		var ths=$(this);
        var rat_el;
        var pid = ths.parent().attr("data-comm-id");
		var cv = ths.parent().attr("data-can-vote");
		var TP = ths.parent().attr("data-comm-t");
        var el_like=ths.siblings(".comm_like");
       	var el_dislike=ths.siblings(".comm_dislike");
       $.ajax({
         url: '//www.forumavia.ru/apps/like_check.php',
         method: 'post',
         success: function(data){

           if(data != '') {            if (cv==1)
	        	{
                var rate=0;
                var was_like=0;
				var was_dislike=0;

		        var action = "like";
		       	if (ths.hasClass("comm_dislike"))
					{
					action = "dislike";
					}
		       	if (action=='like')
		       		{
		       		rate=1;
		       		if (ths.hasClass("comm_like_on"))
						{
						was_like=1;
						rate=0;
						}
					if (el_dislike.hasClass("comm_dislike_on"))
						{
						was_dislike=1;
						}
		       		}
				if (action=='dislike')
			       	{
			       	rate=-1;
			       	if (ths.hasClass("comm_dislike_on"))
						{
						was_dislike=1;
						rate=0;
						}
					if (el_like.hasClass("comm_like_on"))
						{
						was_like=1;
						}

			       	}

	             $.ajax({
	               url: '//www.forumavia.ru/apps/comm_rate.php',
	               method: 'post',
	               data:{sid:topic_id, pid:pid, rate:rate,tp:TP},
	               success: function(resp){
	                 resp = $.trim(resp);
	                 if(resp != '' && resp != 'error') {

	                 	if (action=='like')
				       		{
							ths.toggleClass("comm_like_on");
							if (el_dislike.hasClass("comm_dislike_on"))
								{
								ths.siblings(".comm_dislike").toggleClass("comm_dislike_on");
								}
				       		}
						if (action=='dislike')
					       	{
							ths.toggleClass("comm_dislike_on")
							if (el_like.hasClass("comm_like_on"))
								{
								ths.siblings(".comm_like").toggleClass("comm_like_on");
								}
					       	}

	                   el_likes=ths.siblings(".comm_rating-count_likes");
	                   el_dislikes=ths.siblings(".comm_rating-count_dislikes");

	                   if (action=='like')
		                   	{
		                   	num_likes=parseInt(el_likes.text())+1;
		                   	num_dislikes=parseInt(el_dislikes.text());
	                        if (was_like==1)
	                        	{
	                        	num_likes=parseInt(el_likes.text())-1;
	                        	}

	                        if (was_dislike==1)
	                        	{
	                        	num_likes=parseInt(el_likes.text())+1;
	                        	num_dislikes=parseInt(el_dislikes.text())-1;
	                        	}
	                        el_likes.text(num_likes);
	                        el_dislikes.text(num_dislikes);

		                   	}
		               else
			               	{
			               	num_likes=parseInt(el_likes.text());
			               	num_dislikes=parseInt(el_dislikes.text())+1;

							if (was_like==1)
	                        	{
	                        	num_likes=parseInt(el_likes.text())-1;
	                        	num_dislikes=parseInt(el_dislikes.text())+1;
	                        	}

	                        if (was_dislike==1)
	                        	{
	                        	num_dislikes=parseInt(el_dislikes.text())-1;
	                        	}

	                        el_likes.text(num_likes);
	                        el_dislikes.text(num_dislikes);

			               	}
	                 }
	               }
             	});
             // end cv
             }

           }
           else {
             $('#popUpWindow').modal('show');
           }
         },
       });
     });
   $('.forum_settings').click(function() {
     $('#ForumSettings').modal('show');
});
   $('.auth,.auth_in').click(function() {     $('#popUpWindow').modal('show');
});

   $('button.login').click(function() {
     	$.ajax({
     		url: '//www.forumavia.ru/apps/signin_check.php',
     		method: 'POST',
     		data: {email:$('#email').val(), passw:$('#passw').val()},
     		success: function(resp) {
     			resp = $.trim(resp);
     			if(resp == '') {
     				$('#popUpWindow').modal('hide');
                         //$('.logout').show();
                         location.reload();
     			} else {
                         $('.txt-msg').html(resp);
                    }
     		}
     	});
     });

	var input_email = document.getElementById("email");
	var input_passw = document.getElementById("passw");

	input_email.addEventListener("keyup", function(event) {
	  event.preventDefault();
	  if (event.keyCode === 13) {
	    document.getElementById("login").click();
	  	}
	});
	input_passw.addEventListener("keyup", function(event) {
	  event.preventDefault();
	  if (event.keyCode === 13) {
	    document.getElementById("login").click();
	  	}
	});

	$('.bookmark').click(function() {		var ths=$(this);
        var typ = ths.attr("data-typ");
        var sid = ths.attr("data-sid");
     	$.ajax({
     		url: '//www.forumavia.ru/apps/bookmark_app.php',
     		method: 'POST',
     		data: {typ:typ, sid:sid},
     		success: function(data) {
                console.log(data);
     			if(data != '') {
					ths.toggleClass("bookmark_on");

                    }
     			}
     		});
     });
    $('.comm_remove').click(function() {
		var ths=$(this);
        var id = ths.attr("data-id");
     	$.ajax({
     		url: '//www.forumavia.ru/apps/comm_remove.php',
     		method: 'POST',
     		data: {id:id},
     		success: function(data) {
                console.log(data);
     			if(data != '') {
					//ths.toggleClass("bookmark_on");
					ths.toggleClass("comm_removed");
					ths.parent('td').toggleClass("comm_removed");
					if (ths.hasClass("comm_removed"))
						{
						//action = "dislike";
						ths.text("восстановить");

						}
					else
						{						ths.text("удалить");						}

                    }
     			}
     		});
     });

	var tooltips = $(document).tooltip({
    	items: ".comm_rating-count_likes, .comm_rating-count_dislikes, .user_profile",
    	position: {
	    	my: "center top",
	        at: "center bottom"
	        },
        content: function (callback) {


			var ttyp = $(this).attr("data-ttyp");
			var mod = $(this).attr("data-mod");

            if (ttyp=='user')
            	{            	var user = $(this).attr("data-user");            	 $.ajax({
				  type: 'POST',
				  url: '//www.forumavia.ru/apps/tooltip_user.php',
				  data: {uid:user,m:mod},
				  success: function(response){

	                    callback(response);
				  		}
					});            	}

            else
            	{            	 var pid = $(this).parent().attr("data-comm-id");
				var TP = $(this).parent().attr("data-comm-t");
				var ACT = $(this).attr("data-comm-act");

	             $.ajax({
				  type: 'POST',
				  url: '//www.forumavia.ru/apps/tooltip_info.php',
				  data: {sid:topic_id, pid:pid, tp:TP,act:ACT},
				  success: function(response){
	                    callback(response);
				  		}
					});
				}
        },
        show: null,
        close: function (event, ui) {
            ui.tooltip.hover(

            function () {
                $(this).stop(true).fadeTo(400, 1);
            },

            function () {
                $(this).fadeOut("400", function () {
                    $(this).remove();
                })
            });
        }
    });






});
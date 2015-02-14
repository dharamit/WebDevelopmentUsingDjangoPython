$(function (){
	var $posts = $('#posts');
	$.ajax({
		type: 'GET',
		url: 'http://127.0.0.1:8000/api/posts',
		success: function(posts){
			//console.log('success',data);
			$.each(posts, function(i,post){
				$posts.append('<li>'+post.author+":   "+post.title+'</li>');
			});
		}
	});
});
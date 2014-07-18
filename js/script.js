$(document).ready(function(){
	
	
	//$('.btntooltip').tooltip();
	
	$('li').click(function(){
		$("[class='active'").removeClass('active');
		$(this).addClass('active');
	});

});

function load_profile(){
	document.getElementById("content").innerHTML='<object type="text/html" data="aboutme.html" class="fullsize" ></object>';
}
function load_work(){
	document.getElementById("content").innerHTML='<object type="text/html" data="work.html" class="fullsize" ></object>';
}
$(
	function () {
		if (location.pathname === "/category/dao") {
			$("#li-dao").addClass("active");
		} else if (location.pathname === "/category/fa") {
			$("#li-fa").addClass("active");
		} else if (location.pathname === "/category/shu") {
			$("#li-shu").addClass("active");
		} else {
			$("#li-index").addClass("active");
		}

		$(document).on("click", ".deleteBlog", function (event) {
			event.preventDefault();
			var $target = $(this);
			bootbox.confirm({ 
  				size: "small",
  				message: "Are you sure?", 
  				callback: function(result){ 
  					if (result) {
  						window.location.href = $target.attr("href")
  					}
  				}
			});
		});
	}
)

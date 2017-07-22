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
	}
)
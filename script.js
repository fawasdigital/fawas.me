var page = document.body.getAttribute("data-page");
var activeNav = document.getElementById("nav-" + page);
if (activeNav) activeNav.classList.add("active");

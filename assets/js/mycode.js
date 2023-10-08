var fooditems = document.querySelector(".food .item");

var elem = document.getElementsByClassName()
elem.onchange = function(){
    var hiddenDiv = document.getElementById("showMe");
    hiddenDiv.style.display = (this.value == "") ? "none":"block";
};